import sys, random, definitions
from PySide2.QtWidgets import (QApplication, QWidget)
from PySide2.QtGui import (QPainter, QImage)
from PySide2.QtCore import (QRect, QUrl)
from PySide2.QtMultimedia import (QMediaPlayer)

class Die(QWidget):
    def __init__(self):

        super().__init__()

        self.width = 75
        self.height = self.width
        self.x = 0
        self.y = 0

        self.board_tile_width  = 0
        self.board_tile_height = self.board_tile_width

        self.sides = 6

        self.dice_initialized = False
        self.draw_dice = False

        self.dice_amount = 0
        self.audio_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.audio_player.setMedia(QUrl.fromLocalFile( definitions.ROOT_DIR + "/Trivial_Purfuit/resources/audio/dice_roll.m4a"))
        self.audio_player.setVolume(50)
        self.image_path = definitions.ROOT_DIR + "/Trivial_Purfuit/src/die/"

    def roll(self):
        self.audio_player.play()
        self.dice_amount = 1 + random.randrange(self.sides)
        return self.dice_amount

    def paintEvent(self, event):
        self.draw_dice_fun()
    # end paintEvent()

    def draw_dice_fun(self):
        painter = QPainter(self)

        self.x = self.board_tile_width * 6
        self.y = self.board_tile_height * 2

        # initial dice
        painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                          QImage(self.image_path + "dice-six-faces-six.png"))

        if not self.dice_initialized:
            self.x = self.board_tile_width * 5 - self.width
            self.y = self.board_tile_height * 5 - self.height
            self.dice_initialized = True
        
        elif self.dice_amount == 1:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-one.png"))
        elif self.dice_amount == 2:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-two.png"))
        elif self.dice_amount == 3:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-three.png"))
        elif self.dice_amount == 4:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-four.png"))
        elif self.dice_amount == 5:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-five.png"))
        elif self.dice_amount == 6:
            painter.drawImage(QRect(self.x, self.y, self.width, self.height),
                              QImage(self.image_path + "dice-six-faces-six.png"))
        # end if
        self.draw_dice = False


if __name__ == "__main__":
    try:
        app = QApplication([])
        die = Die()
        die.show()
        sys.exit(app.exec_())

    except Exception as e:
        print(e)
