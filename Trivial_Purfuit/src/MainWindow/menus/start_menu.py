# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import (QDialog)
from Trivial_Purfuit.src.MainWindow.menus.ui_start_menu import Ui_StartMenuDialog


class StartMenu(QDialog):
    """
     Description
    -------------
        TODO - JGC
    """
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = Ui_StartMenuDialog()
        self.ui.setupUi(self)
# end class StartMenu