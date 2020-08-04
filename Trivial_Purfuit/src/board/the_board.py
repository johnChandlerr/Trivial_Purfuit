# This Python file uses the following encoding: utf-8

import sys
import definitions

from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox, QInputDialog)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt, SIGNAL)

from Trivial_Purfuit.src.board.board_funcs import board_funcs
from Trivial_Purfuit.src.board.menus.board_menu import BoardMenu
from Trivial_Purfuit.src.player_token.player_token import PlayerToken
from Trivial_Purfuit.src.die.die import Die
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


from functools import partial


class Board(QMainWindow, board_funcs):
    """
     Description
    -------------
        The board for Trivial Purfuit.
        TODO: JGC - Merge the common stuff between board_funcs and this class.
                    There's duplicate code, but you did everything in this class first.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trivial Purfuit Board")
        self.num_row_tiles = 9
        self.num_col_tiles = 9

        self.board_tile_width  = 75
        self.board_tile_height = self.board_tile_width

        self.board_width  = self.num_row_tiles * self.board_tile_width
        self.board_height = self.num_col_tiles * self.board_tile_height

        monitor = QApplication.desktop().screenGeometry(1)
        self.resize(monitor.width(), self.board_height)

        self.person_tile_color     = Qt.red
        self.events_tile_color     = Qt.white
        self.places_tile_color     = Qt.blue
        self.holiday_tile_color    = Qt.green
        self.roll_again_tile_color = Qt.darkGray

        self.players_initialized = False
        self.dice_initialized    = False
        self.number_of_players = 0
        self.die = Die()
        self.board_menu = BoardMenu()
        self.qa_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/test2.csv")
    # end __init__()

    def update_total_players(self, number_players):
        """
         Description
        -------------
            TODO: JGC
        """
        self.number_of_players = number_players
        print(self.number_of_players)
    # end update_total_players()

    def initialize_game(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        monitor = QApplication.desktop().geometry()

        # Navigation Menu setup
        self.board_menu.resize(monitor.width(), monitor.height())
        self.board_menu.ui.navigation_group.move(self.board_width, monitor.height() / 3)

        temp_x = self.board_menu.ui.navigation_group.x()
        temp_y = self.board_menu.ui.navigation_group.y() + self.board_menu.ui.navigation_group.height()
        self.board_menu.ui.misc_group.move(temp_x, temp_y)

        # Connect signals/slots for buttons on board menu
        self.connect(self.board_menu.ui.up_button, SIGNAL("clicked()"), partial(self.start_move, "UP"))
        self.connect(self.board_menu.ui.down_button, SIGNAL("clicked()"), partial(self.start_move, "DOWN"))
        self.connect(self.board_menu.ui.left_button, SIGNAL("clicked()"), partial(self.start_move, "LEFT"))
        self.connect(self.board_menu.ui.right_button, SIGNAL("clicked()"), partial(self.start_move, "RIGHT"))
        self.connect(self.board_menu.ui.reset_button, SIGNAL("clicked()"), self.reset_player)
        self.connect(self.board_menu.ui.roll_die_button, SIGNAL("clicked()"), self.get_dice_value)

        # Player token initialization
        self.initialize_player_tokens()

        # Die Setup/initialization
        self.initialize_dice()

        self.layout().addChildWidget(self.player_widget)
        self.layout().addChildWidget(self.die)
        self.layout().addChildWidget(self.board_menu)

    # end temp_setup()
    def update_dirs(self):
        """
        Hides the movement buttons based on whether or not its a valid move
        Input:
        Output:
        """
        num_dirs = 4
        player_row = self.player_widget.location[0]
        player_col = self.player_widget.location[1]
        self.board_menu.ui.down_button.setVisible(True)
        self.board_menu.ui.up_button.setVisible(True)
        self.board_menu.ui.left_button.setVisible(True)
        self.board_menu.ui.right_button.setVisible(True)

        if self.get_tile_type(player_row + 1, player_col) == "Invalid"\
            or self.player_widget.direction_to_move == "UP":
            self.board_menu.ui.down_button.setVisible(False)
        if self.get_tile_type(player_row - 1, player_col) == "Invalid"\
            or self.player_widget.direction_to_move =="DOWN":
            self.board_menu.ui.up_button.setVisible(False)
        if self.get_tile_type(player_row, player_col - 1) == "Invalid"\
            or self.player_widget.direction_to_move == "RIGHT":
            self.board_menu.ui.left_button.setVisible(False)
        if self.get_tile_type(player_row, player_col + 1) == "Invalid"\
            or self.player_widget.direction_to_move == "LEFT":
            self.board_menu.ui.right_button.setVisible(False)

    def hide_dirs(self):
        self.board_menu.ui.down_button.setVisible(False)
        self.board_menu.ui.up_button.setVisible(False)
        self.board_menu.ui.left_button.setVisible(False)
        self.board_menu.ui.right_button.setVisible(False)

    def avail_dirs(self):
        """
        Determines possible directions the player could move based on current location
        Input: The player token who is currently moving
        Output: List of available directions
        """
        player_row = self.player_widget.location[0]
        player_col = self.player_widget.location[1]
        directions = list()

        if self.get_tile_type(player_row + 1, player_col) != "Invalid":
            directions.append("Down")
        if self.get_tile_type(player_row - 1, player_col) != "Invalid":
            directions.append("Up")
        if self.get_tile_type(player_row, player_col - 1) != "Invalid":
            directions.append("Left")
        if self.get_tile_type(player_row, player_col + 1) != "Invalid":
            directions.append("Right")

        return directions

    def get_dice_value(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.player_widget.moves_left = self.die.roll()
        self.player_widget.direction_to_move = "NONE"
        self.board_menu.ui.dice_field.clear()
        self.board_menu.ui.dice_field.insertPlainText(str(self.player_widget.moves_left))
        self.update_dirs()
        self.board_menu.ui.roll_die_button.setVisible(False)
        if self.player_widget.moves_left == 6:
            self.hide_dirs()
            self.board_menu.ui.roll_die_button.setVisible(True)
            options = ["None", "People", "Event", "Location", "Holiday"]
            answer, valid_input = QInputDialog().getItem(self, "Select Cake Headquarters", "Select:", options, 0, False)
            #answer = str(answer).lower()
            #if valid_input:
                #answer = str(answer)

            if answer == "People":
                self.player_widget.location[0] = 4
                self.player_widget.location[1] = 8
                self.player_widget.x = self.board_tile_width * 9  - self.player_widget.width
                self.player_widget.y = self.board_tile_height * 5 - self.player_widget.height

            elif answer == "Event":
                self.player_widget.location[0] = 8
                self.player_widget.location[1] = 4
                self.player_widget.x = self.board_tile_width * 5  - self.player_widget.width
                self.player_widget.y = self.board_tile_height * 9 - self.player_widget.height

            elif answer == "Location":
                self.player_widget.location[0] = 0
                self.player_widget.location[1] = 4
                self.player_widget.x = self.board_tile_width * 5  - self.player_widget.width
                self.player_widget.y = self.board_tile_height * 1 - self.player_widget.height

            elif answer == "Holiday":
                self.player_widget.location[0] = 4
                self.player_widget.location[1] = 0
                self.player_widget.x = self.board_tile_width * 1  - self.player_widget.width
                self.player_widget.y = self.board_tile_height * 5 - self.player_widget.height

            else:
                print("No Cake Piece Tile Selected, Staying Here")

            self.player_widget.turn_status = True
            self.player_widget.draw_token  = True
            self.player_widget.update()
            self.perform_tile_action()
            self.board_menu.ui.dice_field.clear()
        # Updates the dice image to immediately reflect the correct image.
        self.die.update()
    # end get_dice_value()

    def start_move(self, label):
        """
         Description
        -------------
         - TODO: JGC
        """
        try:
            if (label == "UP" or label == "DOWN" or
                label == "LEFT" or label == "RIGHT"):

                while (self.player_widget.moves_left > 0):
                    self.player_widget.direction_to_move = label
                    self.player_widget.turn_status = True

                    self.player_widget.update_location()
                    self.update_dirs()
                    self.player_widget.moves_left = self.player_widget.moves_left - 1
                    self.board_menu.ui.dice_field.clear()
                    self.board_menu.ui.dice_field.insertPlainText(str(self.player_widget.moves_left))

                    if len(self.avail_dirs()) > 2 and self.player_widget.moves_left != 0:
                        break
                    else:
                        if self.player_widget.location == [0, 0]:
                            if self.player_widget.direction_to_move == "UP":
                                #self.player_widget.direction_to_move = "RIGHT"
                                label = "RIGHT"
                            else:
                                #self.player_widget.direction_to_move = "DOWN"
                                label = "DOWN"
                        elif self.player_widget.location == [0, 8]:
                            if self.player_widget.direction_to_move == "UP":
                                #self.player_widget.direction_to_move = "DOWN"
                                label = "LEFT"
                            else:
                                #self.player_widget.direction_to_move = "LEFT"
                                label = "DOWN"
                        elif self.player_widget.location == [8, 0]:
                            if self.player_widget.direction_to_move == "DOWN":
                                #self.player_widget.direction_to_move = "RIGHT"
                                label = "RIGHT"
                            else:
                                #self.player_widget.direction_to_move = "UP"
                                label = "UP"
                        elif self.player_widget.location == [8, 8]:
                            if self.player_widget.direction_to_move == "DOWN":
                                #self.player_widget.direction_to_move = "LEFT"
                                label = "LEFT"
                            else:
                                #self.player_widget.direction_to_move = "UP"
                                label = "UP"

                    if self.player_widget.moves_left == 0:
                        self.player_widget.done_moving = True
                    # end if

                    # Manually calls the paint QEvent.
                    self.update()

                    # Once the player is out of spaces to move, prompt the player with a
                    # question from the QA Manager.
                    # TODO: JGC - Prompt the player with a question.
                    if self.player_widget.moves_left == 0 and self.player_widget.done_moving:
                        self.hide_dirs()
                        self.board_menu.ui.roll_die_button.setVisible(True)
                        self.player_widget.done_moving = False
                        self.perform_tile_action()
                    # end if

                else:
                    print("No moves left!")
        except ValueError:
            print("[ERROR] Invalid dice roll amount!")
    # end start_move()

    def initialize_player_tokens(self):
        """
         Description
        -------------
         TODO: JGC - We only support one player for proof-of-concept.
                     Once we have finalized all the core functionality
                     and integration between all subsystems, we will add
                     multiplayer features.

        """
        self.player_widget = PlayerToken("John")
        self.player_widget.board_tile_height = self.board_tile_height
        self.player_widget.board_tile_width  = self.board_tile_width
        self.player_widget.resize(self.board_width, self.board_height)
    # end initialize_player_tokens()

    def initialize_dice(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.die.board_tile_height = self.board_tile_height
        self.die.board_tile_width  = self.board_tile_width
        self.die.resize(self.board_width, self.board_height)
    # end initialize_dice()

    def reset_player(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.player_widget.direction_to_move = "NONE"
        self.player_widget.player_initialized = False
        self.player_widget.turn_status = False
        self.player_widget.done_moving = False
        self.player_widget.moves_left = 0
        self.player_widget.location[0] = 4
        self.player_widget.location[1] = 4
        self.board_menu.ui.dice_field.clear()
        self.update_dirs()
        self.board_menu.ui.roll_die_button.setVisible(True)
        self.player_widget.update()
    # end reset_player()

    def is_roll_again_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a holiday tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 0) or (row == 0 and col == 8) or
            (row == 8 and col == 0) or (row == 8 and col == 8)):
            return True
        # end if
    # end isRollAgainTile()

    def is_person_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a person tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 3) or (row == 0 and col == 6) or
            (row == 1 and col == 0) or (row == 3 and col == 4) or
            (row == 4 and col == 2) or (row == 4 and col == 8) or
            (row == 5 and col == 0) or (row == 7 and col == 4) or
            (row == 8 and col == 1) or (row == 8 and col == 7)):
            return True
        # end if
    # end isPersonTile()

    def is_event_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is an event tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 2) or (row == 0 and col == 5) or
            (row == 2 and col == 0) or (row == 2 and col == 4) or
            (row == 3 and col == 8) or
            (row == 4 and col == 1) or (row == 4 and col == 5) or
            (row == 7 and col == 0) or (row == 7 and col == 8) or
            (row == 8 and col == 4)):
            return True
        # end if
    # end isEventTile()

    def is_place_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a location/place tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 4) or (row == 1 and col == 8) or
            (row == 3 and col == 0) or
            (row == 4 and col == 3) or (row == 4 and col == 7) or
            (row == 6 and col == 0) or (row == 6 and col == 4) or
            (row == 6 and col == 8) or
            (row == 8 and col == 2) or (row == 8 and col == 5)):
            return True
        # end if
    # end isPlaceTile()

    def is_holiday_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a holiday tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 1) or (row == 0 and col == 7) or
            (row == 1 and col == 4) or (row == 2 and col == 8) or
            (row == 4 and col == 0) or (row == 4 and col == 6) or
            (row == 5 and col == 4) or (row == 5 and col == 8) or
            (row == 8 and col == 3) or (row == 8 and col == 6)):
            return True
        # end if
    # end isHolidayTile()

    def is_hub_tile(self, row, col):
        """
        Description
        -------------
        Checks if the current row and column position is the hub tile.

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if (row == 4 and col == 4):
            return True
    # end is_hub_tile()

    def is_cake_tile(self, row, col):
        """
        Description
        -------------
        Checks if the current row and column position is a cake tile.

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 4) or (row == 4 and col == 0) or
            (row == 4 and col == 8) or (row == 8 and col ==4)):
            return True
    # end is_cake_tile()

    def get_tile_type(self, row, col):
        """
        Description
        -------------
        Utilizes previous methods for tile checking to return a string of
        what tile type the current row and column position is

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if self.is_hub_tile(row, col):
             return "hub"
        elif self.is_person_tile(row, col):
            return "People"
        elif self.is_holiday_tile(row, col):
            return "Holiday"
        elif self.is_place_tile(row, col):
            return "Location"
        elif self.is_event_tile(row, col):
            return "Event"
        elif self.is_roll_again_tile(row, col):
            return "roll_again"
        else:
            return "Invalid"
    # end get_tile_type()

    def paintEvent(self, event):
        """
         Description
        -------------
         - Draws the board and player tokens

         Parameters
        -------------
         (1) event: The event signal (QEvent.Type.Paint).
        """

        self.draw_board()

        if not self.dice_initialized:
            self.die.update()
            self.dice_initialized = True
        # end if

        self.do_player_turn()
    # end paintEvent()

    def do_player_turn(self):
        """
         Description
        -------------
         TODO: JGC
        """
        if not self.players_initialized:
            self.player_widget.update()
            self.players_initialized = True
        # end if

        if self.player_widget.turn_status:
            self.player_widget.draw_token = True
            self.player_widget.update()
            self.player_widget.turn_status = False
        # end if
    # end move_player_token()

    def perform_tile_action(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.player_widget.update()
        tile_type = self.get_tile_type(self.player_widget.location[0], self.player_widget.location[1])
        print("The Tile/Question Type Received: " + tile_type)

        if (tile_type == "People" or tile_type == "Holiday" or
            tile_type == "Location" or tile_type == "Event"):

            good_answer = self.ask_question(self.player_widget, tile_type, isCake=False)

            if good_answer:
                # Verify this is a "Cake" Tile before awarding cake piece.
                if self.is_cake_tile(self.player_widget.location[0], self.player_widget.location[1]):
                    self.player_widget.award_cake_piece(cake_category=tile_type)

        elif (tile_type == "roll_again"):
            QMessageBox.question(self, 'Congratulations!', 'Roll Again!', QMessageBox.Ok)

        elif (tile_type == "hub"):
            options = ["None", "People", "Event", "Location", "Holiday"]
            # Verify the player token has all cake pieces awarded before answering the
            # winning question, otherwise ask random question
            if self.player_widget.all_cake_pieces_present():
                answer, valid_input = QInputDialog().getItem(
                    self, "Select Cake Headquarters", "!OTHER PLAYERS! Select the winning question category:",
                    options, 0, False)
                good_answer = self.ask_question(self.player_widget, answer, isCake=False)

                if good_answer:
                    QMessageBox.question(self, 'Congratulations!', 'YOU WIN!', QMessageBox.Ok)
                    QApplication.quit()
            else:
                answer, valid_input = QInputDialog().getItem(
                    self, "Select Cake Headquarters", "Select the question category:",
                    options, 0, False)
                self.ask_question(self.player_widget, answer, isCake=False)

        else:
            print("Invalid Tile/Question Type Received")
            print("Row: " + str(self.player_widget.location[0]))
            print("Col: " + str(self.player_widget.location[1]))
    # end prompt_player_with_question

    def draw_board(self):
        """
         Description
        -------------
         - Paint all of the tiles for the Trivial Purfuit board

         Parameters
        -------------
         (1) event: The event signal (QEvent.Type.Paint).

         NOTE/TODO
        -------------
         (1) Don't be lazy and brute force..
         (2) Run the current board layout by the team
        """
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))

        x = 0
        y = 0

        # The board is drawn from left to right.
        for row in range(self.num_row_tiles):
            for col in range(self.num_col_tiles):

                if self.is_roll_again_tile(row, col):
                    painter.setBrush(QBrush(self.roll_again_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.is_person_tile(row, col):
                    painter.setBrush(QBrush(self.person_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.is_holiday_tile(row, col):
                    painter.setBrush(QBrush(self.holiday_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.is_event_tile(row, col):
                    painter.setBrush(QBrush(self.events_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.is_place_tile(row, col):
                    painter.setBrush(QBrush(self.places_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                # end if

                # TODO: Add image for the center tile and HQ tiles
                '''
                elif self.isHQTile(row, col):
                    tmp_painter.setBrush(QBrush(self.places_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                '''
                # Update to x-coordinate for next tile
                x = x + self.board_tile_width
            # end for

            # Reset (x,y) starting coordinates for next row and columns
            y = y + self.board_tile_height
            x = 0

        # end for
        self.board_initialized = True
    # end draw_board()


# TODO: If the board is not starting point of the application, remove this main when done testing after demo
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        board = Board()
        board.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
