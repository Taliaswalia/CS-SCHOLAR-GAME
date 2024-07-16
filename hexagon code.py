import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hexagon Shooter Game")

# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)

# Hexagon properties
hexagons = []
hexagon_speed = 1
shape_add_counter = 0
shape_add_interval = 100  # Number of frames between adding new shapes

# Clock
clock = pygame.time.Clock()

# Function to draw a spinning hexagon
def draw_hexagon(surface, color, pos, angle):
    size = 20  # Size of hexagon
    points = []
    for i in range(6):
        x = size * math.cos(math.radians(angle + i * 60)) + pos[0]
        y = size * math.sin(math.radians(angle + i * 60)) + pos[1]
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    shape_add_counter += 1
    if shape_add_counter >= shape_add_interval:
        shape_add_counter = 0
        hexagons.append({'pos': [width // 2, 0], 'angle': 0, 'radius': 50, 'rotation_angle': 0})

    # Update and draw hexagons
    for hexagon in hexagons:
        hexagon['angle'] += 0.05
        hexagon['rotation_angle'] += 2  # Spin the hexagon
        hexagon['pos'][0] = width // 2 + hexagon['radius'] * math.cos(hexagon['angle'])
        hexagon['pos'][1] += hexagon_speed
        draw_hexagon(screen, yellow, hexagon['pos'], hexagon['rotation_angle'])

        if hexagon['pos'][1] > height:
            hexagons.remove(hexagon)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

