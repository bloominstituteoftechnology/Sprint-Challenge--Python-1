import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(5,5),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    paddle = Paddle(Vector2(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 50), 170, 20, [0, 0, 0])
        # start paddle at center of X axis and 50 px above floor
    object_list.append(paddle)

    regularBlock = RegularBlock(object_list, Vector2(200,200), 50, 50, [50,50,50])
    object_list.append(regularBlock)

    regularBlock = RegularBlock(object_list, Vector2(200,250), 50, 50, [150,150,150])
    object_list.append(regularBlock)

    x = 25
    color = [255, 0, 0]
    for i in range(8):
        #color = [random.randint(100, 250), random.randint(100, 250), random.randint(100, 250)]
        regularBlock = RegularBlock(object_list, Vector2(x,250), 50, 20, color)
        object_list.append(regularBlock)
        x += 50
        # color[0] = color[0]-30
        # print(color)

    #(self, object_list, position, width, height, color)
  
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
            object_list[1].left = True
            # print('left arrow pressed')
            # print(left)
        if keys[pygame.K_RIGHT]:
            right = True
            object_list[1].right = True

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
