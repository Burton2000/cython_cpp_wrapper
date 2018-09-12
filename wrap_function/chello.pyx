cdef extern from "myAdd.h":
	int add(int x, int y);

def pyAdd(x, y):
	return add(x, y)

