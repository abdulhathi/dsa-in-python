import numpy as np

a = np.array([[10, 20, 30], [11, 21, 31], [12, 22, 32]])

print(a)
""" 
  [[10 20 30]
   [11 21 31]
   [12 22 32]]
"""
print(a.ndim)
print(a.shape)
print(a.size)
print(a[1][2])

# ^ Slicing
print(a[0,0:2])   # ^ [10 20]

print(a[0:2, 2])   # ^ [30 31]