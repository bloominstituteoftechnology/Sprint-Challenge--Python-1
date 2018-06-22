import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *
from paddle import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)
    

    block1 = KineticBlock(Vector2(100,200), 50, 50, [0, 0, 255])
    block2 = KineticBlock(Vector2(250,150), 50, 50, [0, 243, 255])
    block3 = KineticBlock(Vector2(390,280), 50, 50, [255, 0, 0])
    block4 = KineticBlock(Vector2(550,250), 50, 50, [0, 255, 0])
    object_list.append(block1)
    object_list.append(block2)
    object_list.append(block3)
    object_list.append(block4)

    print(object_list[4])

    #paddle here
    paddle = KineticPaddle(Vector2(400,SCREEN_SIZE[1]), 10, 100, 20, [255, 0, 0])
    object_list.append(paddle)
    #print(object_list[5].position.x)
  
def main():
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
            # Do something
            object_list[5].dx = object_list[5].dx
            object_list[5].update()
            #object_list[5].position.x = object_list[5].position.x -5
            print(object_list[5].position.x)
            #pass
        if keys[pygame.K_RIGHT]:
            # Do something
            object_list[5].dx = object_list[5].dx
            object_list[5].update()
            #object_list[5].position.x = object_list[5].position.x + 5
            print(object_list[5].position.x)
            
        if object_list[5].position.x < 0: # screen width
            object_list[5].x = 0
        
        if object_list[5].position.x > SCREEN_SIZE[0]:
            object_list[5].x = SCREEN_SIZE[0] 


        def random_color():
            levels = range(32,256,32)
            return tuple(random.choice(levels) for _ in range(3))


        for object in object_list:
            object.update()
            object.check_collision()
            if object.check_collision():
                if object.color and object != 'kinetic':
                    object.color = random_color()
                    #print(object)
 
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
