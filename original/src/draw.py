import pygame #TODO:  Fix intellisense
import random
from random import randint

from pygame.math import Vector2

from ball import *
from block import *
from paddle import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]
PADDLE_WIDTH = 70
PADDLE_HEIGHT = 16
PADDLE_SPACING = 10
PADDLE_X = SCREEN_SIZE[0] / 2
PADDLE_Y = SCREEN_SIZE[1] - (PADDLE_HEIGHT / 2) - PADDLE_SPACING
PADDLE_COLOR = [randint(64,255), randint(64,255), randint(64,255)]
BALL_RADIUS = 10
BRICKS_PER_ROW = 6
BRICKS_PER_COLUMN = 20
BRICK_WIDTH = 50
BRICK_HEIGHT = 25
BRICK_SPACING = 4
# BRICK_START_X = 75
BRICK_START_X = (SCREEN_SIZE[0] / 2) - (((BRICKS_PER_ROW * BRICK_WIDTH) - ((BRICKS_PER_ROW) * BRICK_SPACING)) / 2)
# BRICK_START_X = (SCREEN_SIZE[0] / 2) - ((BRICKS_PER_ROW * (BRICK_WIDTH - BRICK_SPACING)) / 2)
BRICK_START_Y = BRICK_SPACING + (BRICKS_PER_COLUMN * (BRICK_HEIGHT + BRICK_SPACING))
BRICK_COLOR = [randint(64,255), randint(64,255), randint(64,255)]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(6*random.random() - 2, 6*random.random() - 2),
                                    [255, 10, 0], BALL_RADIUS)
    object_list.append(kinetic)

    paddle = KineticPaddle(Vector2(PADDLE_X, PADDLE_Y), PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
    object_list.append(paddle)
    
    x = BRICK_START_X
    y = BRICK_START_Y
    for i in range(BRICKS_PER_COLUMN):
        for j in range(BRICKS_PER_ROW):
            block = KineticBlock(Vector2(x,y), BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR)
            x += BRICK_WIDTH + BRICK_SPACING
            object_list.append(block)
        x = BRICK_START_X
        y -= (BRICK_HEIGHT + BRICK_SPACING)

def main():
    global PADDLE_X
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            object_list[1].move_left()

        if keys[pygame.K_RIGHT]:
            object_list[1].move_right()

        for object in object_list:
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
        # for paddle in object_list:
        #     paddle.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
