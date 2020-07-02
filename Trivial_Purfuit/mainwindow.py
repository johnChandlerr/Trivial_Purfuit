# This Python file uses the following encoding: utf-8

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog)

from ui_start_menu import Ui_StartMenuDialog
from ui_mainwindow import Ui_MainWindow


class StartMenu(QDialog):
    """
     Description
    -------------
        TODO
    """
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = Ui_StartMenuDialog()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    """
     Description
    -------------
        TODO
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    try:
        app = QApplication([])
        #board = MainWindow()
        #board.show()

        start_menu = StartMenu()
        start_menu.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
