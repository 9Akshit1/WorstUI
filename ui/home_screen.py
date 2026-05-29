import pygame
import random

pygame.init()

# Screen Setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colours
ORANGE = (255, 165, 0)

# Game loop control
running = True
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sky
    screen.fill(ORANGE)

    # Button
    # Coordinates and size: (x, y, width, height)
    my_rect = (50, 50, 150, 100)
    red = (255, 0, 0)

    # Draw the rectangle
    pygame.draw.rect(screen, red, my_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
