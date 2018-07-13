import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    speed = 6
    # Vector2(speed*random.random() - 2, speed*random.random() - 2)
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(speed, speed),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = BreakableBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    breakableblocks = []
    for i in range(0,3):
        breakableblocks.append(BreakableBlock(Vector2(50+(i*100),100),100,50,[255,140,0]))
    object_list.extend(breakableblocks)

    player_paddle = PlayerPaddle(SCREEN_SIZE, Vector2(200,750), 200, 30, [255, 255, 0])
    object_list.append(player_paddle)

def break_breakables(object_list):
    def is_ball_touched(object):
        if hasattr(object, 'touched_by_ball'):
            if object.touched_by_ball: return True
        return False

    object_list[:] = [object for object in object_list if not is_ball_touched(object)]

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
            if event.type == pygame.QUIT: exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left=left, right=right)
            object.check_collision()
        break_breakables(object_list)
 
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
