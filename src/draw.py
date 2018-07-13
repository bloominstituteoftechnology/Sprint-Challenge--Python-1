import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]
VELOCITY = 5

def debug_create_objects(object_list):
    ball = GameBall(1, object_list, SCREEN_SIZE, 
                            Vector2(random.randint(20, SCREEN_SIZE[0] - 150), random.randint(20, SCREEN_SIZE[1] - 150)),
                            Vector2(random.randint(70,100)*0.01*VELOCITY  , random.randint(70,100)*0.01*VELOCITY ),
                            [255, 10, 0], 10)
    
    paddle = Paddle(Vector2(150, 700), 70, 10, [255, 0, 0] )

    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    row_5 = []

    block_dict = {
        "1": BlockOne,
        "2": KineticBlock,
        "3": BlockThree
    }

    for i in range(0,11):
        block_type = block_dict[f'{random.randint(1,3)}']
        block = block_type(Vector2(40 * i, 10), 40, 30, [0, 0, 255])
        row_1.append(block)
    for i in range(0,11):
        block_type = block_dict[f'{random.randint(1,3)}']
        block = block_type(Vector2(40 * i, 40), 40, 30, [255, 0, 0])
        row_2.append(block)
    for i in range(0,11):
        block_type = block_dict[f'{random.randint(1,3)}']
        block = block_type(Vector2(40 * i, 70), 40, 30, [0, 200, 100])
        row_3.append(block)
    for i in range(0,11):
        block_type = block_dict[f'{random.randint(1,3)}']
        block = block_type(Vector2(40 * i, 100), 40, 30, [0, 100, 255])
        row_4.append(block)
    for i in range(0,11):
        block_type = block_dict[f'{random.randint(1,3)}']
        block = block_type(Vector2(40 * i, 130), 40, 30, [255, 255, 0])
        row_5.append(block)

    object_list.extend([ball, paddle, *row_1, *row_2, *row_3, *row_4, *row_5])
  
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
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for object in object_list:
                    if hasattr(object, "paddle"):
                        if mouse_pos[0] > 330:
                            object.rectangle.x = 330
                        else:
                            object.rectangle.x = mouse_pos[0]
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
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
