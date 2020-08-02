# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt, SIGNAL)


from Trivial_Purfuit.src.board import board_funcs

from Trivial_Purfuit.src.player_token import player_token

from Trivial_Purfuit.src.die import die

from functools import partial


class Board(QMainWindow, board_funcs.board_funcs):
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

        self.temp_setup()
        self.players_initialized = False
        self.move_player = False
        self.dice_initialized = False

    def temp_setup(self):
        """
         Description
        -------------
         - Temporary function to setup some Qt GUI functionality for proof-of-concept testing.
        """
        monitor = QApplication.desktop().geometry()

        # TODO: Remove these buttons once you're done testing and showing proof-of-concept
        up_button    = QPushButton("UP", self)
        down_button  = QPushButton("DOWN", self)
        left_button  = QPushButton("LEFT", self)
        right_button = QPushButton("RIGHT", self)

        up_button.move(self.board_width, monitor.height() / 3 - up_button.height())
        down_button.move(self.board_width, monitor.height() / 3 - (up_button.height() * 2))
        left_button.move(self.board_width, monitor.height() / 3 - (up_button.height() * 3))
        right_button.move(self.board_width, monitor.height() / 3 - (up_button.height() * 4))

        self.connect(up_button, SIGNAL("clicked()"), partial(self.get_direction, "UP"))
        self.connect(down_button, SIGNAL("clicked()"), partial(self.get_direction, "DOWN"))
        self.connect(left_button, SIGNAL("clicked()"), partial(self.get_direction, "LEFT"))
        self.connect(right_button, SIGNAL("clicked()"), partial(self.get_direction, "RIGHT"))

        get_dice_amount_button = QPushButton("Move Player", self)
        get_dice_amount_button.move(self.board_width, monitor.height() / 3)
        get_dice_amount_button.clicked.connect(self.get_dice_amount)
        get_dice_amount_button.show()

        reset_player_button = QPushButton("Reset", self)
        reset_player_button.move(get_dice_amount_button.x() + get_dice_amount_button.width(),
                                 get_dice_amount_button.y() + get_dice_amount_button.height())
        reset_player_button.clicked.connect(self.reset_player)
        reset_player_button.show()

        self.dice_text_field = QTextEdit("<Enter Dice Amount>", self)
        self.dice_text_field.move(self.board_width + 100, monitor.height() / 3)
        self.dice_text_field.show()

        roll_dice_button = QPushButton("Roll & Move", self)
        roll_dice_button.move(self.board_width, monitor.height() / 3 - (up_button.height() * 5))
        roll_dice_button.clicked.connect(self.roll_dice)
        roll_dice_button.show()

        self.initialize_player_tokens()
        self.initialize_dice()
        self.layout().addChildWidget(self.player_widget)
        self.layout().addChildWidget(self.dice_widget)
    # end temp_setup()


    def get_direction(self, label):
        if (label == "UP" or label == "DOWN" or
            label == "LEFT" or label == "RIGHT"):
            self.player_widget.direction_to_move = label

        else:
            raise NameError("Invalid Direction Received")
    # end get_direction()

    def initialize_player_tokens(self):
        # TODO: Temp. one player for proof-of-concept
        self.player_widget = player_token.PlayerToken("John")
        self.player_widget.board_tile_height = self.board_tile_height
        self.player_widget.board_tile_width  = self.board_tile_width
        self.player_widget.resize(self.board_width, self.board_height)
    # end initialize_player_tokens()

    def initialize_dice(self):
        self.dice_widget = die.Die()
        self.dice_widget.board_tile_height = self.board_tile_height
        self.dice_widget.board_tile_width = self.board_tile_width
        self.dice_widget.resize(self.board_width, self.board_height)
    # end initialize_dice()

    def reset_player(self):
        self.player_widget.direction_to_move = "NONE"
        self.player_widget.player_initialized = False
        self.player_widget.update()
    # end reset_player()

    def roll_dice(self):
        roll_num = int(self.dice_widget.roll())
        self.dice_amount = roll_num
        self.move_player = True
        self.player_widget.turn_status = self.move_player
        self.update()
    # end roll_dice()

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
            self.dice_widget.update()
            self.dice_initialized = True
        # end if

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
    # end paintEvent()


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
