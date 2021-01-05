import pygame
import random
################################################################
# initialization

pygame.init()

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# display title
pygame.display.set_caption("DP Game")

# FPS
clock = pygame.time.Clock()
################################################################

# 1. User initialization(background, image, coordination, speed, font etc.)

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
# to_y = 0
character_speed = 0.5

# Enemy character
enemy = pygame.image.load("E:\\Pycharm\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width-enemy_width) # - (enemy_width /2) # middle
enemy_y_pos = 0

enemy_speed = 10

# Event loop
running = True  # is this game running?
while running:
    dt = clock.tick(30)  # set up frame per second

    # 2. Event handle
    for event in pygame.event.get():  # what event happened?
        if event.type == pygame.QUIT:  # close event occurred?
            running = False  # is game running?

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # stop when hand off key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. position
    character_x_pos += to_x * dt
    # character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. collision handle
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Collide!!")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
