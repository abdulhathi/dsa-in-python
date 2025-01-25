def matrix_boundy_traversal(matrix):
  top, right, bottom, left = 0, len(matrix[0])-1, len(matrix)-1, 0
  res = []
  while top <= bottom and left <= right:
    for c in range(left, right+1):
      res.append(matrix[top][c])
    top += 1

    for r in range(top, bottom+1):
      res.append(matrix[r][right])
    right -= 1

    if top <= bottom and left <= right:
      for c in range(right,left-1,-1):
        res.append(matrix[bottom][c])
      bottom -= 1

      for r in range(bottom, top-1,-1):
        res.append(matrix[r][left])
      left += 1
  return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix_boundy_traversal(matrix))

matrix = [[1, 2, 3, 4]]
print(matrix_boundy_traversal(matrix))

matrix = [[1], [2], [3]]
print(matrix_boundy_traversal(matrix))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(matrix_boundy_traversal(matrix))
