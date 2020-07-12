# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import (QApplication)
from PySide2.QtWidgets import (QWidget)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt)


class Board(QWidget):
    """
     Description
    -------------
        The board for Trivial Purfuit.
    """
    def __init__(self):
        super().__init__()

        self.num_row_tiles = 9
        self.num_col_tiles = 9

        self.board_tile_width  = 75
        self.board_tile_height = self.board_tile_width

        self.board_width  = self.num_row_tiles * self.board_tile_width
        self.board_height = self.num_col_tiles * self.board_tile_height

        self.resize(self.board_width, self.board_height)

        self.person_tile_color     = Qt.red
        self.events_tile_color     = Qt.white
        self.places_tile_color     = Qt.blue
        self.holiday_tile_color    = Qt.green
        self.roll_again_tile_color = Qt.darkGray


    def isRollAgainTile(self, row, col):
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
    # end isRollAgainTile()

    def isPersonTile(self, row, col):
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
    # end isPersonTile()

    def isEventTile(self, row, col):
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
    # end isEventTile()

    def isPlaceTile(self, row, col):
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
    # end isPlaceTile()

    def isHolidayTile(self, row, col):
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
    # end isHolidayTile()

    def paintEvent(self, event):
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
        tmp_painter = QPainter(self)
        tmp_painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        tmp_painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        x = 0
        y = 0

        # The board is drawn from left to right.
        for row in range(self.num_row_tiles):
            for col in range(self.num_col_tiles):

                if self.isRollAgainTile(row, col):
                    tmp_painter.setBrush(QBrush(self.roll_again_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.isPersonTile(row, col):
                    tmp_painter.setBrush(QBrush(self.person_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.isHolidayTile(row, col):
                    tmp_painter.setBrush(QBrush(self.holiday_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.isEventTile(row, col):
                    tmp_painter.setBrush(QBrush(self.events_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                elif self.isPlaceTile(row, col):
                    tmp_painter.setBrush(QBrush(self.places_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)

                # TODO: Add image for the center tile and HQ tiles
                '''
                elif self.isHQTile(row, col):
                    tmp_painter.setBrush(QBrush(self.places_tile_color, Qt.SolidPattern))
                    tmp_painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                '''
                # Update to x-coordinate for next tile
                x = x + self.board_tile_width

            # Reset (x,y) starting coordinates for next row and columns
            y = y + self.board_tile_height
            x = 0
    # end paintEvent()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        board = Board()
        board.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)