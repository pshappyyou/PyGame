import pygame

pygame.init()

#screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# display title
pygame.display.set_caption("DP Game")

#FPS
clock = pygame.time.Clock()

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

# moving coordination
to_x = 0
to_y = 0

#character speed
character_speed = 0.5

# Enemy character
enemy = pygame.image.load("E:\\Pycharm\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width /2) # middle
enemy_y_pos = (screen_height /2) - (character_height/2)


#Event loop
running = True # is this game running?
while running:
    dt = clock.tick(60) # set up frame per second

   # print("fps:" + str(clock.get_fps()))

    for event in pygame.event.get(): # what event happened?
        if event.type == pygame.QUIT: # close event occurred?
            running = False #is game running?

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # stop when hand off key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #collision handle
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #collide check
    if character_rect.colliderect(enemy_rect):
        print("Collide!!")
        running = False


    #screen.fill((0,0,255))
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # enemy display
    pygame.display.update()

# finish pygame
pygame.quit()
