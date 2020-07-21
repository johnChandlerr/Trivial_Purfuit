# This Python file uses the following encoding: utf-8

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog)
from PySide2.QtCore import (SIGNAL)

from Trivial_Purfuit.src.board.the_board import Board
from Trivial_Purfuit.src.MainWindow.menus.ui_start_menu import Ui_StartMenuDialog
from Trivial_Purfuit.src.MainWindow.menus.setup_menu import SetupMenu
from Trivial_Purfuit.src.MainWindow.ui_mainwindow import Ui_MainWindow


class StartMenu(QDialog):
    """
     Description
    -------------
        TODO - Put this in it's own file.
    """
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = Ui_StartMenuDialog()
        self.ui.setupUi(self)
# end class StartMenu


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

        self.board = Board()
        self.start_menu = StartMenu()
        self.setup_menu = SetupMenu()

        self.connect(self.start_menu.ui.new_game_button, SIGNAL("clicked()"), self.setup_game)
        self.connect(self.start_menu.ui.cancel_button, SIGNAL("clicked()"), self.close_game)
        self.connect(self.setup_menu.ui.start_game_button, SIGNAL("clicked()"), self.start_game)
        self.connect(self.setup_menu.ui.exit_game_button, SIGNAL("clicked()"), self.close_game)

        self.start_menu.show()
    # end __init__()

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
        self.setup_menu.hide()
        self.board.show()
    # end setup_game()

    def close_game(self):
        """
         Description
        -------------
         - Terminate the Trivial Purfuit application
        """
        QApplication.quit()
    # end close_game()
# end class MainWindow

if __name__ == "__main__":
    try:
        app = QApplication([])
        mainWindow = MainWindow()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
