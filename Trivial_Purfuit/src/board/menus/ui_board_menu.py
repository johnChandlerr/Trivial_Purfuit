# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'board_menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_BoardMenu(object):
    def setupUi(self, BoardMenu):
        if not BoardMenu.objectName():
            BoardMenu.setObjectName(u"BoardMenu")
        BoardMenu.resize(500, 317)
        self.navigation_group = QGroupBox(BoardMenu)
        self.navigation_group.setObjectName(u"navigation_group")
        self.navigation_group.setGeometry(QRect(60, 10, 311, 101))
        self.up_button = QPushButton(self.navigation_group)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(100, 30, 101, 24))
        self.down_button = QPushButton(self.navigation_group)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(100, 60, 101, 24))
        self.left_button = QPushButton(self.navigation_group)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setGeometry(QRect(10, 40, 89, 24))
        self.right_button = QPushButton(self.navigation_group)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setGeometry(QRect(200, 40, 101, 24))
        self.misc_group = QGroupBox(BoardMenu)
        self.misc_group.setObjectName(u"misc_group")
        self.misc_group.setGeometry(QRect(60, 150, 311, 101))
        self.reset_button = QPushButton(self.misc_group)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(170, 70, 91, 24))
        self.dice_field = QPlainTextEdit(self.misc_group)
        self.dice_field.setObjectName(u"dice_field")
        self.dice_field.setGeometry(QRect(160, 30, 104, 31))
        self.dice_label = QLabel(self.misc_group)
        self.dice_label.setObjectName(u"dice_label")
        self.dice_label.setGeometry(QRect(40, 35, 91, 21))
        self.roll_die_button = QPushButton(self.misc_group)
        self.roll_die_button.setObjectName(u"roll_die_button")
        self.roll_die_button.setGeometry(QRect(40, 70, 80, 24))

        self.retranslateUi(BoardMenu)

        QMetaObject.connectSlotsByName(BoardMenu)
    # setupUi

    def retranslateUi(self, BoardMenu):
        BoardMenu.setWindowTitle(QCoreApplication.translate("BoardMenu", u"Form", None))
        self.navigation_group.setTitle(QCoreApplication.translate("BoardMenu", u"Player Navigation", None))
        self.up_button.setText(QCoreApplication.translate("BoardMenu", u"Move Up", None))
        self.down_button.setText(QCoreApplication.translate("BoardMenu", u"Move Down", None))
        self.left_button.setText(QCoreApplication.translate("BoardMenu", u"Move Left", None))
        self.right_button.setText(QCoreApplication.translate("BoardMenu", u"Move Right", None))
        self.misc_group.setTitle(QCoreApplication.translate("BoardMenu", u"Misc.", None))
        self.reset_button.setText(QCoreApplication.translate("BoardMenu", u"Reset ", None))
        self.dice_label.setText(QCoreApplication.translate("BoardMenu", u"Dice Amount", None))
        self.roll_die_button.setText(QCoreApplication.translate("BoardMenu", u"Roll Die", None))
    # retranslateUi

