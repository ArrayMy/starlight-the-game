from app.characters import Characters
from app.window import Window

app = Window()
app.setSize(800,600)
app.setName('Application Name')

mainCharacter = Characters()
mainCharacter.set(
  sizeHeight = 30,
  sizeWidth = 30,
  positionX = 140,
  positionY = 390,
  color = '0,0,255')

app.window_show_character(mainCharacter)

#while app:
  #window.fill(backgroundColor)
  #app = listenTurnOff()
  #listeningKeyboard()
  #showBase()
  #showCharacter()
  #if globalEnemy['maxEnemyCount'] >= globalEnemy['enemyCount']:
  #  enemy['positionX'] = createEnemy()
  #  globalEnemy['enemyCount'] = globalEnemy['enemyCount'] + 1
  #else:
  #  enemy['positionY'] = showEnemy(enemy)
  #pygame.display.update()

  #testing functions

#stop instance            
#pygame.quit()


#import  time, random
#start instance

#game functions
#def stepLeft(char):
 # if returnAction(char,'stepLeft') == False:
 #   char['positionY'] = char['positionY'] - 1

#def stepRight(char):
#  if returnAction(char,'stepRight') == False:
#    char['positionY'] = char['positionY'] + 1 

#def showItem(rColor,gColor,bColor,positionX,positionY,width,height):
 # pygame.draw.rect(window, (rColor,gColor,bColor), (positionX,positionY,width,height))

#def showBase():
 # proces = True
  #localWidth = width
  #while proces:
   # if(localWidth > 0):
    #  localWidth = localWidth - 60  
     # showItem(0,255,0,localWidth,20,40,40)
      #showItem(0,255,0,localWidth,80,40,40)
    #else:
     # proces = False

#def createEnemy():
 # localWidth = random.randint(40,740)
  #showItem(255,0,0,localWidth,540,40,40)
  #return localWidth

#def showEnemy(enemy):
 # showItem(255,0,0,enemy['positionX'],enemy['positionY'],40,40)
 # return enemy['positionY'] - 1

#help functions
#def returnAction(char,returnAction):
#  for action in charAttr['moveActions']:
#    if action == returnAction:
#      return charAttr['moveActions'][action]
#  return "undefiend action"  

#def listenTurnOff():
#  for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#      return False
#  return True    

#def listeningKeyboard():
#  keys = pygame.key.get_pressed()
#  if keys[pygame.K_LEFT]:
#    stepLeft(charAttr)
#  if keys[pygame.K_RIGHT]:
#    stepRight(charAttr)

#app = True
#start program