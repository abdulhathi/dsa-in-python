import numpy as np
u = np.array([1, 0])  # ^ 1 is x axis and 0 is y axis
v = np.array([0, 1])  # ^ 0 is x axis and 1 is y axis

z = np.add(u, v)
print(z)

# * Broadcasting Adding constanst to an numpy array

arr = np.array([0, 1, 2, 3, 4])
print(arr + 1)

u = np.array([1,2])
v = np.array([3,2])

print(u+v)

z = u * v
print(z)

print(np.dot(u,v))
