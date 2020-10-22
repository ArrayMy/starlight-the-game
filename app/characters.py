class Characters:
 
  attributes = {} 

  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value
    print(self.attributes)
  