import pygame

class Window:

  def __init__(self):
    pygame.init()
      

  def setSize(self,width,height):
    self.window = pygame.display.set_mode([width, height])

  def setName(self,name):
    pygame.display.set_caption(name)

  def window_show_character(self, character):
    pygame.draw.rect(
      self.window,
      (character.attributes['color']),
      (character.attributes['positionY'],character.attributes['positionX'],character.attributes['sizeWidth'],character.attributes['sizeHeight']))
  
  def window_close_cross(self):
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      return False
    return True    

  def window_listen_keyboard(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      return 'left'
    if keys[pygame.K_RIGHT]:
      return 'right'
      

  def window_fill(self,backgroundColour):
    self.window.fill(backgroundColour)

  def window_update(self):
    pygame.display.update()
