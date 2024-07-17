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
from Healthbar import Health_Bar


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

# screen = pygame.display.set_mode((screenWidth, screenHeight))
# backGround = pygame.image.load('bg RESIZED.png')
# backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

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
score = 0

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
#THIS PART HERE USE IT FOR HEALTH BAR AAAAAAAAAAA
health = 100
health_bar = Health_Bar(580, 20)
allSprites.add(health_bar)
start_game = False

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
BG_COLOR = (0, 0, 0)

# Load assets
CUSTOM_FONT = "spacegeometryfont.otf"
BACKGROUND_IMAGE = "bg RESIZED.png"
LOGO_IMAGE = "logo.png"
LOGO_WIDTH = 350

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load custom assets
background = pygame.image.load(BACKGROUND_IMAGE).convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
logo_original = pygame.image.load(LOGO_IMAGE).convert_alpha()

# Resize logo image
logo_height = int(LOGO_WIDTH / logo_original.get_width() * logo_original.get_height())
logo = pygame.transform.scale(logo_original, (LOGO_WIDTH, logo_height))

# Load the background images
background_images = [pygame.image.load(f"{i}.png").convert_alpha() for i in range(3, 12)]

# Load custom font
font_path = os.path.join(os.path.dirname(__file__), CUSTOM_FONT)
font = pygame.font.Font(CUSTOM_FONT, 48)

# Function to draw text in the center of the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to handle the floating images
def create_floating_images(num_images):
    images = []
    for _ in range(num_images):
        img = random.choice(background_images)
        aspect_ratio = img.get_width() / img.get_height()
        size = random.randint(50, 150)
        new_width = int(size * aspect_ratio)
        img = pygame.transform.scale(img, (new_width, size))

        # Randomly place offscreen around the canvas
        start_positions = [
            (-img.get_width(), random.randint(-img.get_height(), SCREEN_HEIGHT)),
            (SCREEN_WIDTH, random.randint(-img.get_height(), SCREEN_HEIGHT)),
            (random.randint(-img.get_width(), SCREEN_WIDTH), -img.get_height()),
            (random.randint(-img.get_width(), SCREEN_WIDTH), SCREEN_HEIGHT)
        ]
        start_x, start_y = random.choice(start_positions)

        rect = img.get_rect()
        rect.x = start_x
        rect.y = start_y

        # Random speed
        speed = [random.uniform(-2.5, 2.5), random.uniform(-2.5, 2.5)]

        images.append((img, rect, speed))
    return images

# Update the positions of floating images
def update_floating_images(images):
    for i, (img, rect, speed) in enumerate(images):
        rect.x += speed[0]
        rect.y += speed[1]

        # Wrap around offscreen
        if rect.right < 0 or rect.left > SCREEN_WIDTH or rect.bottom < 0 or rect.top > SCREEN_HEIGHT:
            # Choose a new image, size, and speed
            new_img = random.choice(background_images)
            aspect_ratio = new_img.get_width() / new_img.get_height()
            size = random.randint(50, 150)
            new_width = int(size * aspect_ratio)
            new_img = pygame.transform.scale(new_img, (new_width, size))

            # Randomly place offscreen around the canvas
            start_positions = [
                (-new_img.get_width(), random.randint(-new_img.get_height(), SCREEN_HEIGHT)),
                (SCREEN_WIDTH, random.randint(-new_img.get_height(), SCREEN_HEIGHT)),
                (random.randint(-new_img.get_width(), SCREEN_WIDTH), -new_img.get_height()),
                (random.randint(-new_img.get_width(), SCREEN_WIDTH), SCREEN_HEIGHT)
            ]
            start_x, start_y = random.choice(start_positions)

            rect.x = start_x
            rect.y = start_y

            # Random speed
            speed = [random.uniform(-2.5, 2.5), random.uniform(-2.5, 2.5)]

            images[i] = (new_img, rect, speed)

# Main loop
clock = pygame.time.Clock()
floating_images = create_floating_images(25)
while not start_game:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("WORD")
                    start_game = True

        screen.blit(background, (0, 0))
        score = 0


        # Update and draw floating images
        update_floating_images(floating_images)
        for img, rect, _ in floating_images:
            screen.blit(img, rect)

        # Draw the logo centered at the top of the screen
        screen.blit(logo, (SCREEN_WIDTH // 2 - logo.get_width() // 2, 80))

        # Draw the text using custom font
        draw_text("press SPACE to start", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

        pygame.display.flip()
        clock.tick(30)  # Slower frame rate

    # Placeholder for the next screen

    

print(start_game)
# if __name__ == "__main__":
#     main()
#     pygame.quit()


while start_game:
  clock.tick(60)
  screen.blit(background, (0,0))
  #score = 0
  bgm.play(-1)
  #THIS PART HERE USE IT FOR HEALTH BAR AAAAAAAAAA
  health_bar.update(health) #initializes health bar


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

  if (health == 0):
      #print(" YOU DIED PRESS P to play again")
      start_game = False
      
  for en in enemies:
    if player.rect.x - en.xpos < en.size and player.rect.y - en.ypos < en.size:
        if pygame.sprite.spritecollide(player, enemies, True):
            health -= 10


  

  if pygame.sprite.groupcollide(bullets, enemies, True, True):
      print(" End the sides")
      score += 100

  score += 1 
  if highscore < score:
      highscore = score

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
