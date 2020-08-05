
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush, QColor)
from PySide2.QtCore import (Qt, QRect)

class PlayerToken(QWidget):
    """
    The Player Token class to store game progress per player and interact with Board.
    """
    def __init__(self, player_name, b_width, b_height, x_offset, y_offset):
        """
        Construct a PlayerToken instance for a player based on name Provided by Board and an empty cake piece Dictionary
        """
        super().__init__()

        self.width  = 35
        self.height = self.width

        self.cake_width = 13
        self.cake_height = self.cake_width

        self.board_tile_width  = b_width
        self.board_tile_height = b_height

        self.x = self.board_tile_width * 5  - (self.width * x_offset)
        self.y = self.board_tile_width * 5  - (self.height * y_offset)

        self.moves_left = 0

        self.purple = QColor('#9065e5')
        self.name = player_name
        self.is_current_player = False
        self.cake_list = {
            "People":False,
            "Event":False,
            "Location":False,
            "Holiday":False}
        self.turn_status = False
        self.player_initialized = False
        self.draw_token = False
        self.location = [4, 4]
        self.direction_to_move = ""
        self.done_moving = False
        self.resize(b_width, b_height)

    def check_cake_piece(self,cake_category):
        """
        Check whether a cake piece has been given for a cake_category, if cake piece not awarded, then award
        :param cake_category:
        :return: indication that cake piece has been awarded
        """
        return self.cake_list[cake_category]

    def all_cake_pieces_present(self):
        """
        TODO: JGC
        """
        return (self.cake_list["People"] and self.cake_list["Event"] and
                self.cake_list["Holiday"] and self.cake_list["Location"])

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
        self.draw_cakes()
    # end paintEvent()

    def update_location(self, direction=None):
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

        if self.is_current_player:
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        else:
            painter.setPen(QPen(Qt.lightGray, 5, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        painter.drawRect(self.x, self.y, self.width, self.height)
        self.draw_token = False
    # end draw_player()

    def draw_cakes(self):
        painter = QPainter(self)

        #set parameters for center of cake pieces
        self.people_x_center = self.x + 3
        self.people_y_center = self.y + 2

        #set parameters for center of cake pieces
        self.event_x_center = self.x + 19
        self.event_y_center = self.y + 2

        #set parameters for center of cake pieces
        self.place_x_center = self.x + 3
        self.place_y_center = self.y + 21

        #set parameters for center of cake pieces
        self.holiday_x_center = self.x + 19
        self.holiday_y_center = self.y + 21

        #draw people cake (default people cake piece color = blue)
        if self.cake_list["People"]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawRect(self.people_x_center,self.people_y_center,self.cake_width,self.cake_height)

        # draw event cake (default people cake piece color = blue)
        if self.cake_list["Event"]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            painter.drawRect(self.event_x_center, self.event_y_center, self.cake_width, self.cake_height)

        # draw place cake (default people cake piece color = blue)
        if self.cake_list["Location"]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            painter.drawRect(self.place_x_center, self.place_y_center, self.cake_width, self.cake_height)

        # draw holiday cake (default people cake piece color = blue)
        if self.cake_list["Holiday"]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawRect(self.holiday_x_center, self.holiday_y_center, self.cake_width, self.cake_height)
    # end draw_cakes()