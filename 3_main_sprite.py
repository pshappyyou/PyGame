import pygame

pygame.init()

#screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# display title
pygame.display.set_caption("DP Game")

# background
#background = pygame.image.load("E:\\Pycharm\\pygame\\background.png")
background = pygame.image.load("E:/Pycharm/pygame/background.png")

# Character loading
character = pygame.image.load("E:\\Pycharm\\pygame\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2) # middle
character_y_pos = screen_height - character_height

#Event loop
running = True # is this game running?
while running:
    for event in pygame.event.get(): # what event happened?
        if event.type == pygame.QUIT: # close event occurred?
            running = False #is game running?

    #screen.fill((0,0,255))
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

# finish pygame
pygame.quit()
