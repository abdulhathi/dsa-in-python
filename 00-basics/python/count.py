from collections import Counter

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

loremCount = givenstring.count('Lorem')

print(loremCount)

print(Counter(givenstring.split()))

