def parentFunc():
  a, b = 0, 0
  def childFunc():
    nonlocal a, b
    a += 1
    b += 1

  childFunc()
  return a, b

print(parentFunc())