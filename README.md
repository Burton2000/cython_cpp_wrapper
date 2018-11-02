# Wrapper for a cpp function in python
This is just an example of using Cython to wrap a cpp function for use within Python.  

On the command line run:
python setup.py build_ext --inplace

you can now import the module in python

import add.pyAdd
pyAdd(4,5)
9
