from pathlib import Path

textFile = Path("00-basics/python/files/text1.txt")

with open(textFile, 'w') as file:
  file.write('My name is Abdul \n')
  file.write('My location is Irvine \n')

with open(textFile, 'r') as file:
  print(file.readlines())