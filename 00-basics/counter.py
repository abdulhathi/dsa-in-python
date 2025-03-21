from collections import Counter

s = set('bank')
print(s)
print(Counter(s))

print(Counter('bank') == Counter('kand'))

s1, s2 = 'bank', 'kanb'

dic = {}

for i, (a, b) in enumerate(zip(s1, s2)):
  dic[i] = set((a, b))
  if len(dic[i]) == 1:
    del dic[i]

li = ["".join(val) for val in dic.values()]
print(li)
print(True if li[0] == li[1] or li[0][::-1] == li[1] else False)

