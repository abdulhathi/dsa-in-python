l1 = [1, 3, 4, 2, 5]

d1 = {x: x**3 for x in l1}
print(d1)

d2 = {x: f'ID:{x}' for x in l1}
print(d2)

l2 = [101, 103, 102]
l3 = ['gfg', 'ide', 'courses']
d3 = {key: value for key, value in zip(l2, l3)}
print(d3)
