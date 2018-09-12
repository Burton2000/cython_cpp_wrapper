from distutils.core import setup, Extension
from Cython.Build import cythonize

compile_args = ['-std=c++11']

wrap_func = Extension('wrap_class.add',
              sources=['wrap_class/cAdd.pyx', 'wrap_class/myAdd.cpp'],
              extra_compile_args=compile_args,
              language='c++')

setup(
	name='My first wrapped function',
	packages=['wrap_class'],
	ext_modules=cythonize(wrap_func)
)