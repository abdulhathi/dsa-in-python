
def decimal_to_binary(dec):
  binary = ""
  quotient = dec
  while quotient:
    reminder = quotient % 2
    quotient = quotient // 2
    binary = str(reminder) + binary
  
  return binary

res = decimal_to_binary(18)
print(res)

res = decimal_to_binary(12)
print(res)
