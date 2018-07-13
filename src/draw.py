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
                                    Vector2(3, -3),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)


    # paddle = KineticBlock(Vector2(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 50), 70, 15, [0, 0, 0])
    # object_list.append(paddle)

    for i in range(5):
        block_list = []
        color = [0,0,62]
        for j in range(3):
            block = KineticBlock(Vector2(52 + (i*74),100 + (j* 40)), 70, 30, color)
            object_list.append(block)
            print(object_list)
  
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
            object_list[2].rectangle.move_ip(-6,0)
        if keys[pygame.K_RIGHT]:
            right = True
            object_list[2].rectangle.move_ip(6,0)
            
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
