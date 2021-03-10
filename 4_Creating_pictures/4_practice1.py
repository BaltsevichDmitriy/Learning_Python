import pygame
from pygame.draw import *


def angry_smiley(FPS=30, width=900, height=700, dia=400):
    x_center = width / 2
    y_center = height / 2 - height / 10
    eye_horizontal = 155
    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    screen.fill([100, 200, 200])
    clock = pygame.time.Clock()
    circle(screen, (255, 255, 0), (x_center, y_center), dia / 2)
    rect(screen, (5, 5, 5), (x_center - dia / 4.41, y_center + dia / 4.5, dia / 2.2, dia / 10))
    circle(screen, (233, 0, 0), (x_center - dia / 4, y_center - dia / 6), dia / 12)
    circle(screen, (0, 0, 0), (x_center - dia / 4, y_center - dia / 6), dia / 30)
    circle(screen, (233, 0, 0), (x_center + dia / 4, y_center - dia / 6), dia / 16)
    circle(screen, (0, 0, 0), (x_center + dia / 4, y_center - dia / 6), dia / 30)
    polygon(screen, (0, 0, 3), [(x_center - dia / 7.5, y_center - dia / 5.36),
                                (x_center - dia / 9.375, y_center - dia / 4.41),
                                (x_center - dia / 2, y_center - dia / 2.04),
                                (x_center - dia / 1.897, y_center - dia / 2.222)])
    polygon(screen, (0, 0, 3), [(x_center + dia / 7.5, y_center - dia / 5.36),
                                (x_center + dia / 9.375, y_center - dia / 4.41),
                                (x_center + dia / 2 - dia / 20, y_center - dia / 2.04 + dia / 7),
                                (x_center + dia / 1.897 - dia / 20, y_center - dia / 2.222 + dia / 7)])
    pygame.display.update()
    finished = True
    second = 0
    while finished:
        clock.tick(FPS)
        second += 1
        pygame.display.set_caption('Картинка со злым смайликом открыта ' + str(int(second / 30)) + ' сек.')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = False
    pygame.quit()



angry_smiley()
