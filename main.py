import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from random import randrange
from UI import Ui_Form


class RandomCircle(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        d = randrange(10, 1000)
        colors = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        qp.setBrush(QColor(*colors))
        qp.drawEllipse(randrange(0, 1600), randrange(0, 900), d, d)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircle()
    ex.show()
    sys.exit(app.exec_())
