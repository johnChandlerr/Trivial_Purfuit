# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt, SIGNAL)

from Trivial_Purfuit.src.board.board_funcs import board_funcs
from Trivial_Purfuit.src.player_token import player_token
from Trivial_Purfuit.src.die.die import Die
from Trivial_Purfuit.src.board.menus.board_menu import BoardMenu
from functools import partial


class Board(QMainWindow):
    """
     Description
    -------------
        The board for Trivial Purfuit.
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

        monitor = QApplication.desktop().geometry()
        self.resize(monitor.width(), self.board_height)

        self.person_tile_color     = Qt.red
        self.events_tile_color     = Qt.white
        self.places_tile_color     = Qt.blue
        self.holiday_tile_color    = Qt.green
        self.roll_again_tile_color = Qt.darkGray

        self.players_initialized = False
        self.move_player = False
        self.number_of_players = 0

        self.board_menu = BoardMenu()
        self.die        = Die()
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
         - Temporary function to setup some Qt GUI functionality for proof-of-concept testing.
        """
        monitor = QApplication.desktop().geometry()

        # Navigation Menu setup
        self.board_menu.resize(monitor.width(), monitor.height())
        self.board_menu.ui.navigation_group.move(self.board_width, monitor.height() / 3)

        temp_x = self.board_menu.ui.navigation_group.x()
        temp_y = self.board_menu.ui.navigation_group.y() + self.board_menu.ui.navigation_group.height()
        self.board_menu.ui.misc_group.move(temp_x, temp_y)

        self.connect(self.board_menu.ui.up_button, SIGNAL("clicked()"), partial(self.start_move, "UP"))
        self.connect(self.board_menu.ui.down_button, SIGNAL("clicked()"), partial(self.start_move, "DOWN"))
        self.connect(self.board_menu.ui.left_button, SIGNAL("clicked()"), partial(self.start_move, "LEFT"))
        self.connect(self.board_menu.ui.right_button, SIGNAL("clicked()"), partial(self.start_move, "RIGHT"))
        self.board_menu.ui.reset_button.clicked.connect(self.reset_player)

        self.initialize_player_tokens()
        self.layout().addChildWidget(self.player_widget)
        self.layout().addChildWidget(self.board_menu)
    # end temp_setup()

    def start_move(self, label):
        try:
            if (label == "UP" or label == "DOWN" or
                label == "LEFT" or label == "RIGHT"):
                self.player_widget.direction_to_move = label

                self.dice_amount = int(self.board_menu.ui.dice_field.toPlainText())
                self.move_player = True
                self.player_widget.turn_status = self.move_player

                # Manually calls a the paint QEvent.
                self.update()

        except ValueError:
            print("[ERROR] Invalid dice roll amount!")

    # end get_direction()

    def initialize_player_tokens(self):
        # TODO: Temp. one player for proof-of-concept

        self.player_widget = player_token.PlayerToken("John")
        self.player_widget.board_tile_height = self.board_tile_height
        self.player_widget.board_tile_width  = self.board_tile_width
        self.player_widget.resize(self.board_width, self.board_height)
    # end initialize_player_tokens()

    def reset_player(self):
        self.player_widget.direction_to_move = "NONE"
        self.player_widget.player_initialized = False
        self.player_widget.update()
    # end reset_player()

    def get_dice_amount(self):
        self.dice_amount = int(self.dice_text_field.toPlainText())
        self.move_player = True
        self.player_widget.turn_status = self.move_player

        # Manually calls a the paint QEvent.
        self.update()
    # end get_dice_amount()

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
            return "people"
        elif self.is_holiday_tile(row, col):
            return "holiday"
        elif self.is_place_tile(row, col):
            return "place"
        elif self.is_event_tile(row, col):
            return "event"
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
        self.move_player_token()
    # end paintEvent()

    def move_player_token(self):
        """
         Description
        -------------
         TODO: JGC
        """
        if not self.players_initialized:
            self.player_widget.update()
            self.players_initialized = True
        # end if

        if self.move_player:
            self.player_widget.dice_amount = int(self.dice_amount)
            self.player_widget.draw_token = True
            self.player_widget.update()
            self.move_player = False
        # end if
    # end move_player_token()


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
