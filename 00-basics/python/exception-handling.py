try:
  a = 10 / 0
except ZeroDivisionError:
  print(ZeroDivisionError)


try:
  a = 10 / 0
except Exception as e:
  print(e)

try:
  a = 10 / 1
except Exception as e:
  print(e)
else:
  print('This is try except else block')


try:
  a = 10 / 1
except Exception as e:
  print(e)
else:
  print('This is try except else block')
finally:
  print("This is the finally block")

