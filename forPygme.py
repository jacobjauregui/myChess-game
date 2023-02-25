import pygame as pg
import sys
import time as tm
import random as rd
import interface as itf

cl=itf.Colors()

size = (800, 800)
screen = pg.display.set_mode(size)
pg.display.set_caption('Chess')
clock = pg.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    for i in range(60):
        x = rd.randint(0, 800)
        y = rd.randint(0, 800)
        pg.draw.circle(screen, cl.blood, (x, y), 10)
    screen.fill(cl.white)
    pg.display.flip()
    clock.tick(30)

