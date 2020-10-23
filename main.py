from app.characters import Characters
from app.window import Window
from app.enemies import Entities
import random
 
#Create window
app = Window()
app.setSize(800,600)
app.setName('fffffaff')

#Create entities
mainCharacter = Characters()
mainCharacter.set(
  sizeHeight = 30,
  sizeWidth = 30,
  positionX = 140,
  positionY = 390,
  color = (0,0,255))

enemy =  Entities()
enemy.set(
  sizeHeight = 30,
  sizeWidth = 30,
  positionX = 580,
  positionY = random.randint(20, 780),
  color = (255,0,0)
)

program_status = True

#Start program
while program_status:
  #Exit?
  program_status = app.window_close_cross()
  #Reset screen
  app.window_fill((0,0,0))
  #Render entities
  app.window_show_character(mainCharacter)
  #Update entities
  mainCharacter.move(app.window_listen_keyboard())
  #Render updates
  app.window_update()
