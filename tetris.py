from pygameGlobals import *
import sys

#Class for a single block, will be used to make shapes later
class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.screen = SCREEN
        self.x = x
        self.y = y
        self.vel_y = win_y//20
        self.vel_x = win_x//10

    def draw(self):
        rect = pg.Rect(self.x, self.y, cellsize, cellsize)
        pg.draw.rect(self.screen, (200, 0, 0), rect)

    def move_down(self):
        blocklst = []
        #Block moves downwards naturally
        if fpsCounter % 100 == 0 and self.y < win_y - win_y//20:
            self.y += self.vel_y
        else:
            self.y = win_y - win_y//20

    def move_right(self):
        if self.x < win_x - win_x//10:
            self.x += self.vel_x
        else:
            self.x = win_x -win_x//10

    def move_left(self):
        if self.x > 0:
            self.x -= self.vel_x
        else:
            self.x = 0

#Child class, consists of blocks
class Tetrimino(Block):
    def __init__(self):
        pass




#draws a grid to show possible block movement
def drawGrid():
    cellsize = win_x//10
    for x in range(win_x):
        for y in range(win_y):
            rect = pg.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
            pg.draw.rect(SCREEN, (200, 200, 200), rect, 1)


def main():
    #local variables
    run = True
    block = Block((win_x//2 - win_x//10), win_y//20)
    fpsCounter = 0
    blocks = []

    blocks.append(block)

    while run:

        #Event check for quit
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

        #Reset and draw
        SCREEN.fill(BLACK)
        drawGrid()

        #NB
        #NOT REALLY USEFUL, ONLY TEMPORARY
        for block in blocks:
            block.draw()
            block.move_down()
            if keys[pg.K_RIGHT]:
                block.move_right()
            if keys[pg.K_LEFT]:
                block.move_left()

        if block.y > win_y - win_y//10:
            blocks.append(Block((win_x//2 - win_x//10), win_y//20))



        clock.tick(FPS)
        fpsCounter += 1
        pg.display.update()


main()
