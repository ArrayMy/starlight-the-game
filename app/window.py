import pygame

class Window:

  pygame = False

  def __init__(self):
    if self.pygame == False:
      self.pygame = pygame.init()

  def setSize(self,width, height):
    self.pygame.display.set_mode((width, height))

  def setName(self,name):
    self.pygame.display.set_caption(name)

  def window_show_character(self, character):
    self.pygame.draw.rect(
      self.pygame, (
        character.attributes['color'],
        character.attributes['positionY'],character.attributes['positionX'],character.attributes['sizeWidth'],character.attributes['sizeHeight']))