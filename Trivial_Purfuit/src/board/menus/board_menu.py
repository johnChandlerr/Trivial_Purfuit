# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import (QApplication, QWidget)
from Trivial_Purfuit.src.board.menus.ui_board_menu import Ui_BoardMenu


class BoardMenu(QWidget):
    """
     Description
    -------------
        TODO - JGC
    """
    def __init__(self):
        super(BoardMenu, self).__init__()
        monitor = QApplication.desktop().geometry()
        self.resize(monitor.width(), monitor.height())

        self.ui = Ui_BoardMenu()
        self.ui.setupUi(self)
# end class PlayerNavigationMenu


if __name__ == "__main__":
    try:
        app = QApplication([])
        menu = BoardMenu()
        menu.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
