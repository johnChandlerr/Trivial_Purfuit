# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restart_menu.ui'
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


class Ui_RestartMenuDialog(object):
    def setupUi(self, RestartMenuDialog):
        if not RestartMenuDialog.objectName():
            RestartMenuDialog.setObjectName(u"RestartMenuDialog")
        RestartMenuDialog.resize(221, 154)
        self.layoutWidget = QWidget(RestartMenuDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 40, 91, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.play_again_button = QPushButton(self.layoutWidget)
        self.play_again_button.setObjectName(u"play_again_button")

        self.verticalLayout.addWidget(self.play_again_button)

        self.leave_game_button = QPushButton(self.layoutWidget)
        self.leave_game_button.setObjectName(u"leave_game_button")

        self.verticalLayout.addWidget(self.leave_game_button)


        self.retranslateUi(RestartMenuDialog)
        self.leave_game_button.clicked.connect(RestartMenuDialog.close)

        QMetaObject.connectSlotsByName(RestartMenuDialog)
    # setupUi

    def retranslateUi(self, RestartMenuDialog):
        RestartMenuDialog.setWindowTitle(QCoreApplication.translate("RestartMenuDialog", u"Trivial Purfuit Menu", None))
        self.play_again_button.setText(QCoreApplication.translate("RestartMenuDialog", u"Play Again?", None))
        self.leave_game_button.setText(QCoreApplication.translate("RestartMenuDialog", u"Leave Game", None))
    # retranslateUi

