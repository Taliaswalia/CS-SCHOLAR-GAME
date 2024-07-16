import pygame
import math
import random


screenWidth = 400
screenHeight = 300
width = 40
speed = 7


class Enemy(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, finalPosx, size):
        super(Enemy, self,).__init__()
        #random.choice
        self.size = size
        self.enemyShape = [pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('5.png')]
        self.x = random.choice(self.enemyShape)
        self.surf = pygame.transform.scale(random.choice(self.enemyShape),(self.size, self.size))
      # self.x = 7
        self.finalPosx = finalPosx
      # self.surf.fill((18, 107, 4))
      # self.surf = pygame.Surface((self.size, self.size))
        
      #  self.surf.fill((95,87,120))
        self.rect = self.surf.get_rect (center=(xpos,ypos))
        
    
    def update(self):
      dx, dy = self.finalPosx - self.rect.x, 600 - self.rect.y
      dist = math.hypot(dx, dy)
      if round(dist) > 1:
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        #self.x = self.x *0.5self
        self.rect.x += dx * 1.0002
        self.rect.y += dy * 1.0002

        self.size += 1.5
        self.surf = pygame.transform.scale(self.x, (self.size, self.size))
        # size = round((width*(self.x))*2)
        # self.surf = pygame.transform.scale(random.choice(self.enemyShape),(size, size))
        #self.surf.fill((18, 107, 4))

      else:
        self.kill()

  
