import pygame

class Cursor:
  def __init__(self, x ,y ):
    self.x = x
    self.y = y
    self.image = pygame.image.load("CursoR.png")
    self.rescale_image(self.image)
    self.image_size= self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * .3, self.image_size[0] *.3)


  def rescale_image(self,image):
    self.image_size = self.image.get_size()
    scale_size= (self.image_size[0] * .2 , self.image_size[1] * .2 )
    self.image = pygame.transform.scale(self.image, scale_size)
    self.mid_height= (self.image.get_width()/2)
    self.mid_width = (self.image.get_height()/2)
  def move(self,new_x,new_y):
    self.x = new_x
    self.y = new_y
    self.new_x, self.new_y= pygame.mouse.get_pos()
    self.screen.blit(self.image, (self.new_x, self.new_y))