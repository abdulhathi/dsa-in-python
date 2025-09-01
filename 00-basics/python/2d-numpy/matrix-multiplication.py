import numpy as np

x = np.array([[1,2],[3,4]])
print(np.sqrt(x))
print(np.max(x))
print(np.min(x))

y = np.array([[2,2],[2,2]])
print(2*x)

print(x*y)

A = np.array([[0,1,1],[1,0,1]])
B = np.array([[1,1],[1,1],[-1,1]])

c = np.dot(A,B)
print(c)