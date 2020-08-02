import random
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QVBoxLayout)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush, QImage)
from PySide2.QtCore import (Qt, QRect)


class Die(QWidget):
    def __init__(self):

        super().__init__()

        self.width = 100
        self.height = self.width
        self.x = 0
        self.y = 0

        self.board_tile_width  = 0
        self.board_tile_height = self.board_tile_width

        self.sides = 6

        self.dice_initialized = False
        self.draw_dice = False

        self.dice_amount = 0

    def roll(self):
        self.dice_amount = 1 + random.randrange(self.sides)
        return self.dice_amount

    def paintEvent(self, event):
        self.draw_dice_fun()
    # end paintEvent()

    def draw_dice_fun(self):
        painter = QPainter(self)
        self.x = self.board_tile_width * 5 - self.width
        self.y = self.board_tile_height * 5 - self.height
        # initial dice
        painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                          QImage("./dice-six-faces-six.png"))

        if not self.dice_initialized:
            self.x = self.board_tile_width * 5 - self.width
            self.y = self.board_tile_height * 5 - self.height
            self.dice_initialized = True

        print("Dice: ", self.dice_amount)
        if self.dice_amount == 1:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-one.png"))
        elif self.dice_amount == 2:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-two.png"))
        elif self.dice_amount == 3:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-three.png"))
        elif self.dice_amount == 4:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-four.png"))
        elif self.dice_amount == 5:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-five.png"))
        elif self.dice_amount == 6:
            painter.drawImage(QRect(self.x + 150, self.y - 150, self.width, self.height),
                              QImage("./dice-six-faces-six.png"))
        self.draw_dice = False
