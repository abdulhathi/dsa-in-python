def parentFunc():
  a, b = 0, 0
  def childFunc():
    nonlocal a, b
    a += 1
    b += 1

  childFunc()
  return a, b

print(parentFunc())


# * Empty function
def fun1():
  pass

print(fun1())


def f(x):
  return x**2 + 3*x + 2

print(f(1))

print(1**2 + 3*1)