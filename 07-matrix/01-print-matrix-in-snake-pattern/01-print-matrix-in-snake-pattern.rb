def print_matrix_in_snake_pattern(matrix)
  n = matrix.length
  m = matrix[0].length
  res = []
  (0..n-1).each do |i|
    iteration = (0..m-1).to_a
    iteration = (0..m-1).to_a.reverse if i % 2 != 0 
    iteration.each do |j|
      res.append(matrix[i][j])
    end
  end
  res
end


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print print_matrix_in_snake_pattern(matrix)

