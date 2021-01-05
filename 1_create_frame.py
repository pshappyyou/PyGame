import pygame

pygame.init()

#screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# display title
pygame.display.set_caption("DP Game")

#Event loop
running = True # is this game running?
while running:
    for event in pygame.event.get(): # what event happened?
        if event.type == pygame.QUIT: # close event occurred?
            running = False #is game running?

# finish pygame
pygame.quit()
