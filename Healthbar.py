import pygame
screenWidth = 700
screenHeight = 600
class Health_Bar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Health_Bar, self).__init__()
        self.surf = pygame.Surface((100, 20))  # Placeholder for health bar
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.health = 100

    def update(self, health):
        self.health = health
        self.surf.fill((255, 0, 0))  # Red color for health bar background
        pygame.draw.rect(self.surf, (0, 255, 0), (0, 0, self.health, 20))  # Green part of the health bar# import pygame
 
# class Health_Bar(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.surf = pygame.Surface((100, 40))
#         Heart1 = ("full_heart.png")
#         Heart2 = ("half_heart.png")
#         self.health = [Heart1, Heart2]
#         pygame.surf.load (self.health)
#         pygame.bli
#         self.surf = self.health[0]
        


#     def update(self):
#         for heart in self.health:
#             if lives <= 2:
#                 self.health.pop (heart)
#                 lives = 2
