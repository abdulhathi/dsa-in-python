from pathlib import Path

textFile = Path("00-basics/python/files/text1.txt")

with open(textFile, 'a') as file:
  file.write('My favorite drink is Ginger tea. \n')

with open(textFile, 'r') as file:
  print(file.readlines())