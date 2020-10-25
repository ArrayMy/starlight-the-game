#class for player Character, attributes and actions

# @attributes:
# (sizeHeight, sizeWidth, positionX, positionY, color)
class Characters:

  shoots =  {}
  attributes = {} 

  #declare character structure without limit
  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value

  #detect move and call right method
  def move(self, action, window):
    if(action == 'left'):
      self.stepLeft()
    if(action == 'right'):
      self.stepRight()  
    if(action == 'shoot'):
      self.shoot(window)

  #shoot
  def shoot(self,window):
    window.window_create_shoot(self,"classic")
  
  #stepleft
  def stepLeft(self):
    self.attributes['positionY'] = self.attributes['positionY'] - 1
    
  #stepright
  def stepRight(self):
    self.attributes['positionY'] = self.attributes['positionY'] + 1  