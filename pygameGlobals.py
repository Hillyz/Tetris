<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
import pygame as pg

pg.init()
pg.mixer.init()
clock = pg.time.Clock()
FPS = 60
fpsCounter = 0
win_x = 300
win_y = 600
SCREEN = pg.display.set_mode((win_x, win_y))
pg.display.set_caption("Tetris")
cellsize = win_x//10
BLACK = (0,0,0)
