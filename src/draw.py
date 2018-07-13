import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 600]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(10*random.random() - 2, 10*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 255, 0])
    # object_list.append(block)

    paddle = Paddle(SCREEN_SIZE, Vector2(400,590), 100, 20, [0, 0, 255])
    object_list.append(paddle)

    for j in range(100, 200, 20):
      for i in range(25, SCREEN_SIZE[0], 50):
        brick = Brick(SCREEN_SIZE, Vector2(i,j), 50, 20, [random.randint(0,255), random.randint(0,255), random.randint(0,255)])
        object_list.append(brick)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
     
    done = True

    while done: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    print(event)
                if event.key == pygame.K_s:
                    # TODO: Add behavior when button pressed
                    debug_create_objects(object_list)
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left = left, right = right)
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
