# This Python file uses the following encoding: utf-8

import sys
import definitions
from functools import partial

from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox, QInputDialog)
from PySide2.QtGui import (QPainter, QPen, QBrush, QImage)
from PySide2.QtCore import (Qt, SIGNAL, QUrl, QRect)
from PySide2.QtMultimedia import (QMediaPlayer, QMediaPlaylist)

from Trivial_Purfuit.src.board.board_funcs import board_funcs
from Trivial_Purfuit.src.board.menus.board_menu import BoardMenu
from Trivial_Purfuit.src.board.menus.restart_menu import RestartMenu
from Trivial_Purfuit.src.player_token.player_token import PlayerToken
from Trivial_Purfuit.src.die.die import Die
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


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

        self.board_tile_width  = 95
        self.board_tile_height = self.board_tile_width

        self.board_width  = self.num_row_tiles * self.board_tile_width
        self.board_height = self.num_col_tiles * self.board_tile_height

        monitor = QApplication.desktop().geometry()
        self.resize(monitor.width(), self.board_height)

        self.qtype1_tile_color     = Qt.red
        self.qtype2_tile_color     = Qt.white
        self.qtype3_tile_color     = Qt.blue
        self.qtype4_tile_color    = Qt.green
        self.roll_again_tile_color = Qt.darkGray

        self.players_initialized = False
        self.dice_initialized    = False

        # Background music playlist
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/circles.m4a"))
        self.playlist.addMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/got_what_i_got.m4a"))
        self.playlist.addMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/death_bed.m4a"))
        self.playlist.addMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/nikes_on_my_feet.m4a"))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.playlist_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playlist_player.setPlaylist(self.playlist)

        self.number_of_players = 0
        self.player_list = []
        self.die = Die()
        self.board_menu = BoardMenu()
        self.qa_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/questions-and-answers.csv")
        self.question_categories = [definitions.question_type1, definitions.question_type2, definitions.question_type3, definitions.question_type4]
        self.image_path = definitions.ROOT_DIR + "/Trivial_Purfuit/src/board/images/"
        self.restart_menu = RestartMenu()
    # end __init__()

    def initialize_game(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        monitor = QApplication.desktop().geometry()

        # Navigation Menu setup
        self.board_menu.resize(monitor.width(), monitor.height())
        self.board_menu.ui.player_order_group_box.move(self.board_width, self.board_menu.ui.player_order_group_box.y())
        self.board_menu.ui.navigation_group.move(self.board_width, monitor.height() / 3)

        temp_x = self.board_menu.ui.navigation_group.x()
        temp_y = self.board_menu.ui.navigation_group.y() + self.board_menu.ui.navigation_group.height()

        self.board_menu.ui.misc_group.move(temp_x, temp_y)
        self.board_menu.ui.audio_group.move(self.board_menu.ui.misc_group.x(),
                                            self.board_menu.ui.misc_group.y() + self.board_menu.ui.misc_group.height())
        # Connect signals/slots for buttons on board menu
        self.connect(self.board_menu.ui.up_button, SIGNAL("clicked()"), partial(self.start_move, "UP"))
        self.connect(self.board_menu.ui.down_button, SIGNAL("clicked()"), partial(self.start_move, "DOWN"))
        self.connect(self.board_menu.ui.left_button, SIGNAL("clicked()"), partial(self.start_move, "LEFT"))
        self.connect(self.board_menu.ui.right_button, SIGNAL("clicked()"), partial(self.start_move, "RIGHT"))
        self.connect(self.board_menu.ui.reset_button, SIGNAL("clicked()"), self.cheat)
        self.connect(self.board_menu.ui.roll_die_button, SIGNAL("clicked()"), self.get_dice_value)

        # Connect signals/slots for audio slider widgets on board menu
        self.connect(self.board_menu.ui.music_volume_slider, SIGNAL("sliderReleased()"), self.update_music_volume)
        self.connect(self.board_menu.ui.sound_effects_volume, SIGNAL("sliderReleased()"), self.update_sound_effect_volume)
        self.board_menu.ui.sound_effects_volume.setValue(50)
        self.board_menu.ui.music_volume_slider.setValue(50)

        # Die Setup/initialization
        self.initialize_dice()

        # Game sounds
        self.win_noise = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.lose_noise = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.win_noise.setMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/win_bing.m4a"))
        self.lose_noise.setMedia(QUrl.fromLocalFile(definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/lose_noise.m4a"))

        # Start the background music
        self.playlist_player.play()

        self.layout().addChildWidget(self.die)
        self.layout().addChildWidget(self.board_menu)

        self.player_list = self.set_round_order(self.player_list)
        self.current_player = self.player_list[0]
        self.current_player_list_index = 0
        self.current_player.is_current_player = True
        self.board_menu.ui.current_player_field.insertPlainText(str(self.current_player.name))
    # end initialize_game()

    def hide_dirs(self):
        self.board_menu.ui.down_button.setVisible(False)
        self.board_menu.ui.up_button.setVisible(False)
        self.board_menu.ui.left_button.setVisible(False)
        self.board_menu.ui.right_button.setVisible(False)
    #end hide_dirs

    def avail_dirs(self):
        """
        Determines possible directions the player could move based on current location
        Input: The player token who is currently moving
        Output: List of available directions
        """
        player_row = self.current_player.location[0]
        player_col = self.current_player.location[1]
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

    def update_dirs(self):
        """
        Hides the movement buttons based on whether or not its a valid move
        Input:
        Output:
        """
        player_row = self.current_player.location[0]
        player_col = self.current_player.location[1]
        self.board_menu.ui.down_button.setVisible(True)
        self.board_menu.ui.up_button.setVisible(True)
        self.board_menu.ui.left_button.setVisible(True)
        self.board_menu.ui.right_button.setVisible(True)

        if self.get_tile_type(player_row + 1, player_col) == "Invalid" \
                or self.current_player.direction_to_move == "UP":
            self.board_menu.ui.down_button.setVisible(False)
        if self.get_tile_type(player_row - 1, player_col) == "Invalid" \
                or self.current_player.direction_to_move == "DOWN":
            self.board_menu.ui.up_button.setVisible(False)
        if self.get_tile_type(player_row, player_col - 1) == "Invalid" \
                or self.current_player.direction_to_move == "RIGHT":
            self.board_menu.ui.left_button.setVisible(False)
        if self.get_tile_type(player_row, player_col + 1) == "Invalid" \
                or self.current_player.direction_to_move == "LEFT":
            self.board_menu.ui.right_button.setVisible(False)
    # end update_dirs()

    def set_default_game_volume(self):
        self.playlist_player.setVolume(50)
        self.board_menu.ui.music_volume_slider.setValue(50)
        self.board_menu.ui.music_volume_slider.setValue(50)
    # end set_default_game_volume

    def update_music_volume(self):
        tmp_volume = self.board_menu.ui.music_volume_slider.value()
        self.playlist_player.setVolume(tmp_volume)
    # end update_music_volume()

    def update_sound_effect_volume(self):
        tmp_volume = self.board_menu.ui.sound_effects_volume.value()

        # Set volume for lose/win effects
        self.win_noise.setVolume(tmp_volume)
        self.lose_noise.setVolume(tmp_volume)

        # Set the volume for each player token
        for player in self.player_list:
            player.audio_player.setVolume(tmp_volume)

        # Set the die volume
        self.die.audio_player.setVolume(tmp_volume)
    # end update_sound_effect_volume()

    def get_dice_value(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.current_player.moves_left = self.die.roll()
        self.current_player.direction_to_move = "NONE"
        self.board_menu.ui.dice_field.clear()
        self.board_menu.ui.dice_field.insertPlainText(str(self.current_player.moves_left))
        self.board_menu.ui.current_player_field.clear()
        self.board_menu.ui.current_player_field.insertPlainText(str(self.current_player.name))

        self.update_dirs()
        self.board_menu.ui.roll_die_button.setVisible(False)

        if self.current_player.moves_left == 6:
            self.current_player.moves_left = 0
            self.hide_dirs()
            self.board_menu.ui.roll_die_button.setVisible(True)
            answer, valid_input = QInputDialog().getItem(self, "Select Cake Headquarters", "Select:", self.question_categories, 0, False)

            if answer == self.question_categories[0]:
                self.current_player.location[0] = 4
                self.current_player.location[1] = 8
                self.current_player.x = self.board_tile_width * 9  - (self.current_player.width * self.current_player.x_offset)
                self.current_player.y = self.board_tile_height * 5 - (self.current_player.height * self.current_player.y_offset)

            elif answer == self.question_categories[1]:
                self.current_player.location[0] = 8
                self.current_player.location[1] = 4
                self.current_player.x = self.board_tile_width * 5  - (self.current_player.width * self.current_player.x_offset)
                self.current_player.y = self.board_tile_height * 9 - (self.current_player.height * self.current_player.y_offset)

            elif answer == self.question_categories[2]:
                self.current_player.location[0] = 0
                self.current_player.location[1] = 4
                self.current_player.x = self.board_tile_width * 5  - (self.current_player.width * self.current_player.x_offset)
                self.current_player.y = self.board_tile_height * 1 - (self.current_player.height * self.current_player.y_offset)

            elif answer == self.question_categories[3]:
                self.current_player.location[0] = 4
                self.current_player.location[1] = 0
                self.current_player.x = self.board_tile_width * 1  - (self.current_player.width * self.current_player.x_offset)
                self.current_player.y = self.board_tile_height * 5 - (self.current_player.height * self.current_player.y_offset)

            else:
                print("Incorrect answer")

            self.current_player.turn_status = True
            self.current_player.draw_token  = True
            self.current_player.update()
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
            # TODO: Could add a check to restart for those too impatient.
            self.current_player.audio_player.play()

            if (label == "UP" or label == "DOWN" or
                label == "LEFT" or label == "RIGHT"):

                while (self.current_player.moves_left > 0):
                    self.current_player.direction_to_move = label
                    self.current_player.turn_status = True

                    self.current_player.update_location(direction=label)
                    self.update_dirs()
                    self.current_player.moves_left = self.current_player.moves_left - 1
                    self.board_menu.ui.dice_field.clear()
                    self.board_menu.ui.dice_field.insertPlainText(str(self.current_player.moves_left))

                    if len(self.avail_dirs()) > 2 and self.current_player.moves_left != 0:
                        break
                    else:
                        if self.current_player.location == [0, 0]:
                            if self.current_player.direction_to_move == "UP":
                                label = "RIGHT"
                            else:
                                label = "DOWN"
                        elif self.current_player.location == [0, 8]:
                            if self.current_player.direction_to_move == "UP":
                                label = "LEFT"
                            else:
                                label = "DOWN"
                        elif self.current_player.location == [8, 0]:
                            if self.current_player.direction_to_move == "DOWN":
                                label = "RIGHT"
                            else:
                                label = "UP"
                        elif self.current_player.location == [8, 8]:
                            if self.current_player.direction_to_move == "DOWN":
                                label = "LEFT"
                            else:
                                label = "UP"

                    if self.current_player.moves_left == 0:
                        self.current_player.done_moving = True
                    # end if

                    # Manually calls the paint QEvent.
                    self.update()

                    # Once the player is out of spaces to move, prompt the player with a
                    # question from the QA Manager.
                    if self.current_player.moves_left == 0 and self.current_player.done_moving:
                        self.current_player.direction_to_move = "NONE"
                        self.hide_dirs()
                        self.board_menu.ui.roll_die_button.setVisible(True)
                        self.current_player.done_moving = False
                        self.perform_tile_action()
                    # end if

                else:
                    print("No moves left!")

        except ValueError:
            print("[ERROR] Invalid dice roll amount!")
    # end start_move()

    def initialize_player_tokens(self, total_players, player_one, player_two,
                                 player_three, player_four):
        """
         Description
        -------------
         TODO: JGC -

        """

        if total_players >= 1:
            self.player_widget = PlayerToken(player_one, self.board_tile_width, self.board_tile_height,
                                             2.6, 2.6)
            self.player_widget.resize(self.board_width, self.board_height)
            self.layout().addChildWidget(self.player_widget)
            self.player_list.append(self.player_widget)

        if total_players >= 2:
            player_widget_two = PlayerToken(player_two, self.board_tile_width, self.board_tile_height,
                                            1, 1)
            player_widget_two.resize(self.board_width, self.board_height)
            self.layout().addChildWidget(player_widget_two)
            self.player_list.append(player_widget_two)

        if total_players >= 3:
            player_widget_three = PlayerToken(player_three, self.board_tile_width, self.board_tile_height,
                                            2.6, 1)
            player_widget_three.resize(self.board_width, self.board_height)
            self.layout().addChildWidget(player_widget_three)
            self.player_list.append(player_widget_three)

        if total_players >= 4:
            player_widget_four = PlayerToken(player_four, self.board_tile_width, self.board_tile_height,
                                            1, 2.6)
            player_widget_four.resize(self.board_width, self.board_height)
            self.layout().addChildWidget(player_widget_four)
            self.player_list.append(player_widget_four)
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

    def cheat(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.current_player.award_cake_piece(self.question_categories[0])
        self.current_player.award_cake_piece(self.question_categories[1])
        self.current_player.award_cake_piece(self.question_categories[2])
        self.current_player.award_cake_piece(self.question_categories[3])
        self.current_player.update()
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
    # end is_roll_again_tile()

    def is_qtype1_tile(self, row, col):
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
    # end is_person_tile()

    def is_qtype2_tile(self, row, col):
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
    # end is_event_tile()

    def is_qtype3_tile(self, row, col):
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
    # end is_place_tile()

    def is_qtype4_tile(self, row, col):
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
    # end is_holiday_tile()

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
        elif self.is_qtype1_tile(row, col):
            return self.question_categories[0]
        elif self.is_qtype2_tile(row, col):
            return self.question_categories[1]
        elif self.is_qtype3_tile(row, col):
            return self.question_categories[2]
        elif self.is_qtype4_tile(row, col):
            return self.question_categories[3]
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

        for player in self.player_list:
            self.do_player_turn(player)
    # end paintEvent()

    def do_player_turn(self, player):
        """
         Description
        -------------
         TODO: JGC
        """

        if player.turn_status:
            player.draw_token = True
            player.update()
            player.turn_status = False
        # end if
    # end do_player_turn()

    def perform_tile_action(self):
        """
         Description
        -------------
         - TODO: JGC
        """
        self.current_player.update()
        tile_type = self.get_tile_type(self.current_player.location[0], self.current_player.location[1])

        roll_again = False

        if tile_type in self.question_categories:

            good_answer = self.ask_question(self.current_player, tile_type, isCake=False)

            if good_answer:
                self.win_noise.play()
                roll_again = True
                # Verify this is a "Cake" Tile before awarding cake piece.
                if self.is_cake_tile(self.current_player.location[0], self.current_player.location[1]):
                    self.current_player.award_cake_piece(cake_category=tile_type)
            else:
                self.lose_noise.play()

        elif (tile_type == "roll_again"):
            self.win_noise.play()
            roll_again = True
            QMessageBox.question(self, 'Congratulations!', 'Roll Again!', QMessageBox.Ok)

        elif (tile_type == "hub"):
            # Verify the player token has all cake pieces awarded before answering the
            # winning question, otherwise ask random question
            if self.current_player.all_cake_pieces_present():
                answer, valid_input = QInputDialog().getItem(
                    self, "Select Category", "!OTHER PLAYERS! Select the winning question category:",
                    self.question_categories, 0, False)
                good_answer = self.ask_question(self.current_player, answer, isCake=False)

                if good_answer:
                    self.win_noise.play()
                    QMessageBox.question(self, 'Congratulations!', 'YOU WIN!', QMessageBox.Ok)
                    self.restart_menu.show()
                else:
                    self.lose_noise.play()
            else:
                answer, valid_input = QInputDialog().getItem(
                    self, "Select Category", "Select the question category:",
                    self.question_categories, 0, False)
                good_answer = self.ask_question(self.current_player, answer, isCake=False)
                if good_answer:
                    roll_again = True
                else:
                    self.lose_noise.play()

        else:
            print("Invalid Tile/Question Type Received")
            print("Row: " + str(self.current_player.location[0]))
            print("Col: " + str(self.current_player.location[1]))

        # If not roll again tile, point to the next player in the list
        if not roll_again:
            # Deactivate the yellow outline for current player
            self.current_player.is_current_player = False
            self.current_player_list_index = (self.current_player_list_index + 1) % len(self.player_list)
            self.current_player = self.player_list[self.current_player_list_index]
            self.current_player.is_current_player = True
            self.board_menu.ui.current_player_field.clear()
            self.board_menu.ui.current_player_field.insertPlainText(str(self.current_player.name))
            self.board_menu.ui.dice_field.clear()
        # end if
    # end perform_tile_action

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
                    painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                      QImage(self.image_path + "roll_again.png"))

                elif self.is_qtype1_tile(row, col):
                    painter.setBrush(QBrush(self.qtype1_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                    if self.is_cake_tile(row, col):
                        painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                          QImage(self.image_path + "collect.png"))

                elif self.is_qtype4_tile(row, col):
                    painter.setBrush(QBrush(self.qtype4_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                    if self.is_cake_tile(row, col):
                        painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                          QImage(self.image_path + "collect.png"))

                elif self.is_qtype2_tile(row, col):
                    painter.setBrush(QBrush(self.qtype2_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                    if self.is_cake_tile(row, col):
                        painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                          QImage(self.image_path + "collect.png"))

                elif self.is_qtype3_tile(row, col):
                    painter.setBrush(QBrush(self.qtype3_tile_color, Qt.SolidPattern))
                    painter.drawRect(x, y, self.board_tile_width, self.board_tile_height)
                    if self.is_cake_tile(row, col):
                        painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                          QImage(self.image_path + "collect.png"))

                elif self.is_hub_tile(row, col):
                    painter.drawImage(QRect(x, y, self.board_tile_width, self.board_tile_height),
                                      QImage(self.image_path + "win.png"))

                # Quadrant One
                elif row == 1 and col == 1:
                    painter.drawImage(QRect(self.board_tile_width, self.board_tile_height, self.board_tile_width * 3, self.board_tile_height * 3),
                                      QImage(self.image_path + "american_flag.jpeg"))

                # Quadrant Two
                elif row == 5 and col == 1:
                    painter.drawImage(QRect(self.board_tile_width * row, self.board_tile_height, self.board_tile_width * 3, self.board_tile_height * 3),
                                      QImage(self.image_path + "fireworks-two.jpg"))

                # Quadrant Three
                elif row == 1 and col == 5:
                    painter.drawImage(QRect(self.board_tile_width , self.board_tile_height * col, self.board_tile_width * 3, self.board_tile_height * 3),
                                      QImage(self.image_path + "underwear_guy.jpeg"))

                # Quadrant Four
                elif row == 5 and col == 5:
                    painter.drawImage(QRect(self.board_tile_width * row, self.board_tile_height * col, self.board_tile_width * 3, self.board_tile_height * 3),
                                      QImage(self.image_path + "doi.jpg"))
                # end if

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