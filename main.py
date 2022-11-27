import random
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.pushed)
        self.coords = [0, 0]
        self.flag = False

    def draw(self):
        if self.flag:
            size1 = random.randint(30, 300)
            self.coords = [random.randint(size1, 800 - size1), random.randint(size1, 600 - size1)]
            self.qp.drawEllipse(*self.coords, size1, size1)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.setBrush(QColor(255, 255, 0))
        self.draw()
        self.qp.end()

    def pushed(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())