import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog)
from PySide2.QtCore import (SIGNAL)

from Trivial_Purfuit.src.MainWindow.menus.ui_setup_menu import Ui_Dialog

class SetupMenu(QDialog):
    """
     Description
    -------------
        TODO - Put this in it's own file.
    """
    def __init__(self):
        super(SetupMenu, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
# end class StartMenu
