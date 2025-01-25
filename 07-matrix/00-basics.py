# Create two dimentional array in python

rows = 4
cols = 5
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

print(matrix)

print('Column length : ', len(matrix[0]))
print('Row length : ', len(matrix))