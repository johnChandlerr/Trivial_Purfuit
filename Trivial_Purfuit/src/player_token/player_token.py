
import definitions

from PySide2.QtWidgets import (QWidget)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt, QUrl)
from PySide2.QtMultimedia import (QMediaPlayer)


import definitions


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

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.moves_left = 0

        self.name = player_name
        self.is_current_player = False
        self.question_categories = [definitions.question_type1, definitions.question_type2, definitions.question_type3, definitions.question_type4]
        self.cake_list = {
            self.question_categories[0]:False,
            self.question_categories[1]:False,
            self.question_categories[2]:False,
            self.question_categories[3]:False}
        self.turn_status = False
        self.player_initialized = False
        self.draw_token = False
        self.location = [4, 4]
        self.direction_to_move = ""
        self.done_moving = False
        self.resize(b_width, b_height)
        self.audio_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.audio_player.setMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/player_move.m4a"))
    # end __init__()

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
        return (self.cake_list[self.question_categories[0]] and self.cake_list[self.question_categories[1]] and
                self.cake_list[self.question_categories[2]] and self.cake_list[self.question_categories[3]])

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
        self.qtype1_x_center = self.x + 3
        self.qtype1_y_center = self.y + 2

        #set parameters for center of cake pieces
        self.qtype2_x_center = self.x + 19
        self.qtype2_y_center = self.y + 2

        #set parameters for center of cake pieces
        self.qtype3_x_center = self.x + 3
        self.qtype3_y_center = self.y + 21

        #set parameters for center of cake pieces
        self.qtype4_x_center = self.x + 19
        self.qtype4_y_center = self.y + 21

        #draw people cake (default people cake piece color = blue)
        if self.cake_list[self.question_categories[0]]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            painter.drawRect(self.qtype1_x_center,self.qtype1_y_center,self.cake_width,self.cake_height)

        # draw event cake (default people cake piece color = blue)
        if self.cake_list[self.question_categories[1]]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            painter.drawRect(self.qtype2_x_center, self.qtype2_y_center, self.cake_width, self.cake_height)

        # draw place cake (default people cake piece color = blue)
        if self.cake_list[self.question_categories[2]]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            painter.drawRect(self.qtype3_x_center, self.qtype3_y_center, self.cake_width, self.cake_height)

        # draw holiday cake (default people cake piece color = blue)
        if self.cake_list[self.question_categories[3]]:
            painter.setPen(QPen(Qt.transparent, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawRect(self.qtype4_x_center, self.qtype4_y_center, self.cake_width, self.cake_height)
    # end draw_cakes()