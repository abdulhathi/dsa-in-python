
# * Catalon number : 2nCn // (n+1)
def countUniqueBST(n):
  twoN = 2*n
  twoNCn = 1

  for i in range(twoN,n, -1):
    twoNCn *= i
  
  for i in range(1,n+1):
    twoNCn //= i

  return twoNCn // (n+1)


print(countUniqueBST(3))
print(countUniqueBST(4))
print(countUniqueBST(5))
