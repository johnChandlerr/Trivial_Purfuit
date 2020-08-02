# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import (QApplication, QWidget)
from Trivial_Purfuit.src.board.menus.ui_player_navigation_menu import Ui_PlayerNavigationMenu


class PlayerNavigationMenu(QWidget):
    """
     Description
    -------------
        TODO - JGC
    """
    def __init__(self):
        super(PlayerNavigationMenu, self).__init__()
        monitor = QApplication.desktop().geometry()
        self.resize(monitor.width(), monitor.height())

        self.ui = Ui_PlayerNavigationMenu()
        self.ui.setupUi(self)
# end class PlayerNavigationMenu


if __name__ == "__main__":
    try:
        app = QApplication([])
        menu = PlayerNavigationMenu()
        menu.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
