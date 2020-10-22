# fffffaff v0.1
# by ArrayMy
import pygame, time
#start instance
pygame.init()

#window
width, height = 800, 600
backgroundColor = 0, 0, 0
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("app name")
#game attributes
charAttr = {
  'sizeHeight': 30,
  'sizeWidth': 30,
  'positionX': 15,
  'positionY': 15,
  'bgColor': {
    'red': 255,
    'green': 0,
    'blue': 0
  },
  'moveActions': {
    'jump': False,
    'move': False,
  }
}


#def charJump(char):
 # if charActionRules(char,'jump'):

#return character action activity True:False
def charActionRules(char,returnAction):
  for action in charAttr['moveActions']:
    if action == returnAction:
      return charAttr['moveActions'][action]

app = True
#start program
while app:
  window.fill(backgroundColor)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
            app = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    charAttr['positionY'] = charAttr['positionY'] - 1
  if keys[pygame.K_RIGHT]:
    charAttr['positionY'] = charAttr['positionY'] + 1
  if keys[pygame.K_UP]:
    charAttr['positionX'] = charAttr['positionX'] - 1
  if keys[pygame.K_DOWN]:
    charAttr['positionX'] = charAttr['positionX'] + 1
  
  pygame.draw.rect(window, (charAttr['bgColor']['red'],charAttr['bgColor']['green'],charAttr['bgColor']['blue']), (charAttr['positionY'],charAttr['positionX'],charAttr['sizeWidth'], charAttr['sizeHeight']))
  pygame.display.update()

  #testing functions
  charActionRules(charAttr, 'jump')


#stop instance            
pygame.quit()