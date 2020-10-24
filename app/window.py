#class Window is API for PyGame and this app
import pygame

# @window
# pygame
class Window:

  #create pygame instance
  def __init__(self):
    pygame.init()

  #set window size    
  def setSize(self,width,height):
    self.windowWidth = width
    self.windowHeight = height
    self.window = pygame.display.set_mode([width, height])
  
  #set window name
  def setName(self,name):
    pygame.display.set_caption(name)
  
  #window fill color
  def window_fill(self,backgroundColour):
    self.window.fill(backgroundColour)
  
  #window update
  def window_update(self):
    pygame.display.update()
  
  #render character
  def window_show_character(self, character):
    pygame.draw.rect(
      self.window,
      (character.attributes['color']),
      (character.attributes['positionY'],character.attributes['positionX'],character.attributes['sizeWidth'],character.attributes['sizeHeight']))


  def window_show_character_base(self, base):
    localWindowWidth = self.windowWidth
    localItemsCount = base.itemsCount
    localProces = True
    while localProces:
      if(localWindowWidth > 0):
        localItemsCount = localItemsCount + 1
        localWindowWidth = localWindowWidth - 60
        pygame.draw.rect(self.window,
         (base.attributes['color']),
         (localWindowWidth,
          base.attributes['positionX'],
          base.attributes['sizeWidth'],
          base.attributes['sizeHeight']))
      else:
        base.itemsCount = localItemsCount
        localProces = False


  
  #close button, event get (need for keyboard listeting)
  def window_close_cross(self):
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      return False
    return True    
  #check left, right keyboards
  def window_listen_keyboard(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      return 'left'
    if keys[pygame.K_RIGHT]:
      return 'right'

  def window_show_base(self, base):
    print("zesz")