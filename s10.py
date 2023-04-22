import pygame
pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CUSTOM_COLOR = (160, 38, 173)
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pos_x = 0
pos_y = 0
pos_x_change = 1
pos_y_change = 1

done = True
# ------------ Main Program Loop -------------
while done:
    # ------------ Main event loop ------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         done = False

    # ------------ Game logic should go here ------------

    # ------------ Drawing code should go here ------------
    # screen.fill(WHITE)
    # pygame.draw.rect(screen, CUSTOM_COLOR, [0,0, 10,10])
    # pygame.draw.line(screen, BLACK, [0, 0], [300, 300])
    # pygame.draw.lines(screen, CUSTOM_COLOR, False, [[0, 0], [100, 100], [10,200]])
    # pygame.draw.ellipse(screen, (255,0,0), [100,100,100,100], 3)
    # pygame.draw.circle(screen, (255, 0, 0), [
    #                    100, 100], 100 ,False, False, False, True)
    # pygame.draw.circle(screen, CUSTOM_COLOR, [
    #                    100, 100], 100, False, True, False, False)
    # pygame.draw.circle(
    #     screen, BLACK, [100, 100], 100, False, False, True, False)
    # pygame.draw.polygon(screen, BLACK, [[0, 200], [100, 100], [200, 200]],7)
    pygame.draw.ellipse(screen, CUSTOM_COLOR, [pos_x, pos_y, 10, 10])
    pos_x += pos_x_change
    pos_y += pos_y_change
    # todo add bouncing

    # update the screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
