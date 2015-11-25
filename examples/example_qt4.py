import pyglet
import sys

from PyQt4 import QtCore, QtGui, QtOpenGL
from pygletwidget.qt4 import QPygletWidget

class MyPygletWidget(QPygletWidget):
    def on_init(self):
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image("logo.png"))
        self.label = pyglet.text.Label(
            text="This is a pyglet label rendered in a Qt widget :)")
        self.setMinimumSize(QtCore.QSize(640, 480))

    def on_draw(self):
        self.sprite.draw()
        self.label.draw()


def main():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    widget = MyPygletWidget()
    window.setCentralWidget(widget)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
