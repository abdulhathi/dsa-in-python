
rating = 9

def fun1():
  print(rating)

fun1()

def fun2():
  """
  This is fun2
  """
  global myVar
  myVar = "Abdul"

fun2()
print(myVar)
myVar = "Hathi"
print(myVar)


help(fun2)