# This is pong

# Import
import pygame, sys

# Screen size
screen_width = 1000
screen_height = 500
half_width = screen_width // 2
half_height = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))

# Pygame Title
pygame.display.set_caption("Pong")

# Clock
clock = pygame.time.Clock()

# Initiate the pygame
pygame.init()

# State colours
KYLE = (152, 118, 84)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
PINK = (255, 255, 255)

# Surfboard variables
surf_x = 15
surf_y = surf_x * 6

# Right surfboard
right_surfboard = pygame.Rect(900, 200, surf_x, surf_y)

# Right surfboard margin - so I can control collisions with a single axis and not just with whe surfboard - prevents ball entering surfboard from top and bouncing through
top_right_surfboard = pygame.Rect(900, 200, surf_x, 2)
bottom_right_surfboard = pygame.Rect(900, 200 + (surf_y - 2), surf_x, 2)
left_right_surfboard = pygame.Rect(900, 200, 2, surf_y)
right_right_surfboard = pygame.Rect(900 + surf_x, 200, 2, surf_y)

# Left surfboard
left_surfboard = pygame.Rect(100, 200, surf_x, surf_y)

# Left surfboard margin
top_left_surfboard = pygame.Rect(100, 200, surf_x, 2)
bottom_left_surfboard = pygame.Rect(100, 200 + (surf_y - 2), surf_x, 2)
left_left_surfboard = pygame.Rect(100, 200, 2, surf_y)
right_left_surfboard = pygame.Rect(100 + surf_x, 200, 2, surf_y)

#NOTE: Make left margin and make all margins move with the surfboard then after that, sort collisions :)

# Ball variables
ballsize = 20
ballspeed = 5
ballspeed_x = ballspeed
ballspeed_y = ballspeed
ball = pygame.Rect(half_width, half_height, ballsize, ballsize)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keybinds
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        if left_surfboard.y - 5 >= 0: # if surfboard y coordinate more than 0
            left_surfboard.y -= 5
            top_left_surfboard.y -= 5
            bottom_left_surfboard.y -= 5
            left_left_surfboard.y -= 5
            right_left_surfboard.y -= 5
    
    if key[pygame.K_s]:
        if left_surfboard.y + 5 <= screen_height - surf_y: # surf_y is so it dosen't go thru floor cos surfboard collides at top
            left_surfboard.y += 5
            top_left_surfboard.y += 5
            bottom_left_surfboard.y += 5
            left_left_surfboard.y += 5
            right_left_surfboard.y += 5

    if key[pygame.K_UP]:
        if right_surfboard.y - 5 >= 0: # if surfboard y coordinate less than 0
            right_surfboard.y -= 5
            top_right_surfboard.y -= 5
            bottom_right_surfboard.y -= 5
            left_right_surfboard.y -= 5
            right_right_surfboard.y -= 5

    if key[pygame.K_DOWN]:
        if right_surfboard.y + 5 <= screen_height - surf_y: # surf_y is so it dosen't go thru floor cos surfboard collides at top
            right_surfboard.y += 5
            top_right_surfboard.y += 5
            bottom_right_surfboard.y += 5
            left_right_surfboard.y += 5
            right_right_surfboard.y += 5

    # Move the ball
    ball.x += ballspeed_x
    ball.y += ballspeed_y

    # Wall colision check
    if ball.top <= 0 or ball.bottom >= screen_height: # if ball hits top or bottom of screen
        ballspeed_y = -ballspeed_y # move in oppisite y direction

    if ball.left <= 0 or ball.right >= screen_width: # if ball hits left or right of screen
        ballspeed_x = -ballspeed_x # move in oppisite x direction

    # Surfboard collision check x
    if ball.colliderect(right_left_surfboard or left_left_surfboard) or ball.colliderect(left_right_surfboard or right_right_surfboard):
        ballspeed_x = -ballspeed_x

    # Surfboard colision check y - if ball hits top or bottom of surfboard then bounce NOTE: Dosen't work yet :(
    if ball.colliderect(top_left_surfboard or bottom_left_surfboard) or ball.colliderect(top_right_surfboard or bottom_right_surfboard):
        ballspeed_y = -ballspeed_y

    # Background colour
    screen.fill(WHITE)

    # Draw surfboards
    pygame.draw.rect(screen, BLUE, left_surfboard)
    pygame.draw.rect(screen, RED, right_surfboard)

    # Draw right surfboard margin
    pygame.draw.rect(screen, BLACK, top_right_surfboard)
    pygame.draw.rect(screen, BLACK, bottom_right_surfboard)
    pygame.draw.rect(screen, BLACK, left_right_surfboard)
    pygame.draw.rect(screen, BLACK, right_right_surfboard)

    # Draw left surfboard margin
    pygame.draw.rect(screen, BLACK, top_left_surfboard)
    pygame.draw.rect(screen, BLACK, bottom_left_surfboard)
    pygame.draw.rect(screen, BLACK, left_left_surfboard)
    pygame.draw.rect(screen, BLACK, right_left_surfboard)

    # Draw ball
    pygame.draw.circle(screen, KYLE, (ball.x, ball.y), 10, 10)

    # Display update
    pygame.display.update()

    # Set game fps
    clock.tick(60)

    # NOTE: Colour array for when a ball hits a wall (background change) or a surfboard (ball change)
