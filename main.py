import pygame
import random
from cursor import Cursor
from red import Red
from blue import Blue 
from green import Green
from purple import Purple
from pink import Pink
from Gem import Gem
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
round_start = False
won=False
lose= False

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


start_time= time.time()
end_time= time.time()
time_left = float(round(10 - (end_time - start_time), 2))

#sprites
c= Cursor(200,150)
red= Red(random.randint(0,500),random.randint(0,500))
pink= Pink(random.randint(0,500), random.randint(0,500))
green= Green(random.randint(0,500), random.randint(0,500))
blue = Blue(random.randint(0,500), random.randint(0,500))
purple= Purple(random.randint(0,500), random.randint(0,500))
# gem = Gem(random.choice(color_gems),random.randint(0,300), random.randint(0,300))
level= 1
display_level= my_font.render("level: " + str(level), True , (255,255,255))
display_win = my_font.render("Onto the next level!", True, (255, 255, 255))

# set up variables for the display
SCREEN_HEIGHT = 540
SCREEN_WIDTH = 670
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r= 100
g= 10
b= 90




while run :
   # --- Main event loop
   ## ----- NO BLIT ZONE START ----- ##
   keys = pygame.key.get_pressed()  # checking pressed key
   if keys[pygame.K_d]:
       c.move_direction("right")
   if keys[pygame.K_a]:
       c.move_direction("left")
   if keys[pygame.K_w]:
       c.move_direction("up")
   if keys[pygame.K_s]:
       c.move_direction("down")

   for event in pygame.event.get():
       # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            click_start= True
        if click_start == True:
            round_start== True
            time.sleep(random.randint(0,4))



   #blitting station#
   screen.fill((r,g,b))

   if click_start == False:
    screen.blit(introduction,(5,100))
    screen.blit(directions1,(5,150))
    screen.blit(directions2,(5,200))

    screen.blit(game_start, (5,300))


   if click_start == True:
       screen.blit(c.image, c.rect)
       screen.blit(display_level, (0,10))
       screen.blit(pink.image, pink.rect )
       screen.blit(red.image, red.rect)
       screen.blit(green.image, green.rect)
       screen.blit(blue.image, blue.rect)
       screen.blit(purple.image, purple.rect)
   pygame.display.update()


pygame.quit()