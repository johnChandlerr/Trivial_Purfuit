# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player_navigation_menu.ui'
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


class Ui_PlayerNavigationMenu(object):
    def setupUi(self, PlayerNavigationMenu):
        if not PlayerNavigationMenu.objectName():
            PlayerNavigationMenu.setObjectName(u"PlayerNavigationMenu")
        PlayerNavigationMenu.resize(500, 317)
        self.navigation_group = QGroupBox(PlayerNavigationMenu)
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
        self.misc_group = QGroupBox(PlayerNavigationMenu)
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

        self.retranslateUi(PlayerNavigationMenu)

        QMetaObject.connectSlotsByName(PlayerNavigationMenu)
    # setupUi

    def retranslateUi(self, PlayerNavigationMenu):
        PlayerNavigationMenu.setWindowTitle(QCoreApplication.translate("PlayerNavigationMenu", u"Form", None))
        self.navigation_group.setTitle(QCoreApplication.translate("PlayerNavigationMenu", u"Player Navigation", None))
        self.up_button.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Move Up", None))
        self.down_button.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Move Down", None))
        self.left_button.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Move Left", None))
        self.right_button.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Move Right", None))
        self.misc_group.setTitle(QCoreApplication.translate("PlayerNavigationMenu", u"Misc.", None))
        self.reset_button.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Reset ", None))
        self.dice_label.setText(QCoreApplication.translate("PlayerNavigationMenu", u"Dice Amount", None))
    # retranslateUi

