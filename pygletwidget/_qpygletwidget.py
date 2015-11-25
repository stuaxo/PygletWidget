"""
Shared implementation for PySide and QT4.

pygletwidget.qt4 and pygletwidget.pyside set pygletwidget.QT_FLAVOUR to "PYSIDE" or "QT4"
"""
import pyglet
import pygletwidget
pyglet.options['shadow_window'] = False
pyglet.options['debug_gl'] = False

from pyglet import gl

if pygletwidget.QT_FLAVOUR=="PYSIDE":
    from PySide import QtCore, QtGui, QtOpenGL
elif pygletwidget.QT_FLAVOUR=="QT4":
    from PyQt4 import QtCore, QtGui, QtOpenGL
else:
    raise ValueError('pygletwidget.QT_FLAVOUR not set, import pygletwidget.qt4 or pygletwidget.pyside')



class QPygletWidget(QtOpenGL.QGLWidget):
    """
    A simple pyglet widget.

    User can subclass this widget and implement the following methods:
        - on_init: called when open gl has been initialised
        - on_update: called every dt.
        - on_draw: called when paintGL is executed
        - on_resize: called when resizeGL is executed
    """
    def __init__(self, parent=None,
                 clear_color=(0.0, 0.0, 0.0, 1.0),
                 frame_time=32,
                 dt=16):
        """
        :param clear_color: The widget clear color
        :type clear_color: tuple(r, g, b, a)

        :param frame_time: The desired frame time [ms]
        :type: frame_time: int

        :param dt: The desired update rate [ms]
        :type: dt: int
        """
        QtOpenGL.QGLWidget.__init__(self, parent)

        # init members
        self._clear_color = clear_color
        self._dt = dt
        self.update_timer = QtCore.QTimer()
        self.draw_timer = QtCore.QTimer()

        # configure draw and update timers
        self.update_timer.setInterval(dt)
        self.update_timer.timeout.connect(self._update)
        self.draw_timer.setInterval(frame_time)
        self.draw_timer.timeout.connect(self.updateGL)

        # start timers
        self.update_timer.start()
        self.draw_timer.start()

    def _update(self):
        """
        Calls on_update with the choosen dt
        """
        self.on_update(self._dt)

    def on_init(self):
        """
        Lets the user initialise himself
        """
        pass

    def on_draw(self):
        """
        Lets the user draw his scene
        """
        pass

    def on_update(self, dt):
        """
        Lets the user draw his scene
        """
        pass

    def on_resize(self, w, h):
        """
        Lets the user handle the widget resize event. By default, this method
        resizes the view to the widget size.
        """
        gl.glViewport(0, 0, w, h)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, w, 0, h, -1, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def initializeGL(self):
        """
        Initialises open gl:
            - create a mock context to fool pyglet
            - setup various opengl rule (only the clear color atm)
        """
        gl.current_context = pygletwidget.Context()
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        self.on_init()

    def resizeGL(self, w, h):
        """
        Resizes the gl camera to match the widget size.
        """
        self.on_resize(w, h)

    def paintGL(self):
        """
        Clears the back buffer than calls the on_draw method
        """
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        self.on_draw()

