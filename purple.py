import pygame

class Purple:
  def __init__(self, x ,y ):
    self.x = x
    self.y = y
    self.image = pygame.image.load("purple_gem.jpeg")
    self.image_size= self.image.get_size()
    scale_size = (self.image_size[0] * .08, self.image_size[1] * .08)
    self.image = pygame.transform.scale(self.image, scale_size)
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

  def move(self,new_x,new_y):
    self.x = new_x
    self.y = new_y
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])