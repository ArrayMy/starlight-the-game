#class for enemies entities

class Entities:

  attributes = {} 

  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value

