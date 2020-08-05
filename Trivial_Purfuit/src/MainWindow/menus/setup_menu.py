# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import (QDialog)
from Trivial_Purfuit.src.MainWindow.menus.ui_setup_menu import Ui_SetupMenuDialog


class SetupMenu(QDialog):
    """
     Description
    -------------
        TODO - JGC
    """
    def __init__(self):
        super(SetupMenu, self).__init__()
        self.ui = Ui_SetupMenuDialog()
        self.ui.setupUi(self)
# end class StartMenu
