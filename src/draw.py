import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

#blocks **turnn into list
    block = KineticBlock(Vector2(50, 35), 50, 50, [200, 200, 255])
    object_list.append(block)

    block2 = KineticBlock(Vector2(125, 35), 50, 50, [255, 100, 25])
    object_list.append(block2)

    block3 = KineticBlock(Vector2(200, 35), 50, 50, [175, 80, 100])
    object_list.append(block3)

    block4 = KineticBlock(Vector2(275, 35), 50, 50, [150, 100, 150])
    object_list.append(block4)

    block5 = KineticBlock(Vector2(350, 35), 50, 50, [175, 255, 175])
    object_list.append(block5)
    
#paddle
    paddle = KineticBlock(Vector2(200,750), 100, 50, [255, 255, 0])
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
