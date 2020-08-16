# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import (QDialog)
from Trivial_Purfuit.src.board.menus.ui_restart_menu import Ui_RestartMenuDialog


class RestartMenu(QDialog):
    """
     Description
    -------------
        TODO - JGC
    """
    def __init__(self):
        super(RestartMenu, self).__init__()
        self.ui = Ui_RestartMenuDialog()
        self.ui.setupUi(self)
# end class RestartMenu