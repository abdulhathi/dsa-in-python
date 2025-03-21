from collections import OrderedDict

dic = OrderedDict()

dic[1] = 'a'
dic[2] = 'b'
dic[5] = 'c'

del dic[2]

print(type(dic.keys()))
print(list(dic.keys()))