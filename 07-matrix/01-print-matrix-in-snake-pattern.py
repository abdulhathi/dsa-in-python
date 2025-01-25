def print_matrix_in_snake_pattern(matrix):
  rows, cols = len(matrix), len(matrix[0])
  for r in range(rows):
    if r % 2 == 0:
      for c in range(cols):
        print(matrix[r][c])
    else:
      for c in range(cols-1, -1, -1):
        print(matrix[r][c])


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(print_matrix_in_snake_pattern(matrix))