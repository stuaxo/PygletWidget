import sys
import pyglet
pyglet.options['shadow_window'] = False
pyglet.options['debug_gl'] = False

from pyglet import gl

QT_FLAVOUR=None

class ObjectSpace(object):
    """ Object space mocker """
    def __init__(self):
        # Textures and buffers scheduled for deletion the next time this
        # object space is active.
        self._doomed_textures = []
        self._doomed_buffers = []


class Context(object):
    """
    pyglet.gl.Context mocker. This is used to make pyglet believe that a valid
    context has already been setup. (Qt takes care of creating the open gl
    context)

    _Most of the methods are empty, there is just the minimum required to make
    it look like a duck..._
    """
    # define the same class attribute as pyglet.gl.Context
    CONTEXT_SHARE_NONE = None
    CONTEXT_SHARE_EXISTING = 1
    _gl_begin = False
    _info = None
    _workaround_checks = [
        ('_workaround_unpack_row_length',
         lambda info: info.get_renderer() == 'GDI Generic'),
        ('_workaround_vbo',
         lambda info: info.get_renderer().startswith('ATI Radeon X')),
        ('_workaround_vbo_finish',
         lambda info: ('ATI' in info.get_renderer() and
                       info.have_version(1, 5) and
                       sys.platform == 'darwin'))]

    def __init__(self, context_share=None):
        """
        Setup workaround attr and object spaces (again to mock what is done in
        pyglet context)
        """
        self.object_space = ObjectSpace()
        for attr, check in self._workaround_checks:
            setattr(self, attr, None)

    def __repr__(self):
        return '%s()' % self.__class__.__name__

    def set_current(self):
        pass

    def destroy(self):
        pass

    def delete_texture(self, texture_id):
        pass

    def delete_buffer(self, buffer_id):
        pass

