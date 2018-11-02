# Wrapper for a cpp function in python
This is just an example of using Cython to wrap a cpp function for use within Python.  

## How to run
On the command line run:  
`python setup.py build_ext --inplace`  

you can now import and use the module in python like so:

`import add.pyAdd`  
`pyAdd(4,5)`  
`>>>9`  
