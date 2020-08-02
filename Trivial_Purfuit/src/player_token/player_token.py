
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush, QColor)
from PySide2.QtCore import (Qt, QRect)

class PlayerToken(QWidget):
    """
    The Player Token class to store game progress per player and interact with Board.
    """
    def __init__(self, player_name):
        """
        Construct a PlayerToken instance for a player based on name Provided by Board and an empty cake piece Dictionary
        """
        super().__init__()

        self.width  = 35
        self.height = self.width
        self.x = 0
        self.y = 0
        self.board_tile_width  = 0
        self.board_tile_height = self.board_tile_width

        self.dice_amount = 0

        self.purple = QColor('#9065e5')
        self.name = player_name
        self.cake_list = {
            "people":False,
            "event":False,
            "place":False,
            "holiday":False}
        self.turn_status = False
        self.player_initialized = False
        self.draw_token = False
        self.location = []
        self.direction_to_move = ""


    def check_cake_piece(self,cake_category):
        """
        Check whether a cake piece has been given for a cake_category, if cake piece not awarded, then award
        :param cake_category:
        :return: indication that cake piece has been awarded
        """
        return self.cake_list[cake_category]


    def award_cake_piece(self, cake_category):
        """
        Get a random question of the provided type
        :param question_type: The type of question the user wants to retrieve
        :return: Confirmation of cake piece type awarded
        """
        if self.cake_list[cake_category] == False:
            self.cake_list[cake_category] = True


    def paintEvent(self, event):
        self.draw_player()
    # end paintEvent()


    def draw_player(self):
        spaces    = self.dice_amount
        direction = self.direction_to_move

        painter = QPainter(self)
        #painter.setClipRect(QRect(0, 0, 1900, 1900))
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(self.purple, Qt.SolidPattern))

        if not self.player_initialized:
            self.x = self.board_tile_width * 5  - self.width
            self.y = self.board_tile_height * 5 - self.height
            self.player_initialized = True

        elif self.draw_token:
            if direction == "UP":
                self.y = self.y - (self.board_tile_height * spaces)
                print("UP Player X: ", self.x)
                print("UP Player Y: ", self.y)

            elif direction == "DOWN":
                self.y = self.y + (self.board_tile_height * spaces)
                print("DOWN Player X: ", self.x)
                print("DOWN Player Y: ", self.y)

            elif direction == "LEFT":
                self.x = self.x - (self.board_tile_width * spaces)

            elif direction == "RIGHT":
                self.x = self.x + (self.board_tile_width * spaces)


        painter.drawRect(self.x, self.y, self.width, self.height)
        self.draw_token = False
    # end draw_player()