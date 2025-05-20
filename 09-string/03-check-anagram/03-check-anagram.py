from collections import defaultdict


def checkAnagram(s1: str, s2: str) -> bool:
  if len(s1) != len(s2):
    return False
  dic = defaultdict(int)
  n = len(s1)
  for i in range(n):
    dic[s1[i]] += 1
    dic[s2[i]] -= 1

  for value in dic.values():
    if value > 0:
      return False
  return True


print(checkAnagram('listen', 'silent'))
print(checkAnagram('aacb', 'acab'))
print(checkAnagram('aab', 'abb'))
