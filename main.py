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
  'image': '',
  'moveActions': {
    'jump': False,
    'stepRight': False,
    'stepLeft': False,
  }
}

#game functions
def stepLeft(char):
  if returnAction(char,'stepLeft') == False:
    char['positionY'] = char['positionY'] - 1

def stepRight(char):
  if returnAction(char,'stepRight') == False:
    char['positionY'] = char['positionY'] + 1 

#help functions
def returnAction(char,returnAction):
  for action in charAttr['moveActions']:
    if action == returnAction:
      return charAttr['moveActions'][action]
  return "undefiend action"  

app = True
#start program
while app:
  window.fill(backgroundColor)
  #event listening
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
            app = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    stepLeft(charAttr)
  if keys[pygame.K_RIGHT]:
    stepRight(charAttr)
  #draw character  
  pygame.draw.rect(window, (charAttr['bgColor']['red'],charAttr['bgColor']['green'],charAttr['bgColor']['blue']), (charAttr['positionY'],charAttr['positionX'],charAttr['sizeWidth'], charAttr['sizeHeight']))
  pygame.display.update()

  #testing functions

#stop instance            
pygame.quit()