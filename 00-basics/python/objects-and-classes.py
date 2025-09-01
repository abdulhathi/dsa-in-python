class Circle:
  name = 'Circle'
  def __init__(self, radius, color):
    self.Radius = radius
    self.Color = color
  
  def addRadius(self, radius):
    self.Radius += radius


redCircle = Circle(3, 'Red')
for attr in dir(redCircle):
  print(attr)

redCircle.addRadius(10)
print(redCircle.Radius)
print(redCircle.name)