for a, b in zip('baank', 'kanba'):
  print(a, b)
  if a not in s:
    s.add(a)
  else:
    s.discard(a)
  if b not in s:
    s.add(b)
  else:
    s.discard(b)
  print(s)
