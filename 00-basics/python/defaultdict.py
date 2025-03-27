from collections import defaultdict

dic = defaultdict(int)

for i in range(5):
  dic[i] += 1

print(dic)