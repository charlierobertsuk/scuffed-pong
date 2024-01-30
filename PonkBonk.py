# welcome to PonkBonk

# imports
import pygame, random, sys

# basically window setup
pygame.display.set_caption("Pong But It's Kyle")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500

pygame.init()

# variables
screen = pygame.display.set_mode((screen_width, screen_height))
redsize = 15
bluesize = 15
ballwidth = 20
ballradius = 10
redsquare = pygame.Rect(920, 200, redsize, redsize * 6)
bluesquare = pygame.Rect(80, 200, bluesize, bluesize * 6)
ball = pygame.Rect(screen_width // 2, screen_height // 2, ballwidth, ballradius)
ball_speed_x = 5  # ball x axis speed
ball_speed_y = 5  # ball y axis speed
RED = (255, 0, 0) # so this is red
BLUE = (0, 0, 255) # belive it or not, this is bluee
PINK = (255, 0, 255) # i decided pink was a good idea
BLACK = (0, 0, 0) # like the oppisite of colour
KYLE = ("#987654") # we love Kyle

# game loop
while True: # game loop - anything that updates goes in here :)
    for event in pygame.event.get(): # when game run:
        if event.type == pygame.QUIT: # if quit then quit
            pygame.quit() # pygame quit
            sys.exit() # sys quit - all game go poof

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if bluesquare.y - 5 >= 0:
            bluesquare.y -= 5
    if key[pygame.K_s]:
        if bluesquare.y + 5 <= screen_height - 80:
            bluesquare.y += 5
    if key[pygame.K_UP]:
        if redsquare.y - 5 >= 0:
            redsquare.y -= 5
    if key[pygame.K_DOWN]:
        if redsquare.y + 5 <= screen_height - 80:
            redsquare.y += 5

    # update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # check for wall colisions
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x

    # check for surfboard collisions
    if ball.colliderect(bluesquare) or ball.colliderect(redsquare):
        ball_speed_x = -ball_speed_x * 1.02

    screen.fill(KYLE)
    pygame.draw.rect(screen, RED, redsquare)
    pygame.draw.rect(screen, BLUE, bluesquare)
    pygame.draw.circle(screen, (PINK), (ball.x, ball.y), ballwidth, ballradius)

    pygame.display.update()
    clock.tick(60)
