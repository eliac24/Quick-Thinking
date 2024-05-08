import pygame
import random
from cursor import Cursor
from red import Red
from blue import Blue 
from green import Green
from purple import Purple
from pink import Pink

click_start = False
level_1 = False
level_2 = False
level_3 = False
level_4 = False 
level_5 = False 


introduction= print("Welcome to Quick Thinking!")
directions1 = print("In this game, the background will show (in text) a color you have to collect.You need to pick the right colored gem in a certain time")
directions2 = print("You need to quickly pick the right gem to advance to the next level")
lose_directions = ("If you are not quick enough you have to repeat the level")

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption("Quick Thinking!")

r= 100
b= 30
g= 70
background= (r,g,b)

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


screen.fill((background))