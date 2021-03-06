# This Python file uses the following encoding: utf-8

import sys
import definitions
from threading import Thread

from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCore import (SIGNAL, QUrl)
from PySide2.QtMultimedia import (QMediaPlayer)

from Trivial_Purfuit.src.board.the_board import Board
from Trivial_Purfuit.src.MainWindow.menus.start_menu import StartMenu
from Trivial_Purfuit.src.MainWindow.menus.setup_menu import SetupMenu
from Trivial_Purfuit.src.MainWindow.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """
     Description
    -------------
        The central window that is responsible for the user-interface for the Trivial Purfuit application
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.number_players = 0
        self.board = Board()
        self.start_menu = StartMenu()
        self.setup_menu = SetupMenu()
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.connect(self.start_menu.ui.new_game_button, SIGNAL("clicked()"), self.setup_game)
        self.connect(self.start_menu.ui.cancel_button, SIGNAL("clicked()"), self.close_game)
        self.connect(self.setup_menu.ui.start_game_button, SIGNAL("clicked()"), self.start_game)
        self.connect(self.setup_menu.ui.exit_game_button, SIGNAL("clicked()"), self.close_game)
        self.connect(self.board.restart_menu.ui.leave_game_button, SIGNAL("clicked()"), self.close_game)
        self.connect(self.board.restart_menu.ui.play_again_button, SIGNAL("clicked()"), self.restart_game)
        self.start_menu.show()
        #self.music_thread = Thread(target=self.play_background_music)
        #self.music_thread.start()
    # end __init__()

    def play_background_music(self):
        self.media_player.setMedia(QUrl.fromLocalFile( definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/bensound-anewbeginning.mp3"))
        self.media_player.setVolume(5)
        self.media_player.play()

        while True:
            print("State: ", self.media_player.state())
    # end play_background_music

    def setup_game(self):
        """
         Description
        -------------
         - Function to configure/setup a new game
        """
        self.start_menu.hide()
        self.setup_menu.show()
    # end setup_game()

    def start_game(self):
        """
         Description
        -------------
         - Function to start the game
        """
        try:
            self.number_players = int(self.setup_menu.ui.players_text_edit.toPlainText())

            pone_name   = self.setup_menu.ui.playerOneNameTextEdit.toPlainText()
            ptwo_name   = self.setup_menu.ui.playerTwoNameTextEdit.toPlainText()
            pthree_name = self.setup_menu.ui.playerThreeNameTextEdit.toPlainText()
            pfour_name  = self.setup_menu.ui.playerFourNameTextEdit.toPlainText()

            self.board.initialize_player_tokens(self.number_players,
                                                pone_name,
                                                ptwo_name,
                                                pthree_name,
                                                pfour_name)
            self.setup_menu.hide()
            self.board.initialize_game()
            self.board.show()
            self.board.hide_dirs()

            # TODO: JGC
            self.board.board_menu.ui.player_order_group_box.hide()

        except ValueError:
            print("[ERROR] Invalid input! Must be (1, 2, 3, or 4)!")
    # end start_game()

    def close_game(self):
        """
         Description
        -------------
         - Terminate the Trivial Purfuit application
        """
        #self.music_thread.join()
        QApplication.quit()
    # end close_game()

    def restart_game(self):
        self.board = Board()
        self.connect(self.board.restart_menu.ui.leave_game_button, SIGNAL("clicked()"), self.close_game)
        self.connect(self.board.restart_menu.ui.play_again_button, SIGNAL("clicked()"), self.restart_game)
        self.setup_menu.show()
    # end restart_game
# end class MainWindow


if __name__ == "__main__":
    try:
        app = QApplication([])
        mainWindow = MainWindow()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
