import pygame
screenWidth = 700
screenHeight = 600
class Health_Bar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Health_Bar, self).__init__()
        self.surf = pygame.Surface((100, 20))  # Placeholder for health bar
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.health = 50

    def update(self, health):
        self.health = health
        self.surf.fill((191, 29, 29))  # Red color for health bar background
        pygame.draw.rect(self.surf, (32, 128, 57), (0, 0, self.health*2, 20))  # Green part of the health bar# import pygame
