import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    ball = GameBall(1, object_list, SCREEN_SIZE, 
                            Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                            Vector2(4*random.random() - 2, 4*random.random() - 2),
                            [255, 10, 0], 20)

    kb_1 = KineticBlock(Vector2(   0, 10), 40, 10, [0, 0, 255])
    kb_2 = KineticBlock(Vector2(  40, 10), 40, 10, [0, 0, 255])
    kb_3 = KineticBlock(Vector2(  80, 10), 40, 10, [0, 0, 255])
    kb_4 = KineticBlock(Vector2( 120, 10), 40, 10, [0, 0, 255])
    kb_5 = KineticBlock(Vector2( 160, 10), 40, 10, [0, 0, 255])
    kb_6 = KineticBlock(Vector2( 200, 10), 40, 10, [0, 0, 255])
    kb_7 = KineticBlock(Vector2( 240, 10), 40, 10, [0, 0, 255])
    kb_8 = KineticBlock(Vector2( 280, 10), 40, 10, [0, 0, 255])
    kb_9 = KineticBlock(Vector2( 320, 10), 40, 10, [0, 0, 255])
    kb_10 = KineticBlock(Vector2(360, 10), 40, 10, [0, 0, 255])
    kb_11 = KineticBlock(Vector2(400, 10), 40, 10, [0, 0, 255])
    kb_12 = KineticBlock(Vector2(440, 10), 40, 10, [0, 0, 255])
    kb_13 = KineticBlock(Vector2(480, 10), 40, 10, [0, 0, 255])
    kb_14 = KineticBlock(Vector2(520, 10), 40, 10, [0, 0, 255])
    kb_15 = KineticBlock(Vector2(560, 10), 40, 10, [0, 0, 255])
    kb_16 = KineticBlock(Vector2(600, 10), 40, 10, [0, 0, 255])
    kb_17 = KineticBlock(Vector2(640, 10), 40, 10, [0, 0, 255])

    object_list.extend([ball, kb_1, kb_2, kb_3, kb_4, kb_5, kb_6, kb_7, kb_8, kb_9, kb_10, kb_11, kb_12, kb_13, kb_14, kb_15, kb_16, kb_17])
  
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
