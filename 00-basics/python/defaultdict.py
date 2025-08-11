from collections import defaultdict

dic = defaultdict(int)

for i in range(5):
  dic[i] += 1

print(dic)

dic = defaultdict(list)

for i in range(5):
  if not i in dic[i]:
    dic[i] = [10+i, 11+i]

li = [sum(val) for val in dic.values()]
print(max(li))
