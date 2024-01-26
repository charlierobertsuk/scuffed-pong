import pygame, random, sys
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

pygame.init()


screen = pygame.display.set_mode((1000,500))
colour = (255, 0, 0)
pygame.draw.rect(screen, colour, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#987654")

    pygame.display.update()
    clock.tick(60) # fps - set to 60 fps as default
