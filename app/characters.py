#class for player Character, attributes and actions

# @attributes:
# (sizeHeight, sizeWidth, positionX, positionY, color)
class Characters:

  attributes = {} 

  #declare character structure without limit
  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value

  #detect move and call right method
  def move(self, action):
    if(action == 'left'):
      self.stepLeft()
    if(action == 'right'):
      self.stepRight()  

  #stepleft
  def stepLeft(self):
    self.attributes['positionY'] = self.attributes['positionY'] - 1
    
  #stepright
  def stepRight(self):
    self.attributes['positionY'] = self.attributes['positionY'] + 1  