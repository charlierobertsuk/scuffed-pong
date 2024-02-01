# This is pong

# Import
import pygame, sys, random

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
PINK = ("pink")
PURPLE = (99, 3, 48)
DARKGREEN = (1, 50, 32)
ORANGE = (255, 68, 51) 

# Colour change on colision variables
background_colour_change = [KYLE, PURPLE, GREEN, YELLOW]
ball_colour_change = [AQUA, DARKGREEN, ORANGE, PINK]
i = 0
j = 0

# Surfboard variables
surf_x = 15
surf_y = surf_x * 6

# Right surfboard
right_surfboard = pygame.Rect(900, 200, surf_x, surf_y)

# Right surfboard margin - so I can control collisions with a single axis and not just with whe surfboard - prevents ball entering surfboard from top and bouncing through
top_right_surfboard = pygame.Rect(900, 200, surf_x, 2)
bottom_right_surfboard = pygame.Rect(900, 200 + (surf_y - 2), surf_x, 2)

# Left surfboard
left_surfboard = pygame.Rect(100, 200, surf_x, surf_y)

# Left surfboard margin
top_left_surfboard = pygame.Rect(100, 200, surf_x, 2)
bottom_left_surfboard = pygame.Rect(100, 200 + (surf_y - 2), surf_x, 2)

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
    
    if key[pygame.K_s]:
        if left_surfboard.y + 5 <= screen_height - surf_y: # surf_y is so it dosen't go thru floor cos surfboard collides at top
            left_surfboard.y += 5
            top_left_surfboard.y += 5
            bottom_left_surfboard.y += 5

    if key[pygame.K_UP]:
        if right_surfboard.y - 5 >= 0: # if surfboard y coordinate less than 0
            right_surfboard.y -= 5
            top_right_surfboard.y -= 5
            bottom_right_surfboard.y -= 5

    if key[pygame.K_DOWN]:
        if right_surfboard.y + 5 <= screen_height - surf_y: # surf_y is so it dosen't go thru floor cos surfboard collides at top
            right_surfboard.y += 5
            top_right_surfboard.y += 5
            bottom_right_surfboard.y += 5

    # Move the ball
    ball.x += ballspeed_x
    ball.y += ballspeed_y

    # Colour change loop
    if i != 3:

        # Wall colision check
        if ball.top <= 0 or ball.bottom >= screen_height: # if ball hits top or bottom of screen
            ballspeed_y = -ballspeed_y # move in oppisite y direction
            i += 1
            if i == 3:
                i = 0

        if ball.left <= 0 or ball.right >= screen_width: # if ball hits left or right of screen
            ballspeed_x = -ballspeed_x # move in oppisite x direction
            i += 1
            if i == 3:
                i = 0

        # Background colour
        screen.fill(background_colour_change[i])

    if j != 3:

        #shape = random.randint (1, 3)
        shape = 2
        if shape == 1:
            # Draw ball (circle)
            pygame.draw.circle(screen, ball_colour_change[i], (ball.x, ball.y), 10, 10) #NOTE: Ball collides half way when left colision - pls fix

        if shape == 2:
            # Draw ball (square)
            pygame.draw.rect(screen, ball_colour_change[j], ball)

        if shape == 3:
            # Draw ball (triangle)
            pygame.draw.polygon(screen, ball_colour_change[j], ((25,75),(320,125),(250,375)))

    # Surfboard collision check x
    if ball.colliderect(left_surfboard or left_surfboard) or ball.colliderect(right_surfboard or right_surfboard):
        ballspeed_x = -ballspeed_x
        j +=1
        if j == 3:
            j = 0

    # Surfboard colision check y - if ball hits top or bottom of surfboard then bounce NOTE: Dosen't work yet :(
    if ball.colliderect(top_left_surfboard or bottom_left_surfboard) or ball.colliderect(top_right_surfboard or bottom_right_surfboard):
        ballspeed_y = -ballspeed_y
        j += 1
        if j == 3:
            j = 0
    
# NOTE: fix if statement

    # Draw surfboards
    pygame.draw.rect(screen, BLUE, left_surfboard)
    pygame.draw.rect(screen, RED, right_surfboard)

    # Draw right surfboard margin
    pygame.draw.rect(screen, RED, top_right_surfboard)
    pygame.draw.rect(screen, RED, bottom_right_surfboard)

    # Draw left surfboard margin
    pygame.draw.rect(screen, BLUE, top_left_surfboard)
    pygame.draw.rect(screen, BLUE, bottom_left_surfboard)

    # Display update
    pygame.display.update()

    # Set game fps
    clock.tick(60)

