import pygame
from player import Player
from applw import Pong
from ground import Ground
from enemy import Enemy
import math
import pygame.mouse
from pgzrun import *
import random as random
import os

from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  QUIT

)

pygame.init()
clock = pygame.time.Clock()




player = Player()

screenWidth = 700
screenHeight = 600
isFlor = False # dont need anymore
ground = Ground()
cooldown = 500 # for bullets

screen = pygame.display.set_mode((screenWidth, screenHeight))
backGround = pygame.image.load('bg RESIZED.png')
backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

allSprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
allSprites.add(ground)
allSprites.add(player)

xPlaces = [100, 400, 260, 300, 140, 490, 10] # the x value that the enemy will go to

bgm = pygame.mixer.Sound("EscapeFromNewYork.mp3") # music


lives = 5
isDead = False

CUSTOM_FONT = "spacegeometryfont.otf"
font = pygame.font.Font(CUSTOM_FONT, 36)
highscore = 0

width = 700
height = 600
x0 = width//2
y0 = height//2

circleCount = 100
radiusDiff = 10
stepCol = (255-50)/circleCount

circles = []

for i in range(circleCount):
  circles.append([x0, y0, 100, 50])

def draw_circle(circle):
  angle = 0                   # Angle of movement along the ellipse to draw the next point.
  step = math.pi / 50    # Step with which the points of the ellipse are drawn.

  circle_x = circle[0]
  circle_y = circle[1]
  circle_r = circle[2]
  circle_color = circle[3]

  while angle < math.pi * 2:
      x = round(circle_x + math.sin(angle) * circle_r//2)
      y = round(circle_y + math.cos(angle) * circle_r //2)

      if 0 < x < width and 0 < y < height:
          pygame.draw.circle(screen,(0, circle_color, circle_color), (x,y), 2)

      angle += step

global rotAngle
rotAngle = 0

pong = Pong(10,10)
last = pygame.time.get_ticks()
lastEnemy = pygame.time.get_ticks()



while True:
  clock.tick(60)
  screen.blit(backGround, (0,0))
  bgm.play(-1)


  for i in range(len(circles) - 2, -1, -1):
      circle = circles[i]

      circle[2] += radiusDiff
      circle[3] += stepCol
      circles[i + 1] = circle

      draw_circle(circle)

  # Calculating X, Y coordinates for a new circle (Changes how much the tunnel rorates)
  rotAngle += 0.05
  x = x0 + math.sin(rotAngle) * 1.0
  y = y0 + math.cos(rotAngle) * 1.0

  # Add a new circle to the beginning of the list
  circles[0] = [x, y, 100, 50]


  playerkeys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()

  playerkeys = pygame.key.get_pressed()
  hasFloored = pygame.sprite.collide_rect(player, ground)

  now = pygame.time.get_ticks()
  if (now - last >= cooldown) and playerkeys[K_SPACE]:
    pong = Pong(player.rect.x, player.rect.y +40)
    
    allSprites.add(pong)
    bullets.add(pong)
    last = pygame.time.get_ticks()
  if (now - lastEnemy >= 1000) and len(enemies) <= 5:
       enemy = Enemy(random.randint(300,350), random.randint(300,340), random.choice(xPlaces), 20)
       enemies.add(enemy)

       lastEnemy = pygame.time.get_ticks()

  if (lives == 0):
      print(" YOU DIED PRESS P to play again")
      

  if pygame.sprite.spritecollide(player, enemies, True):
      lives = lives - 1
  

  if pygame.sprite.groupcollide(bullets, enemies, True, True):
      print(" End the sides")
      highscore += 100

  highscore += 1 

  bullets.update(player)
  enemies.update()


  if hasFloored:
      isFlor = True
  else:
      isFlor = False

  for en in enemies:
     screen.blit(en.surf, en.rect)

  for sprite in allSprites:
            screen.blit(sprite.surf, sprite.rect)
  

  
          
            

  player.update(playerkeys, isFlor, now)
  score_text = font.render(f'Score: {highscore}', True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
 

  pygame.display.update()
 # while moving == True:
  # player.rect.x += 1
