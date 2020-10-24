class Base:

  attributes = {}
  itemsCount = 0
  items = {}

  def __init__(self, character):
    self.character = character

  #duplicty code, TODO: create polymorf for this method
  def set(self, **kwargs):
    for key, value in kwargs.items():
      self.attributes[key] = value
    #self.size = args