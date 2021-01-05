import pygame
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

# Event loop
running = True  # is this game running?
while running:
    dt = clock.tick(30)  # set up frame per second

    # 2. Event handle
    for event in pygame.event.get():  # what event happened?
        if event.type == pygame.QUIT:  # close event occurred?
            running = False  # is game running?

    # 3. Game character position

    # 4. Collision handle

    pygame.display.update()

pygame.quit()
