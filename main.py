import pygame
import random
from cursor import Cursor
from red import Red
from blue import Blue 
from green import Green
from purple import Purple
from pink import Pink
import time


level= 1


#basic booleans
click_start = False
run= True
win=False
lose= False
time_run = True
try_again = False
round_start = False
ultimate_win= False

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
my_font_2 =pygame.font.SysFont('Playfair', 50)
my_font_3= pygame.font.SysFont("Robotto", 70)
pygame.display.set_caption("Quick Thinking!")

gem= ""

# gems list to randomize
# color_gems= ["red", "blue", "green", "purple", "pink"]

index = random.randint(0,4)
if index == 1:
    gem = "Red"
if index == 2:
    gem = "Blue"
if index == 3:
    gem = "Green"
if index == 4:
    gem = "Purple"
if index == 5:
    gem = "Pink"
display_color = my_font_2.render(str(gem), True, (255,255,255))



start_time= time.time()
end_time= time.time()
if time_run ==True:
    if level == 1 :
        time_left = float(round(10 - (end_time - start_time), 2))
        time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
    if level == 2 :
        time_left = float(round(8 - (end_time - start_time), 2))
        time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
    if level == 3:
        time_left = float(round(6 - (end_time - start_time), 2))
        time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
    if level == 4:
        time_left = float(round(4 - (end_time - start_time), 2))
        time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
    if level == 5:
        time_left = float(round(2 - (end_time - start_time), 2))
        time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))

#intro messages
introduction= my_font.render("Welcome to Quick thinking", True, (0,0,0))
directions1 = my_font.render("In this game, the background will show (in text) a color you have to collect", True, (0,0,0))
directions2 = my_font.render("You need to quickly pick the right gem to advance to the next level", True, (0,0,0))
display_level= my_font.render("level: " + str(level), True , (0,0,0))
display_win = my_font.render("Onto the next level!, press space to move on", True, (0, 0, 0))
game_start= my_font.render("click if you are ready to start", True, (0,0,0))
time_left_display= my_font.render("Time left: " + str(time_left),True, (0,0,0) )
try_again_display= my_font.render("You lost, press space to try again", True, (0,0,0))
ultimate_win_display= my_font_3.render("You have beat my game! Congrats", True, (0,0,0))



#sprites
c= Cursor(200,150)
red= Red(random.randint(0,500),random.randint(0,500))
pink= Pink(random.randint(0,500), random.randint(0,500))
green= Green(random.randint(0,500), random.randint(0,500))
blue = Blue(random.randint(0,500), random.randint(0,500))
purple= Purple(random.randint(0,500), random.randint(0,500))
bg = pygame.image.load("background.jpg")
bg= pygame.transform.scale(bg, (710,600))
index = random.randint(0,4)



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

   end_time = time.time()
   if time_run == True:
       if level == 1 and time_left != 0:
           time_left = float(round(7 - (end_time - start_time), 2))
           time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
       if level == 2 and time_left != 0:
           time_left = float(round(6 - (end_time - start_time), 2))
           time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
       if level == 3 and time_left != 0:
           time_left = float(round(5 - (end_time - start_time), 2))
           time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
       if level == 4 and time_left != 0:
           time_left = float(round(4 - (end_time - start_time), 2))
           time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
       if level == 5 and time_left != 0:
           time_left = float(round(2 - (end_time - start_time), 2))
           time_left_display = my_font.render("Time left: " + str(time_left), True, (0, 0, 0))
   ## ----- NO BLIT ZONE START ----- ##
   keys = pygame.key.get_pressed()
   # checking pressed key
   if keys[pygame.K_d]:
       c.move_direction("right")
   if keys[pygame.K_a]:
       c.move_direction("left")
   if keys[pygame.K_w]:
       c.move_direction("up")
   if keys[pygame.K_s]:
       c.move_direction("down")
   for event in pygame.event.get():
       if event.type == pygame.QUIT: # If user clicked close
         run = False
       if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          click_start= True
          time_run = True
          lose = False
          time_left = 5
        if event.type == pygame.TEXTINPUT:
            if event.text == " " :
                click_start = True
                time_run = True
        if c.rect.colliderect(red.rect) and gem == "Red" and time_left != 0:
          time_run = False
          win = True
          level += 1
          display_win = my_font.render("Onto the next level!", True, (0, 0, 0))
          display_level = my_font.render("level: " + str(level), True, (0, 0, 0))
        if c.rect.colliderect(blue.rect) and gem =="Blue" and time_left != 0:
           time_run = False
           win = True
           level += 1
           display_win = my_font.render("Onto the next level!", True, (0, 0, 0))
           display_level = my_font.render("level: " + str(level), True, (0, 0, 0))
        if c.rect.colliderect(green.rect) and gem == "Green" and time_left != 0:
            time_run = False
            win = True
            lose = False
            level += 1
            display_win = my_font.render("Onto the next level!", True, (0, 0, 0))
            display_level = my_font.render("level: " + str(level), True, (0, 0, 0))
        if c.rect.colliderect(purple.rect) and gem == "Purple" and time_left !=0:
            time_run = False
            win = True
            lose = False
            level += 1
            display_win = my_font.render("Onto the next level!", True, (0, 0, 0))
            display_level = my_font.render("level: " + str(level), True, (0, 0, 0))
        if c.rect.colliderect(pink.rect) and gem == "Pink" and time_left !=0:
            time_run == False
            win = True
            lose = False
            level += 1
            display_win = my_font.render("Onto the next level!", True, (0, 0, 0))
            display_level = my_font.render("level: " + str(level), True, (0, 0, 0))
        if time_left == 0.0 :
          lose= True
          win= False
          time_run = False
          try_again = True
        if win == True:
            time_run = False
        if level == 5 and win == True:
            ultimate_win == True
            ultimate_win_display = my_font_3.render("You have beat my game! Congrats", True, (0, 0, 0))

   screen.blit(bg, (0, 0))


   if click_start == False:
    screen.blit(introduction,(5,100))
    screen.blit(directions1,(5,150))
    screen.blit(directions2,(5,200))

    screen.blit(game_start, (5,300))

   if time_left ==0 or lose == True :
       screen.blit(try_again_display, (200,200))

   if click_start == True and time_run == True  :
       screen.blit(display_color, (500, 500))
       screen.blit(red.image, red.rect)
       screen.blit(blue.image, blue.rect)
       screen.blit(green.image, green.rect)
       screen.blit(purple.image, purple.rect)
       screen.blit(pink.image, pink.rect)
       screen.blit(c.image, c.rect)

   if click_start == True:
       screen.blit(display_level, (0, 10))
       screen.blit(time_left_display, (0,30))

   if win == True:
       screen.blit(display_win, (100,200))
   pygame.display.update()

   if ultimate_win == True:
       ultimate_win_display= my_font_3.render("You have beat my game! Congrats", True, (0,0,0))

pygame.quit()