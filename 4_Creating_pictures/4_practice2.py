import pygame
from pygame.draw import *
import random as rn

pygame.init()
width = 1500
height = 900
FPS = 30
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('КРАТРИНА НА ВЫСТАВКУ')
clock = pygame.time.Clock()
# background
rect(screen, (180, 210, 255), (0, 0, width, height / 2.3))  # sky
rect(screen, (50, 50, 255), (0, height - height / 1.7, width, height / 3.9))  # sea
rect(screen, (155, 155, 35), (0, height - height / 3, width, height / 3))  # beach
circle(screen, (255, 255, 0), (width / 1.1, height / 10), height / 11)  # sun


def cloud(x_gan=7, y_gan=15, dia_gan=30):
    """ make cloud """
    ab_cloud_span = int(width / x_gan)
    y_cloud_span = int(height / y_gan)
    dia = height / dia_gan
    delta = int(dia)
    for j in range(2):
        for i in range(5):
            x = rn.randint(ab_cloud_span, ab_cloud_span + delta)
            y = rn.randint(y_cloud_span, y_cloud_span + delta)
            circle(screen, (199, 199, 200), (x, y), dia + 2)
            circle(screen, (255, 255, 255), (x, y), dia)
            ab_cloud_span += delta
        if j == 1:
            circle(screen, (200, 200, 200), (x + delta / 1.5, y - delta / 3), dia + 2)
            circle(screen, (255, 255, 255), (x + delta / 1.5, y - delta / 3), dia)
        ab_cloud_span = int(width / x_gan)
        y_cloud_span += delta

cloud()
cloud(2,18,22)
pygame.display.update()
finished = True
while finished:
    clock.tick(FPS)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False

pygame.quit()
