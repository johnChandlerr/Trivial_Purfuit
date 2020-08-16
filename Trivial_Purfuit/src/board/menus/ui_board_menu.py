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
        BoardMenu.resize(714, 625)
        self.navigation_group = QGroupBox(BoardMenu)
        self.navigation_group.setObjectName(u"navigation_group")
        self.navigation_group.setGeometry(QRect(40, 280, 311, 101))
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
        self.misc_group.setGeometry(QRect(40, 420, 311, 171))
        self.reset_button = QPushButton(self.misc_group)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(200, 120, 91, 24))
        self.dice_field = QPlainTextEdit(self.misc_group)
        self.dice_field.setObjectName(u"dice_field")
        self.dice_field.setGeometry(QRect(190, 30, 104, 31))
        self.dice_label = QLabel(self.misc_group)
        self.dice_label.setObjectName(u"dice_label")
        self.dice_label.setGeometry(QRect(20, 35, 161, 21))
        self.roll_die_button = QPushButton(self.misc_group)
        self.roll_die_button.setObjectName(u"roll_die_button")
        self.roll_die_button.setGeometry(QRect(40, 120, 80, 24))
        self.dice_label_2 = QLabel(self.misc_group)
        self.dice_label_2.setObjectName(u"dice_label_2")
        self.dice_label_2.setGeometry(QRect(20, 80, 161, 21))
        self.current_player_field = QPlainTextEdit(self.misc_group)
        self.current_player_field.setObjectName(u"current_player_field")
        self.current_player_field.setGeometry(QRect(190, 70, 104, 31))
        self.player_order_group_box = QGroupBox(BoardMenu)
        self.player_order_group_box.setObjectName(u"player_order_group_box")
        self.player_order_group_box.setGeometry(QRect(40, 10, 301, 211))
        self.player_one_label = QLabel(self.player_order_group_box)
        self.player_one_label.setObjectName(u"player_one_label")
        self.player_one_label.setGeometry(QRect(10, 40, 121, 21))
        self.player_one_pos = QPlainTextEdit(self.player_order_group_box)
        self.player_one_pos.setObjectName(u"player_one_pos")
        self.player_one_pos.setGeometry(QRect(170, 40, 104, 31))
        self.player_two_label = QLabel(self.player_order_group_box)
        self.player_two_label.setObjectName(u"player_two_label")
        self.player_two_label.setGeometry(QRect(10, 80, 121, 21))
        self.player_two_pos = QPlainTextEdit(self.player_order_group_box)
        self.player_two_pos.setObjectName(u"player_two_pos")
        self.player_two_pos.setGeometry(QRect(170, 80, 104, 31))
        self.player_three_pos = QPlainTextEdit(self.player_order_group_box)
        self.player_three_pos.setObjectName(u"player_three_pos")
        self.player_three_pos.setGeometry(QRect(170, 120, 104, 31))
        self.player_four_pos = QPlainTextEdit(self.player_order_group_box)
        self.player_four_pos.setObjectName(u"player_four_pos")
        self.player_four_pos.setGeometry(QRect(170, 160, 104, 31))
        self.player_three_label = QLabel(self.player_order_group_box)
        self.player_three_label.setObjectName(u"player_three_label")
        self.player_three_label.setGeometry(QRect(10, 120, 121, 21))
        self.player_four_label = QLabel(self.player_order_group_box)
        self.player_four_label.setObjectName(u"player_four_label")
        self.player_four_label.setGeometry(QRect(10, 160, 121, 21))
        self.audio_group = QGroupBox(BoardMenu)
        self.audio_group.setObjectName(u"audio_group")
        self.audio_group.setGeometry(QRect(380, 350, 311, 151))
        self.music_volume_slider = QSlider(self.audio_group)
        self.music_volume_slider.setObjectName(u"music_volume_slider")
        self.music_volume_slider.setGeometry(QRect(120, 50, 160, 16))
        self.music_volume_slider.setOrientation(Qt.Horizontal)
        self.music_label = QLabel(self.audio_group)
        self.music_label.setObjectName(u"music_label")
        self.music_label.setGeometry(QRect(20, 50, 91, 21))
        self.sound_label = QLabel(self.audio_group)
        self.sound_label.setObjectName(u"sound_label")
        self.sound_label.setGeometry(QRect(20, 90, 91, 21))
        self.sound_effects_volume = QSlider(self.audio_group)
        self.sound_effects_volume.setObjectName(u"sound_effects_volume")
        self.sound_effects_volume.setGeometry(QRect(120, 90, 160, 16))
        self.sound_effects_volume.setOrientation(Qt.Horizontal)

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
        self.misc_group.setTitle(QCoreApplication.translate("BoardMenu", u"Current Player Information", None))
        self.reset_button.setText(QCoreApplication.translate("BoardMenu", u"Cheat", None))
        self.dice_label.setText(QCoreApplication.translate("BoardMenu", u"Moves Left for Player", None))
        self.roll_die_button.setText(QCoreApplication.translate("BoardMenu", u"Roll Die", None))
        self.dice_label_2.setText(QCoreApplication.translate("BoardMenu", u"Current Player", None))
        self.player_order_group_box.setTitle(QCoreApplication.translate("BoardMenu", u"Player Order", None))
        self.player_one_label.setText(QCoreApplication.translate("BoardMenu", u"Player One", None))
        self.player_two_label.setText(QCoreApplication.translate("BoardMenu", u"Player Two", None))
        self.player_three_label.setText(QCoreApplication.translate("BoardMenu", u"Player Three", None))
        self.player_four_label.setText(QCoreApplication.translate("BoardMenu", u"Player Four", None))
        self.audio_group.setTitle(QCoreApplication.translate("BoardMenu", u"Audio Settings", None))
        self.music_label.setText(QCoreApplication.translate("BoardMenu", u"Music", None))
        self.sound_label.setText(QCoreApplication.translate("BoardMenu", u"Sound Effects", None))
    # retranslateUi

