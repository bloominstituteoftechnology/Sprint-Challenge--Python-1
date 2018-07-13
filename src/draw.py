import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 600]
BACKGROUND_COLOR = [255, 255, 255]
DIFFICULTY = 10
PADDLE_WIDTH = 90
PADDLE_HEIGHT = 20

def debug_create_objects(object_list):
    ball = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(DIFFICULTY, DIFFICULTY),
                                    [255, 10, 0], 15)
    # object_list.append(ball)

    kinetic_block = KineticBlock(Vector2(300, 25), 100, 20, [0, 0, 255])
    # object_list.append(kinetic_block)

    vanishing_block = VanishingBlock(Vector2(100, 25), 100, 20, [255, 0, 0])
    # object_list.append(vanishing_block)

    multiple_hits_block = MultipleHitsBlock(Vector2(200, 25), 100, 20, [0, 255, 0])
    # object_list.append(multiple_hits_block)

    paddle = Paddle(Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-20), PADDLE_WIDTH, PADDLE_HEIGHT, [255, 165, 0])
    
    object_list += [ball, kinetic_block, vanishing_block, multiple_hits_block, paddle]

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)

    while True: # TODO:  Create more elegant condition for loop
        # left = False
        # right = False

        keys = pygame.key.get_pressed()
        ball = object_list[0]
        paddle = object_list[-1]

        if ball.dropped_count > 5:
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.

        if keys[pygame.K_LEFT]:
            paddle.position.x = max(PADDLE_WIDTH//2, paddle.position.x - 5)
            paddle.update()
            pass
            # left = True
        if keys[pygame.K_RIGHT]:
            paddle.position.x = min(SCREEN_SIZE[0]-PADDLE_WIDTH//2, paddle.position.x + 5)
            paddle.update()
            pass
            # right = True
        for object in object_list:
            object.update()
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
