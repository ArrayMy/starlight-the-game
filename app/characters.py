class Characters:
 
  attributes = {} 

  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value
  
  def move(self, action):
    if(action == 'left'):
      self.stepLeft()
    if(action == 'right'):
      self.stepRight()  

  def stepLeft(self):
    self.attributes['positionY'] = self.attributes['positionY'] - 1

  def stepRight(self):
    self.attributes['positionY'] = self.attributes['positionY'] + 1  