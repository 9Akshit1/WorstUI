import pygame
import random

pygame.init()

# Screen Setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colours
BLUE = (207, 226, 243)
GREEN = (0, 255, 0)

# Hole Coordinates
holes = []
hole_rects = []  # Keeps track of the physical space each hole takes up

while len(holes) < 5:
    hole_x = random.randint(50, WIDTH - 50)
    hole_y = random.randint(HEIGHT // 2 + 50, HEIGHT - 50)
    
    # Keeping the hole within bounds.
    # All holes are at least 10 pixels away from each other.
    new_rect = pygame.Rect(hole_x - 25, hole_y - 15, 50, 30)
    
    # Check if the new hole overlaps with any existing holes
    overlap = False
    for existing_rect in hole_rects:
        if new_rect.colliderect(existing_rect):
            overlap = True
            break
            
    # If it doesn't overlap, save both the coordinates and the rect
    if not overlap:
        holes.append((hole_x, hole_y))
        hole_rects.append(new_rect)

# 1. Import the image and optimize its format
new_width = 100
new_height = 60
my_image = pygame.image.load(r"C:\Users\rickh\Downloads\cloud.png").convert_alpha()
scaled_image = pygame.transform.scale(my_image, (new_width, new_height))

# Set image position coordinates (X, Y)
image_x = 100
image_y = 150

# Generate cloud positions with random speeds
# Format: [x, y, speed]
clouds = []
for i in range(3):
    cloud_x = random.randint(0, WIDTH - new_width)
    cloud_y = random.randint(0, HEIGHT // 2 - new_height)
    cloud_speed = random.uniform(1, 4)  # Random speed between 1 and 4 pixels per frame
    clouds.append([cloud_x, cloud_y, cloud_speed])

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
    screen.fill(BLUE)

    # Ground
    bottom_rect = pygame.Rect(0, HEIGHT // 2, WIDTH, HEIGHT // 2)
    pygame.draw.rect(screen, GREEN, bottom_rect)

    # The sun
    pygame.draw.circle(screen, (255, 255, 0), (WIDTH // 2 + 200, HEIGHT // 4 - 75), 50)

    # Holes
    for hole_x, hole_y in holes:
        pygame.draw.ellipse(screen, (185, 139, 94), (hole_x - 25, hole_y - 15, 50, 30))

    # Update and draw clouds
    for cloud in clouds:
        cloud[0] += cloud[2]  # Update x position based on speed
        
        # Wrap cloud around screen
        if cloud[0] > WIDTH:
            cloud[0] = -new_width
        
        screen.blit(scaled_image, (cloud[0], cloud[1]))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
