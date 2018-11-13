import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]

BLOCK_WIDTH = 55
BLOCK_HEIGHT = 25
TOTAL_BLOCK = 6
BLOCK_POSITION = [53,60]
BLOCK_ROW = 5
BLOCK_COLUMN = 6
BLOCK_SPACING = 5

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 30
PADDLE_POSITION = [200, 700]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    #Create Blocks
    x = BLOCK_POSITION[0]
    y = BLOCK_POSITION[1]
    
    for i in range(BLOCK_ROW):
        for j in range(BLOCK_COLUMN):
            rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            block = KineticBlock(Vector2(x, y), BLOCK_WIDTH, BLOCK_HEIGHT, rand_color)

            object_list.append(block)
            x += BLOCK_WIDTH + BLOCK_SPACING
        x = BLOCK_POSITION[0]
        y += BLOCK_HEIGHT + BLOCK_SPACING

    #Create Paddle
    paddle = Paddle(Vector2(PADDLE_POSITION), PADDLE_WIDTH, PADDLE_HEIGHT, [255, 255, 255])
    object_list.append(paddle)

  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left=left, right=right)
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
