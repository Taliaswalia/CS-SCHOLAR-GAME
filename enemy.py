import pygame
import math
import random
from hitbox import Hitbox


screenWidth = 700
screenHeight = 600
width = 60
speed = 7

screen = pygame.display.set_mode((screenWidth, screenHeight))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, finalPosx, size):
        super(Enemy, self,).__init__()
        #random.choice
        self.size = size
        self.enemyShape = [pygame.image.load('triangleEn.png'),pygame.image.load('hexagonEn.png'),pygame.image.load('octogonEn.png'), pygame.image.load('squareEn.png'),pygame.image.load('pentagonEn.png')]
        self.x = random.choice(self.enemyShape)
        self.surf = pygame.transform.scale(self.x,(self.size, self.size+10))
        self.xpos = xpos
        self.ypos = ypos

        self.finalPosx = finalPosx
        # self.surf = pygame.Surface((self.size, self.size))
        # self.surf.fill((18, 107, 4))
        
        
      #  self.surf.fill((95,87,120))
        self.rect = self.surf.get_rect (center=(xpos,ypos))
        
    
    def update(self):
      dx, dy = self.finalPosx - self.rect.x, 600 - self.rect.y
      dist = math.hypot(dx, dy)
      if round(dist) > 1:
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.

        self.xpos += dx * 1.002
        self.ypos += dy * 1.002

        self.size *= 1.02
        self.surf = pygame.transform.scale(self.x, (self.size, self.size))
        self.rect = self.surf.get_rect (center=(self.xpos,self.ypos))
        

      else:
        self.kill()

  
