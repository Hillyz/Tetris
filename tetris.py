from pygameGlobals import *
import sys

#Class for a single block, will be used to make shapes later
class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((cellsize, cellsize))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (win_x//2, win_y//20)
        self.x = x
        self.y = y
        self.vel_y = win_y//20
        self.vel_x = win_x//10


    def move_down(self):
        blocklst = []
        #Block moves downwards naturally
        if fpsCounter % 100 == 0 and self.rect.y < win_y - win_y//20:
            self.rect.y += self.vel_y
        else:
            self.rect.y = win_y - win_y//20

    def move_right(self):
        if self.rect.x < win_x - win_x//10:
            self.rect.x += self.vel_x
        else:
            self.rect.x = win_x -win_x//10

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.vel_x
        else:
            self.rect.x = 0

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
    locked_blocks = []
    all_sprites = pg.sprite.Group()
    all_sprites.add(block)

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
            #block.draw()
            block.move_down()
            if keys[pg.K_RIGHT]:
                block.move_right()
            if keys[pg.K_LEFT]:
                block.move_left()

            #if block.checkCollision(locked_blocks):
                #locked_blocks.append(block)
                #blocks.remove(block)

        if block.y > win_y - win_y//10:
            locked_blocks.append(block)
            blocks.remove(block)
            blocks.append(Block((win_x//2 - win_x//10), win_y//20))



        for block in locked_blocks:
            pass
            #block.draw()

        all_sprites.update()

        all_sprites.draw(SCREEN)

        clock.tick(FPS)
        fpsCounter += 1
        pg.display.update()


main()
