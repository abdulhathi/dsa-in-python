import math

def find_the_number_is_cube_root(num):
  cubeRoot = round(num ** (1/3))
  return (3 ** cubeRoot)


print(find_the_number_is_cube_root(81))
print(find_the_number_is_cube_root(243))

print((math.log10(243) / math.log10(3)) % 1 == 0) 

print(5.0 % 1 == 0)