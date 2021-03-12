import pygame
from pygame.draw import *
import random as rn

pygame.init()
width = 1900
height = 1000
FPS = 30
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('КРАТРИНА НА ВЫСТАВКУ')
clock = pygame.time.Clock()
# background
rect(screen, (180, 210, 255), (0, 0, width, height / 2.3))  # sky
rect(screen, (50, 50, 255), (0, height - height / 1.7, width, height / 3.9))  # sea
rect(screen, (155, 155, 35), (0, height - height / 3, width, height / 3))  # beach
circle(screen, (255, 255, 0), (width / 1.1, height / 10), height / 11)  # sun


def draw_cloud(x_gan=7, y_gan=15, dia_gan=15, delta_dia=1):
    """ make cloud """
    ab_cloud_span = int(width / x_gan)
    y_cloud_span = int(height / y_gan)
    dia = int(height / dia_gan)
    delta = int((dia + delta_dia) / 2)
    for j in range(2):
        for i in range(5):
            x = rn.randint(ab_cloud_span, ab_cloud_span + delta)
            y = rn.randint(y_cloud_span, y_cloud_span + delta)
            ellipse(screen, (159, 159, 200), [x, y, dia + delta_dia + 2, dia + 2])
            ellipse(screen, (255, 255, 255), [x, y, dia + delta_dia, dia])
            ab_cloud_span += delta
        if j == 1:
            ellipse(screen, (199, 199, 200), [x, y, dia + delta_dia + 2, dia + 2])
            ellipse(screen, (255, 255, 255), [x, y, dia + delta_dia, dia])
        ab_cloud_span = int(width / x_gan)
        y_cloud_span += delta - delta_dia


def draw_boat(x_start=width / 2, y_start=height / 2, size=2):
    rect(screen, (115, 77, 5), (x_start*0.8, y_start*0.98, x_start/size*0.8,y_start/size/3.3))
    circle(screen, (115, 77, 5), (x_start*0.8, y_start*0.98), y_start/size/3.3)
    rect(screen, (50, 50, 255), (x_start*0.5, y_start*0.83, x_start/size,y_start/size/3.3))


draw_cloud()
draw_cloud(3, 18, 11, 42)
draw_boat()
pygame.display.update()
finished = True
while finished:
    clock.tick(FPS)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False

pygame.quit()
