import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *


SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    #Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(400,150),
                                    Vector2(3, 3),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)
    player_block = PlayerBlock(Vector2(400,400), 150, 50, [0, 0, 0])
    block12 = SingleHit(Vector2(47,100), 50, 50, [0, 0, 255])
    block13 = SingleHit(Vector2(98,100), 50, 50, [0, 0, 255])
    block14 = SingleHit(Vector2(149,100), 50, 50, [0, 0, 255])
    block6 = SingleHit(Vector2(149,100), 50, 50, [0, 0, 255])
    block = SingleHit(Vector2(200,100), 50, 50, [0, 0, 255])
    block1 = SingleHit(Vector2(251,100), 50, 50, [0, 0, 255])
    block2 = SingleHit(Vector2(302,100), 50, 50, [0, 0, 255])
    block3 = SingleHit(Vector2(353,100), 50, 50, [0, 0, 255])
    block4 = SingleHit(Vector2(404,100), 50, 50, [0, 0, 255])
    block5 = SingleHit(Vector2(455,100), 50, 50, [0, 0, 255])
    block6 = SingleHit(Vector2(506,100), 50, 50, [0, 0, 255])
    block7 = SingleHit(Vector2(557,100), 50, 50, [0, 0, 255])
    block8 = SingleHit(Vector2(608,100), 50, 50, [0, 0, 255])
    block9 = SingleHit(Vector2(659,100), 50, 50, [0, 0, 255])
    block10 = SingleHit(Vector2(710,100), 50, 50, [0, 0, 255])
    block11 = SingleHit(Vector2(761,100), 50, 50, [0, 0, 255])
    object_list.append(block)
    object_list.append(block1)
    object_list.append(block2)
    object_list.append(block3)
    object_list.append(block4)
    object_list.append(block5)
    object_list.append(block6)
    object_list.append(block7)
    object_list.append(block8)
    object_list.append(block9)
    object_list.append(block10)
    object_list.append(block11)
    object_list.append(block12)
    object_list.append(block13)
    object_list.append(block14)

    object_list.append(player_block)

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
