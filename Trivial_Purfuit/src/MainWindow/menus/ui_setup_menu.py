# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_menu.ui'
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


class Ui_SetupMenuDialog(object):
    def setupUi(self, SetupMenuDialog):
        if not SetupMenuDialog.objectName():
            SetupMenuDialog.setObjectName(u"SetupMenuDialog")
        SetupMenuDialog.resize(318, 166)
        self.players_text_edit = QTextEdit(SetupMenuDialog)
        self.players_text_edit.setObjectName(u"players_text_edit")
        self.players_text_edit.setGeometry(QRect(10, 10, 201, 31))
        self.playerFourNameTextEdit = QTextEdit(SetupMenuDialog)
        self.playerFourNameTextEdit.setObjectName(u"playerFourNameTextEdit")
        self.playerFourNameTextEdit.setGeometry(QRect(170, 110, 141, 31))
        self.playerOneNameTextEdit = QTextEdit(SetupMenuDialog)
        self.playerOneNameTextEdit.setObjectName(u"playerOneNameTextEdit")
        self.playerOneNameTextEdit.setGeometry(QRect(20, 70, 141, 31))
        self.start_game_button = QPushButton(SetupMenuDialog)
        self.start_game_button.setObjectName(u"start_game_button")
        self.start_game_button.setGeometry(QRect(220, 0, 91, 24))
        self.exit_game_button = QPushButton(SetupMenuDialog)
        self.exit_game_button.setObjectName(u"exit_game_button")
        self.exit_game_button.setGeometry(QRect(220, 30, 91, 24))
        self.playerTwoNameTextEdit = QTextEdit(SetupMenuDialog)
        self.playerTwoNameTextEdit.setObjectName(u"playerTwoNameTextEdit")
        self.playerTwoNameTextEdit.setGeometry(QRect(170, 70, 141, 31))
        self.playerThreeNameTextEdit = QTextEdit(SetupMenuDialog)
        self.playerThreeNameTextEdit.setObjectName(u"playerThreeNameTextEdit")
        self.playerThreeNameTextEdit.setGeometry(QRect(20, 110, 141, 31))

        self.retranslateUi(SetupMenuDialog)

        QMetaObject.connectSlotsByName(SetupMenuDialog)
    # setupUi

    def retranslateUi(self, SetupMenuDialog):
        SetupMenuDialog.setWindowTitle(QCoreApplication.translate("SetupMenuDialog", u"Dialog", None))
        self.players_text_edit.setHtml(QCoreApplication.translate("SetupMenuDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Enter Number of Players [1-4]</span></p></body></html>", None))
        self.playerFourNameTextEdit.setHtml(QCoreApplication.translate("SetupMenuDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Player Four Name</span></p></body></html>", None))
        self.playerOneNameTextEdit.setHtml(QCoreApplication.translate("SetupMenuDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Player One Name</span></p></body></html>", None))
        self.start_game_button.setText(QCoreApplication.translate("SetupMenuDialog", u"Start Game", None))
        self.exit_game_button.setText(QCoreApplication.translate("SetupMenuDialog", u"Exit", None))
        self.playerTwoNameTextEdit.setHtml(QCoreApplication.translate("SetupMenuDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Player Two Name</span></p></body></html>", None))
        self.playerThreeNameTextEdit.setHtml(QCoreApplication.translate("SetupMenuDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Player Three Name</span></p></body></html>", None))
    # retranslateUi

