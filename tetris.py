from pygameGlobals import *
import sys

#Class for a single block, will be used to make shapes later
class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((cellsize, cellsize))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (win_x//2, 0)
        self.vel_y = win_y//20
        self.vel_x = win_x//10


    def move_down(self):
        #Block moves downwards naturally
        if self.rect.y < win_y - win_y//20 :
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


    def collision(self, group2):
<<<<<<< Updated upstream
        collision = pg.sprite.spritecollide(self, group2, True)
=======
        collision = pg.sprite.spritecollide(self, group2, False, )
>>>>>>> Stashed changes
        if collision:
            return True

#Child class, consists of blocks
class Tetrimino(Block):
    def __init__(self):
        pass




#draws a grid to show possible block movement
<<<<<<< Updated upstream
#TAKES TOO MUCH TIME TO DRAW EACH FRAME, FIND SOLOUTION
def drawGrid():
    cellsize = win_x//10
    gridlst = []
    for x in range(win_x):
        for y in range(win_y):
            rect = pg.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
            gridlst.append(rect)
            #pg.draw.rect(SCREEN, (200, 200, 200), rect, 1)
    return gridlst


=======
def drawGrid():
    for x in range(0,win_x, win_x//10):
        pg.draw.line(SCREEN, (200, 200, 200), (x, 0), (x, win_y))
    for y in range(0, win_y, win_y//20):
        pg.draw.line(SCREEN, (200, 200, 200), (0, y), (win_x, y))
>>>>>>> Stashed changes


def main():
    #local variables
    run = True
    block = Block()
    fpsCounter = 0
    movement_delay = 0
<<<<<<< Updated upstream
    live_blocks = pg.sprite.Group()
    dead_blocks = pg.sprite.Group()
    live_blocks.add(block)
    gridlst = drawGrid()
=======
    insta_delay = 0
    live_blocks = pg.sprite.Group()
    dead_blocks = pg.sprite.Group()
    live_blocks.add(block)
>>>>>>> Stashed changes

#Game loop
    while run:
        #Run game at certain fps
        clock.tick(FPS)
        fpsCounter += 1

        #Event check for quit
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

        #Block movement
        for block in live_blocks:
            movement_delay += 1
<<<<<<< Updated upstream
=======
            insta_delay += 1
            #Makes sure that there is no bug because of collision
            if len(live_blocks) > 1:
                block.remove(live_blocks)

>>>>>>> Stashed changes
            #Player key input check
            if keys[pg.K_LEFT] and movement_delay % 5 == 0:
                block.move_left()
                movement_delay = 0
            if keys[pg.K_RIGHT] and movement_delay % 5 == 0:
                block.move_right()
                movement_delay = 0
            if keys[pg.K_DOWN]:
                block.move_down()
            if fpsCounter % 48 == 0:
                block.move_down()

            #Block is placed at the bottom, new block is spawned
            #Forced by player
<<<<<<< Updated upstream
            if keys[pg.K_SPACE] and movement_delay % 10 == 0:
=======
            if keys[pg.K_SPACE] and insta_delay > 0:
>>>>>>> Stashed changes
                block.rect.y = win_y - win_y//20
                dead_blocks.add(block)
                block.remove(live_blocks)
                newblock = Block()
                live_blocks.add(newblock)
<<<<<<< Updated upstream
                movement_delay = 0
=======
                insta_delay = -50
>>>>>>> Stashed changes

            #naturally by block movement
            elif block.rect.y >= win_y - win_y//20:
                dead_blocks.add(block)
                block.remove(live_blocks)
                newblock = Block()
                live_blocks.add(newblock)


<<<<<<< Updated upstream
            ## ??????
            #for block in dead_blocks:
            #    block.rect.topleft = (block.rect.x, win_y - win_y//20)

            # Checks if there is collision
            if block.collision(dead_blocks):
                print("test")
=======
            # Checks if there is collision
            if block.collision(dead_blocks):
                print("Collision", block.rect.y)
>>>>>>> Stashed changes
                dead_blocks.add(block)
                block.remove(live_blocks)
                newblock = Block()
                live_blocks.add(newblock)
<<<<<<< Updated upstream
=======
                ## ??????
                block.rect.topleft = (block.rect.x, block.rect.y - win_y//20)
                #for block in dead_blocks:
                #    block.rect.topleft = (block.rect.x, block.rect.y - win_y//20)
>>>>>>> Stashed changes

        #Update
        live_blocks.update()
        dead_blocks.update()

        #Draw / render
        SCREEN.fill(BLACK)
        live_blocks.draw(SCREEN)
        dead_blocks.draw(SCREEN)
<<<<<<< Updated upstream
=======
        drawGrid()
>>>>>>> Stashed changes

        #Flip display
        pg.display.update()


main()
