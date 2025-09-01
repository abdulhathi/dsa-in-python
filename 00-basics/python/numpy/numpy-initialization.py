import numpy as np

a = np.array([0, 1, 2, 3, 4])
print(a)
print(type(a))    # <class 'numpy.ndarray'>

print(type(a[0]))  # <class 'numpy.int64'>
print(a.dtype)    # int64

print(np.__version__)  # 2.0.2


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b)
print(type(b))    # <class 'numpy.ndarray'>

print(type(b[0])) # <class 'numpy.float64'>
print(b.dtype)    # float64
