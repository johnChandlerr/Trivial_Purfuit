
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush)
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

        self.moves_left = 0

        self.name = player_name
        self.cake_list = {
            "people":False,
            "event":False,
            "place":False,
            "holiday":False}
        self.turn_status = False
        self.player_initialized = False
        self.draw_token = False
        self.location = [4, 4]
        self.direction_to_move = ""
        self.done_moving = False

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

    def update_location(self):
        direction = self.direction_to_move

        if direction == "UP":
            self.y = self.y - self.board_tile_height
            self.location[0] = self.location[0] - 1

        elif direction == "DOWN":
            self.y = self.y + self.board_tile_height
            self.location[0] = self.location[0] + 1

        elif direction == "LEFT":
            self.x = self.x - self.board_tile_width
            self.location[1] = self.location[1] - 1

        elif direction == "RIGHT":
            self.x = self.x + self.board_tile_width
            self.location[1] = self.location[1] + 1
    # end update_location()

    def draw_player(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.darkMagenta, Qt.SolidPattern))

        if not self.player_initialized:
            self.x = self.board_tile_width * 5  - self.width
            self.y = self.board_tile_height * 5 - self.height
            self.player_initialized = True

        painter.drawRect(self.x, self.y, self.width, self.height)
        self.draw_token = False
    # end draw_player()