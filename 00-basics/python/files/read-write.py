
from pathlib import Path

readFile = Path("00-basics/python/files/text.txt")
writeFile = Path("00-basics/python/files/text1.txt")

with open(readFile, 'r') as file1:
  with open(writeFile, 'w') as file2:
    for lineData in file1.readlines():
      file2.write(lineData)

with open(writeFile, 'r') as file2:
  print(file2.readlines())