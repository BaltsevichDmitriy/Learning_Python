import turtle as t
import math


def spiral():
    """Рисует спираль с N кольцами"""
    t.color('green', 'green')
    t.speed(0)
    radius = 0
    ring_total = 10
    ring_total_n = 0
    ring = 360
    ring_now = 0
    think = 20
    while ring_total != ring_total_n:
        ring_now = 0
        angl = 0
        ring_total_n += 1
        while ring != ring_now:
            x = radius * math.cos(math.radians(angl))
            y = radius * math.sin(math.radians(angl))
            # x1 = radius * math.cos(math.radians(angl + 1))
            # y1 = radius * math.sin(math.radians(angl + 1))
            t.goto(x, y)
            ring_now += 1
            angl += 1
            radius += think / 360


spiral()
