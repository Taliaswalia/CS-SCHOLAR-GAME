import pygame
import pygame.gfxdraw
from applw import Pong

from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  K_w,
  K_a,
  K_d,
  QUIT
)
screenWidth = 400
screenHeight = 300
snakeWidth = 40
speed = 7


#Player
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((snakeWidth, snakeWidth), pygame.SRCALPHA)
    self.run = []
    self.loop = 0
    self.run.append(pygame.image.load("PlayerFrame1.png"))
    self.run.append(pygame.image.load("PlayerFrame2.png"))
    self.run.append(pygame.image.load("PlayerFrame3.png"))
    self.run.append(pygame.image.load("PlayerFrame4.png"))
    self.surf =pygame.transform.scale(self.run[self.loop], (100 , 100))
    
    self.rect = self.surf.get_rect(center=(480,100))
    self.yOffset = 0
    self.gravity = 1
    self.last = pygame.time.get_ticks()


  # Player movement
  def update(self, playerkeys, isFlor,now):
   # self.isGrounded = pygame.sprite.spritecollideany(self,group)
   # now = pygame.time.get_ticks()
    

    
    if self.loop  == len(self.run)-1: 
      self.loop  = 0
    if now - self.last > 100: 
      self.loop = self.loop + 1
      self.surf = pygame.transform.scale(self.run[self.loop ], (100 , 100))
      self.last = pygame.time.get_ticks()

    if isFlor == True:
      self.yOffset = 0
      if playerkeys[K_UP] or playerkeys[K_w]:
        self.yOffset = -18
    else:
      self.yOffset += 1 
      
    

      # self.yOffset = self.yOffset + self.gravity

    self.rect.move_ip((0, self.yOffset))

    #elif playerkeys[K_DOWN] and self.rect.y < 382:
     #self.rect.move_ip(0,7)
    if (playerkeys[K_LEFT] or playerkeys[K_a]) and self.rect.x >0:
     self.rect.move_ip(-speed,0) 
    elif (playerkeys[K_RIGHT]or playerkeys[K_d]) and self.rect.x < 483:
     self.rect.move_ip(speed,0)

  # def createBull(self):
      
  #        return Pong(self.rect.x, self.rect.y)

  
