from pygameGlobals import *
import sys

#Class for a single block, will be used to make shapes later
class Block():
    def __init__(self, x, y):
        self.screen = SCREEN
        self.x = x
        self.y = y
        self.vel_y = win_y//20

    def draw(self):
        block1 = pg.Rect(self.x*cellsize, self.y*cellsize, cellsize, cellsize)
        pg.draw.rect(self.screen, (255, 0, 0), block1)
        print(block1)

    def move(self):
        #Block moves downwards naturally
        if fpsCounter % 48 == 0 and self.y < win_y:
            self.y += self.vel_y




#draws a grid to show possible block movement
def drawGrid():
    cellsize = win_x//10
    for x in range(win_x):
        for y in range(win_y):
            rect = pg.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
            pg.draw.rect(SCREEN, (200, 200, 200), rect, 1)


def main():
    run = True
    block = Block(win_x//5, win_y//20)
    fpsCounter = 0

    while run:

        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

        SCREEN.fill(BLACK)

        drawGrid()

        block.draw()

        block.move()

        fpsCounter += 1
        clock.tick(FPS)
        pg.display.update()


main()
