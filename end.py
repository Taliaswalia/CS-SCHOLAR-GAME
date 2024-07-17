import pygame
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
BG_COLOR = (0, 0, 0)
PLAYER_SCORE = 12345  # Example score

# Load assets
CUSTOM_FONT = "spacegeometryfont.otf"
ROBOTO = "Roboto-Light.ttf"
BACKGROUND_IMAGE = "background.png"
LOGO_IMAGE = "gameover.png"
LOGO_WIDTH = 450

# Button Colors
BUTTON_COLORS = [(56, 93, 109), (53, 80, 112), (81, 85, 117), (109, 89, 122), (181, 101, 118)]
BUTTON_ALPHA = 128  # Transparency level (0-255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load custom assets
background = pygame.image.load(BACKGROUND_IMAGE).convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
logo_original = pygame.image.load(LOGO_IMAGE).convert_alpha()

# Resize logo image
logo_height = int(LOGO_WIDTH / logo_original.get_width() * logo_original.get_height())
logo = pygame.transform.scale(logo_original, (LOGO_WIDTH, logo_height))

# Load custom font
font_path = os.path.join(os.path.dirname(__file__), CUSTOM_FONT)
roboto_path = os.path.join(os.path.dirname(__file__), ROBOTO)
font = pygame.font.Font(font_path, 48)
button_font = pygame.font.Font(font_path, 36)
score_font = pygame.font.Font(font_path, 48)

# Function to draw text in the center of the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to create a button with a translucent background
def draw_button(text, font, color, surface, x, y, width, height, bg_color):
    button_rect = pygame.Surface((width, height), pygame.SRCALPHA)
    button_rect.fill((*bg_color, BUTTON_ALPHA))
    surface.blit(button_rect, (x - width // 2, y - height // 2))
    draw_text(text, font, color, surface, x, y)
    return pygame.Rect(x - width // 2, y - height // 2, width, height)

# Function to show the credits page
def show_credits():
    custom_credits_font = pygame.font.Font(font_path, 48)
    credits_font = pygame.font.Font(roboto_path, 36)
    credits = [
        "CREDITS",
        "Game Developers: Group 3",
        "Music: Mike Taylor",
        "Artwork: Jane Doe",
        "Special Thanks: John Smith",
        "Special Thanks: Jane Doe",
        "Special Thanks: John Smith",
        "Special Thanks: Jane Doe",
        "Special Thanks: John Smith",
        "Special Thanks: Jane Doe",
        "Special Thanks: John Smith",
        "Special Thanks: Jane Doe",
    ]
    credits_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    credits_overlay.fill((0, 0, 0, 100))
    screen.blit(credits_overlay, (0, 0))

    credit_y = SCREEN_HEIGHT

    while credit_y > -len(credits) * 50:
        screen.blit(credits_overlay, (0, 0))
        for i, line in enumerate(credits):
            y_pos = credit_y + i * 50
            if i == 0:
                draw_text(line, custom_credits_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, y_pos)
            else:
                draw_text(line, credits_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, y_pos)

        close_button = draw_button("Close", button_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 200, 50, BUTTON_COLORS[4])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if close_button.collidepoint(event.pos):
                        return True

        credit_y -= 1  # Speed of scrolling
        pygame.time.wait(10)  # Delay to control speed

    return True

# Function to show the scores page
def show_scores():
    scores_font = pygame.font.Font(font_path, 36)
    scores = [
        "HIGH SCORES",
        "Player 1: 5000",
        "Player 2: 4500",
        "Player 3: 4000",
    ]
    scores_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    scores_overlay.fill((0, 0, 0, 180))
    screen.blit(scores_overlay, (0, 0))

    for i, line in enumerate(scores):
        draw_text(line, scores_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, 100 + i * 50)

    close_button = draw_button("Close", button_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 200, 50, BUTTON_COLORS[3])
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if close_button.collidepoint(event.pos):
                        waiting = False
    return True

# Main loop
def main():
    clock = pygame.time.Clock()
    button_y_start = 315
    button_spacing = 60

    while True:
        screen.blit(background, (0, 0))

        screen.blit(logo, (SCREEN_WIDTH // 2 - logo.get_width() // 2, 50))

        # Display player score
        draw_text(f"Score: {PLAYER_SCORE}", score_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, 215)

        buttons = [
            ("Return to Menu", lambda: None, BUTTON_COLORS[1]),
            ("Credits", show_credits, BUTTON_COLORS[0]),
            ("Scores", show_scores, BUTTON_COLORS[2])
        ]

        for i, (text, action, color) in enumerate(buttons):
            y_pos = button_y_start + i * button_spacing
            button_rect = draw_button(text, button_font, (255, 255, 255), screen, SCREEN_WIDTH // 2, y_pos, 250, 50, color)
            buttons[i] = (button_rect, action)

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button_rect, action in buttons:
                        if button_rect.collidepoint(event.pos):
                            if not action():
                                return

if __name__ == "__main__":
    main()
    pygame.quit()
