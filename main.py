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
  'positionX': 140,
  'positionY': 390,
  'bgColor': {
    'red': 0,
    'green': 0,
    'blue': 255
  },
  'image': '',
  'moveActions': {
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

def showCharacter():
  pygame.draw.rect(window, (charAttr['bgColor']['red'],charAttr['bgColor']['green'],charAttr['bgColor']['blue']), (charAttr['positionY'],charAttr['positionX'],charAttr['sizeWidth'], charAttr['sizeHeight']))

def showItemInBase(rColor,gColor,bColor,positionX,positionY,width,height):
  pygame.draw.rect(window, (rColor,gColor,bColor), (positionX,positionY,width,height))

def showBase():
  proces = True
  localWidth = width
  while proces:
    if(localWidth > 0):
      localWidth = localWidth - 60  
      showItemInBase(0,255,0,localWidth,20,40,40)
      showItemInBase(0,255,0,localWidth,80,40,40)
    else:
      proces = False

#help functions
def returnAction(char,returnAction):
  for action in charAttr['moveActions']:
    if action == returnAction:
      return charAttr['moveActions'][action]
  return "undefiend action"  

def listenTurnOff():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
            app = False

def listeningKeyboard():
  listenTurnOff()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    stepLeft(charAttr)
  if keys[pygame.K_RIGHT]:
    stepRight(charAttr)

app = True
#start program
while app:
  window.fill(backgroundColor)

  listeningKeyboard()
  showBase()
  showCharacter()
  
  pygame.display.update()

  #testing functions

#stop instance            
pygame.quit()