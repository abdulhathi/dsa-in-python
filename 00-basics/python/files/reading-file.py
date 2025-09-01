from pathlib import Path

# # path = Path.home('')
# print(Path.home())
textFile = Path("00-basics/python/files/text.txt")
file = open(textFile, 'r')
print(file)

print(file.name)
print(file.mode)
file.close()

# * read()
print("----Read()--------")
with open(textFile, 'r') as file1:
  fileContent = file1.read()
  print(file1.closed)

print(fileContent)

print(file1.closed)

# * readline
print("----ReadLine--------")
with open(textFile, 'r') as file1:
  print(file1.readline())
  print(file1.readline())

# * Read particular chars
print("----ReadLine(4)--------")
with open(textFile, 'r') as file1:
  print(file1.readline(4))
  print(file1.readline(5))
  file1.seek(20)
  print(file1.readline(5))

print("----ReadLines--------")
# * readlines
with open(textFile, 'r') as file1:
  print(file1.readlines())

