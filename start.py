import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
BG_COLOR = (0, 0, 0)

# Load assets
CUSTOM_FONT = "spacegeometryfont.otf"
BACKGROUND_IMAGE = "background.png"
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
font = pygame.font.Font(font_path, 48)

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
def main():
    clock = pygame.time.Clock()
    floating_images = create_floating_images(25)
    start_game = False

    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True

        screen.blit(background, (0, 0))

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

    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    # PLACEHOLDER FOR THE NEXT SCREEN
    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    #           LOOK HERE
    screen.fill(BG_COLOR)
    draw_text("game has started!", font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()
    pygame.quit()
