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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(318, 166)
        self.players_text_edit = QTextEdit(Dialog)
        self.players_text_edit.setObjectName(u"players_text_edit")
        self.players_text_edit.setGeometry(QRect(0, 0, 201, 31))
        self.default_text_edit = QTextEdit(Dialog)
        self.default_text_edit.setObjectName(u"default_text_edit")
        self.default_text_edit.setGeometry(QRect(0, 40, 141, 31))
        self.default_two_text_edit = QTextEdit(Dialog)
        self.default_two_text_edit.setObjectName(u"default_two_text_edit")
        self.default_two_text_edit.setGeometry(QRect(0, 80, 141, 31))
        self.start_game_button = QPushButton(Dialog)
        self.start_game_button.setObjectName(u"start_game_button")
        self.start_game_button.setGeometry(QRect(220, 0, 91, 24))
        self.exit_game_button = QPushButton(Dialog)
        self.exit_game_button.setObjectName(u"exit_game_button")
        self.exit_game_button.setGeometry(QRect(220, 30, 91, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.players_text_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Enter Number of Players [1-4]</span></p></body></html>", None))
        self.default_text_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Default Placeholder</span></p></body></html>", None))
        self.default_two_text_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">Default Placeholder</span></p></body></html>", None))
        self.start_game_button.setText(QCoreApplication.translate("Dialog", u"Start Game", None))
        self.exit_game_button.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

