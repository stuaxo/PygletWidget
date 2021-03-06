PygletWidget
=============

A widget to easily display **one** pyglet scene in a PySide/Qt application.

This has been tested on Ubuntu 12.04-17.04, Windows XP and Windows 7.

License
---------
There is no license as this is more a reminder than anything else.

You are free to use this file without any restrictions. 

Requirements
-----------------

- Python 2.7
- PySide or PyQT4


Usage
--------
Here is an example for PySide from the examples/ folder:

```python
import pyglet
import sys

from PySide import QtCore, QtGui, QtOpenGL
from pygletwidget.pyside import QPygletWidget

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
```

You can run the script by issuing the following command::

```bash
  python examples/example_pyside.py
```

Contributors
------------

Colin Duquesnoy, Stuart Axon
