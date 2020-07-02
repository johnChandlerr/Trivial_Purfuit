# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_menu.ui'
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


class Ui_StartMenuDialog(object):
    def setupUi(self, StartMenuDialog):
        if not StartMenuDialog.objectName():
            StartMenuDialog.setObjectName(u"StartMenuDialog")
        StartMenuDialog.resize(266, 154)
        self.layoutWidget = QWidget(StartMenuDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 40, 91, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_game_button = QPushButton(self.layoutWidget)
        self.new_game_button.setObjectName(u"new_game_button")

        self.verticalLayout.addWidget(self.new_game_button)

        self.cancel_button = QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.verticalLayout.addWidget(self.cancel_button)


        self.retranslateUi(StartMenuDialog)
        self.cancel_button.clicked.connect(StartMenuDialog.close)

        QMetaObject.connectSlotsByName(StartMenuDialog)
    # setupUi

    def retranslateUi(self, StartMenuDialog):
        StartMenuDialog.setWindowTitle(QCoreApplication.translate("StartMenuDialog", u"Trivial Purfuit Menu", None))
        self.new_game_button.setText(QCoreApplication.translate("StartMenuDialog", u"New Game", None))
        self.cancel_button.setText(QCoreApplication.translate("StartMenuDialog", u"Cancel", None))
    # retranslateUi

