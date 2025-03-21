"""
  * list comprehension to find all even numbers
"""

even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)

"""
  * get all upper case
"""
li = ['geeks', 'for', 'geeks', 'gfg', 'ide']

print([word.upper() for word in li if word.startswith('g')])
