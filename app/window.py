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

  def window_show_enemies(self, enemy):
    pygame.draw.rect(
      self.window,
      (enemy.attributes['color']),
      (enemy.attributes['positionY'],
      enemy.attributes['positionX'],
      enemy.attributes['sizeWidth'],
      enemy.attributes['sizeHeight']))    

  def window_show_character_base(self, base):
    localWindowWidth = self.windowWidth
    localItemsCount = base.itemsCount
    localProces = True
    while localProces:
      if(localWindowWidth > 0):
        localItemsCount = localItemsCount + 1
        base.items[localItemsCount] = localWindowWidth
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


  def window_create_shoot(self,character,type):
    if(type == "classic"):
      localHeight = 10
      localWidth = 10
    pygame.draw.rect(
      self.window,
      (125,125,125),
      (character.attributes['positionY'],
      character.attributes['positionX'],
      localHeight,
      localWidth))
    #Save shoots in array
    if(len(character.shoots) == 0):
      localShootsPosition = 0
    else:
      localShootsPosition = len(character.shoots)
    character.shoots[localShootsPosition] = {
      'color': (125,125,125),
      'positionX': character.attributes['positionX'],
      'positionY': character.attributes['positionY'],
      'height': localHeight,
      'width': localWidth,
      'type': type,
    }
    print(character.shoots)

  def window_render_shoots(self, character):
    print(character.shoots)
    #for shoot in character.shoots:
     # print(shoot)
      #pygame.draw.rect(
       # self.window,
        #(shoot['color']),
        #(shoot['positionY'],
        #shoot['positionX'],
        #shoot['height'],
        #shoot['width']))
      #shoot['positionX'] + 1    
  
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
    if keys[pygame.K_SPACE]:
      return 'shoot'
