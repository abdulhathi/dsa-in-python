from collections import defaultdict

dict = defaultdict(int)

dict[[1, 2]] = 1
dict[[2, 3]] = 1

print(dict)

dict[[1, 2]] -= 1
print(dict)

for key, val in dict:
  print(type(key), type(val))
