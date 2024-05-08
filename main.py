import pygame
import random
from cursor import Cursor
from red import Red
from blue import Blue 
from green import Green
from purple import Purple
from pink import Pink
import time 

#basic booleans
click_start = False
run= False 
level_1 = False
level_2 = False
level_3 = False
level_4 = False 
level_5 = False 

#gems list to randomize 
color_gems= ["red", "blue", "green", "purple", "pink"]


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption("Quick Thinking!")

#intro messages
introduction= my_font.render("Welcome to Quick thinking", True, (0,0,0))
directions1 = my_font.render("In this game, the background will show (in text) a color you have to collect.You need to pick the right colored gem in a certain time", True, (0,0,0))
directions2 = my_font.render("You need to quickly pick the right gem to advance to the next level", True, (0,0,0))
lose_directions = my_font.render("If you are not quick enough you have to repeat the level",True, (0,0,0))


r= 255
g= 250
b= 70


#sprites
c= Cursor(200,150)
r= Red(random.randint(0,300),random.randint(0,300))
p= Pink(random.randint(0,300), random.randint(0,300))
g= Green(random.randint(0,300), random.randint(0,300))
b= Blue(random.randint(0,300), random.randint(0,300))
pu= Purple(random.randint(0,300), random.randint(0,300))
        

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


#Main game loop 
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    run= False 
  

screen.fill(r,g,b)
if click_start == False:
   screen.blit(introduction, (150,150))
   screen.blit(directions1, (150,200))
   screen.blit(directions2, (150,250))
