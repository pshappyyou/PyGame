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
to_x = 0
to_y = 0

#Event loop
running = True # is this game running?
while running:
    for event in pygame.event.get(): # what event happened?
        if event.type == pygame.QUIT: # close event occurred?
            running = False #is game running?

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: # stop when hand off key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #screen.fill((0,0,255))
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

# finish pygame
pygame.quit()
