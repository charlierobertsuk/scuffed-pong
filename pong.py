import pygame, random, sys # importing pygame for game stuff, random for random intagers, and sys to exit
clock = pygame.time.Clock() # clock for fps
pygame.display.set_caption("Pong") # game with cool 'pong' title
pygame.init() # initiates the game

blue = (0, 0, 255) # this is the colour blue
red = (255, 0, 0) # this is the colour red
kyle = ("#987654") # this is Kyle's hex code :)

width, height = 1000, 500 # width and height for refering to position of surfboards and ball
screen = pygame.display.set_mode((1000,500)) # welcome to my screen

surfboard_scale = 2 # default scale for surfboard
surfboard_multiplier = 5 # multiplier to increace surfboard size in all dimention

surfboard_x = surfboard_scale * surfboard_multiplier # the x axis need to be smaller than the y axis
surfboard_y = surfboard_scale * (surfboard_multiplier * 5) # the y axis has to be bigger than the x axis

red_surfboard = pygame.Rect(920, (height // 2), surfboard_x, surfboard_y) # red surfboard on the right
blue_surfboard = pygame.Rect(80, (height // 2), surfboard_x, surfboard_y) # blue surfboard on the left

while True: # game loop - anything that updates goes in here :)
    for event in pygame.event.get(): # when game run:
        if event.type == pygame.QUIT: # if quit then quit
            pygame.quit() # pygame quit
            sys.exit() # sys quit - all game go poof

    screen.fill(kyle) # background of Kyle's hex code

    pygame.draw.rect(screen, blue, blue_surfboard) # draws blue board
    pygame.draw.rect(screen, red, red_surfboard) # draws red board





    pygame.display.update() # updates the screen
    clock.tick(60) # fps - set to 60 fps as default
