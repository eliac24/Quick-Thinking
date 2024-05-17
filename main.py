import pygame
import random
from cursor import Cursor
from red import Red
from blue import Blue 
from green import Green
from purple import Purple
from pink import Pink
import time



#time
start_time= time.time()
time_1= float(10)
time_2= float(7)
time_3= float(5)
time_4= float(3)
time_5= float(2)


#basic booleans
click_start = False
run= True 
level_1 = False
level_2 = False
level_3 = False
level_4 = False 
level_5 = False 

#gems list to randomize 
color_gems= ["red", "blue", "green", "purple", "pink"]


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Quick Thinking!")

#intro messages
introduction= my_font.render("Welcome to Quick thinking", True, (0,0,0))
directions1 = my_font.render("In this game, the background will show (in text) a color you have to collect", True, (0,0,0))
directions2 = my_font.render("You need to quickly pick the right gem to advance to the next level", True, (0,0,0))

game_start= my_font.render("click if you are ready to start", True, (0,0,0))





#sprites
c= Cursor(200,150)
red= Red(random.randint(0,300),random.randint(0,300))
pink= Pink(random.randint(0,300), random.randint(0,300))
green= Green(random.randint(0,300), random.randint(0,300))
blue = Blue(random.randint(0,300), random.randint(0,300))
purple= Purple(random.randint(0,300), random.randint(0,300))
level= 0

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r= 100
g= 10
b= 90


while run :
   # --- Main event loop
   ## ----- NO BLIT ZONE START ----- ##
   for event in pygame.event.get():
       # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            click_start= True
            level += 1
        if level ==1:
            level_1_border= my_font.render("Level One: You have 10 seconds", True, (0,0,0))
            level_1 == True
        if level == 2:
            level_2_border = my_font.render("level two: You have 8 seconds", True, (0,0,0))
            level_2== True
        if level == 3:
            level_3_border = my_font.render("Level three: You have 6 seconds", True, (0,0,0))
            level_3 == True
        if level == 4:
            level_4_border = my_font.render("Level four: You have 4 seconds", True, (0,0,0))
            level_4 == True

   #blitting station#
   screen.fill((r,g,b))





   if click_start == False:
    screen.blit(introduction,(5,100))
    screen.blit(directions1,(5,150))
    screen.blit(directions2,(5,200))

    screen.blit(game_start, (5,300))


   if click_start == True:
       screen.blit(c.image, c.rect)

   if click_start== True and level_1 == True:

   pygame.display.update()


pygame.quit()