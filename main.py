# fffffaff v0.1
# by ArrayMy
import pygame, time, random
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

globalEnemy = {
  'enemyCount' : 0,
  'maxEnemyCount': 1,
  'delay': False,
}

enemy = {
  'positionX' : 0,
  'positionY' : 540,
}

speed = 0.25

#game functions
def stepLeft(char):
  if returnAction(char,'stepLeft') == False:
    char['positionY'] = char['positionY'] - 1

def stepRight(char):
  if returnAction(char,'stepRight') == False:
    char['positionY'] = char['positionY'] + 1 

def showCharacter():
  pygame.draw.rect(window, (charAttr['bgColor']['red'],charAttr['bgColor']['green'],charAttr['bgColor']['blue']), (charAttr['positionY'],charAttr['positionX'],charAttr['sizeWidth'], charAttr['sizeHeight']))

def showItem(rColor,gColor,bColor,positionX,positionY,width,height):
  pygame.draw.rect(window, (rColor,gColor,bColor), (positionX,positionY,width,height))

def showBase():
  proces = True
  localWidth = width
  while proces:
    if(localWidth > 0):
      localWidth = localWidth - 60  
      showItem(0,255,0,localWidth,20,40,40)
      showItem(0,255,0,localWidth,80,40,40)
    else:
      proces = False

def createEnemy():
  localWidth = random.randint(40,740)
  showItem(255,0,0,localWidth,540,40,40)
  return localWidth

def showEnemy(enemy):
  showItem(255,0,0,enemy['positionX'],enemy['positionY'],40,40)
  return enemy['positionY'] - 1

#help functions
def returnAction(char,returnAction):
  for action in charAttr['moveActions']:
    if action == returnAction:
      return charAttr['moveActions'][action]
  return "undefiend action"  

def listenTurnOff():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return False
  return True    

def listeningKeyboard():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    stepLeft(charAttr)
  if keys[pygame.K_RIGHT]:
    stepRight(charAttr)

app = True
#start program
while app:
  window.fill(backgroundColor)
  app = listenTurnOff()
  listeningKeyboard()
  showBase()
  showCharacter()
  if globalEnemy['maxEnemyCount'] >= globalEnemy['enemyCount']:
    enemy['positionX'] = createEnemy()
    globalEnemy['enemyCount'] = globalEnemy['enemyCount'] + 1
  else:
    enemy['positionY'] = showEnemy(enemy)
  pygame.display.update()

  #testing functions

#stop instance            
pygame.quit()