import numpy as np

a = np.array([0, 1, 2, 3, 4])
a[0] = 100
print(a.size)
print(a.ndim) # ^ dimenstion
print(a)

print(a[2:4])

a[3:5] = 400,500
print(a)

# ^ Steps in slicing (Every 2nd element)
print(a[0:5:2])

print(a[:4])
print(a[4:])

