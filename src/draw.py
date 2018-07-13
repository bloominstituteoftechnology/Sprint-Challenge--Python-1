import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # starting X and Y axis of breakable blocks
    # values change after each iteration of the for loop a few lines below
    posX = 50
    posY = 200

    # start for
    for block in range(1, 10):
        rand = random.randint
        game_ball = kinetic

        block = BreakableBlock(Vector2(posX,200), 100, 100, [rand(0, 255), rand(0, 255), rand(0, 255)], game_ball)
        object_list.append(block)

        posX += 100
    # end for

    block = PlayerBlock(Vector2(320, 465), 1000, 15, [255, 0, 255])
    object_list.append(block)

    print(len(object_list))
  
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
            # check if `object` is an instance of `PlayerBlock`
            # updates the X position but DOES NOT ACTUALLY WORK
            if isinstance(object, PlayerBlock):
                # grab `object` current position
                posX = object.position[0]
                
                if left:
                    object.position[0] -= 1
                    print(f"posX: {posX}")
                    print(object.position[0])

                if right:
                    object.position[0] += 1
                    print(object.position[0])
            
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
