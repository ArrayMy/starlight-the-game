#class for enemies entities

class Enemies:

  speed = 1

  attributes = {} 

  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value

  def move(self,type):
    if(type == "loop"):
      self.stepUp()
  
  def stepUp(self):
    self.attributes['positionX'] = self.attributes['positionX'] - self.speed
