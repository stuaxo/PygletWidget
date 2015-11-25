#!/usr/bin/env python

cmdclass={}
try:
    from setuptools import setup, Command

    from glob import glob
    from os.path import abspath, basename, dirname, join, normpath, relpath
    from shutil import rmtree

    here = normpath(abspath(dirname(__file__)))

    class CleanCommand(Command):
        """Custom clean command to tidy up the project root."""
        CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info ./__pycache__'.split(' ')

        user_options = []

        def initialize_options(self):
            pass
        def finalize_options(self):
            pass
        def run(self):
            global here

            for path_spec in self.CLEAN_FILES:
                # Make paths absolute and relative to this path
                abs_paths = glob(normpath(join(here, path_spec)))
                for path in [str(p) for p in abs_paths]:
                    if not path.startswith(here):
                        # Die if path in CLEAN_FILES is absolute + outside this directory
                        raise ValueError("%s is not a path inside %s" % (path, here))
                    print('removing %s' % relpath(path))
                    rmtree(path)
    cmdclass={'clean': CleanCommand}
except ImportError as e:
    print e
    from distutils.core import setup


setup(name='pygletwidget',
      cmdclass=cmdclass,
      version='0.1.0',
      description='Pyglet Widget for QT4 or PySide',
      author='ColinDuquesnoy',
      author_email='',
      url='https://github.com/stuaxo/QPygletWidget',
      packages=['pygletwidget', 'pygletwidget.qt4', 'pygletwidget.pyside'],
     )
