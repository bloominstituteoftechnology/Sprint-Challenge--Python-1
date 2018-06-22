import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *
from paddle import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
PADDLE_X = 320
PADDLE_Y = 450

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    paddle = KineticPaddle(Vector2(PADDLE_X, PADDLE_Y), 100, 20, [128, 0, 128])
    object_list.append(paddle)
  
    x = 100
    y = 150
    for i in range(5):
        for j in range(5):
            block = KineticBlock(Vector2(x,y), 100, 25, [0, 0, 255])
            x += 105
            object_list.append(block)
        x = 100
        y -= 30

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
        for paddle in object_list:
            paddle.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
