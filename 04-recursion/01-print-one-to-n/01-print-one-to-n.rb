def print_one_to_n(n)
  @res = []
  def dfs(n)
    return if n == 0
    dfs(n-1)
    @res.push(n)
  end
  dfs(n)
  @res
end

print print_one_to_n(5)