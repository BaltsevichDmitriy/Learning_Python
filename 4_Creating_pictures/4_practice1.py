import pygame
from pygame.draw import *

FPS = 30
width = 900
height = 700
dia = 400
delta_up = height / 10
delta_up2 = height / 10 - 10
eye_horizontal = 155
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen.fill([100, 200, 200])
clock = pygame.time.Clock()
circle(screen, (255, 255, 0), (width / 2, height / 2 - delta_up), dia / 2)
rect(screen, (5, 5, 5), (width / 2 - dia / 4.41, height / 2 + dia / 4.5 - delta_up, dia / 2.2, dia / 10))
circle(screen, (233, 0, 0), (width / 2 - dia / 4, height / 2 - dia / 6 - delta_up), dia / 12)
circle(screen, (0, 0, 0), (width / 2 - dia / 4, height / 2 - dia / 6 - delta_up), dia / 30)
circle(screen, (233, 0, 0), (width / 2 + dia / 4, height / 2 - dia / 6 - delta_up), dia / 16)
circle(screen, (0, 0, 0), (width / 2 + dia / 4, height / 2 - dia / 6 - delta_up), dia / 30)
polygon(screen, (0, 0, 3), [(width / 2 - dia / 7.5, height / 2 - dia / 5.36 - delta_up),
                            (width / 2 - dia / 9.375, height / 2 - dia / 4.41 - delta_up),
                            (width / 2 - dia / 2, height / 2 - dia / 2.04 - delta_up),
                            (width / 2 - dia / 1.897, height / 2 - dia / 2.222 - delta_up)])
polygon(screen, (0, 0, 3), [(width / 2 + dia / 7.5, height / 2 - dia / 5.36 - delta_up),
                            (width / 2 + dia / 9.375, height / 2 - dia / 4.41 - delta_up),
                            (width / 2 + dia / 2 - dia / 20, height / 2 - dia / 2.04 - delta_up + dia / 7),
                            (width / 2 + dia / 1.897 - dia / 20, height / 2 - dia / 2.222 - delta_up + dia / 7)])
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
