from sys import *
from os import system


system('pip install cython')
i = argv[1]


makefile = """
from distutils.core import Extension, setup
from Cython.build import cythonize


ext = Extension(name="debug", sources=["debug.pyx"])
setup(ext_modules=cythonize(ext))
"""


setup = open('setup.py', 'w').write(makefile)
py = open(i, 'r').read()


pyx = open('debug.pyx', 'a').write(py)
run = system('python3 setup.py')
