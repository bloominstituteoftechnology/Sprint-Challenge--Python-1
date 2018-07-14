import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 700]
GAME_SIZE = [800, 600]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, GAME_SIZE, 
                                    Vector2(GAME_SIZE[0]/2, GAME_SIZE[1] - 40),
                                    Vector2(10*random.random() - 6, 7*random.random() + 3),
                                    [255, 255, 255], 10)
    object_list.append(kinetic)

    floor = Floor(object_list, GAME_SIZE, Vector2(GAME_SIZE[0]/2,GAME_SIZE[1]), GAME_SIZE[0], 2, [0, 255, 0], 4)
    object_list.append(floor)

    paddle = Paddle(GAME_SIZE, Vector2(400,GAME_SIZE[1]-10), 100, 20, [81, 192, 255])
    object_list.append(paddle)

    for j in range(220, 180 , -20):
      for i in range(25, GAME_SIZE[0], 50):
        brick = Brick(object_list, GAME_SIZE, Vector2(i,j), 48, 18, [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 1)
        object_list.append(brick)
    for j in range(180, 140 , -20):
      for i in range(25, GAME_SIZE[0], 50):
        brick = Brick(object_list, GAME_SIZE, Vector2(i,j), 48, 18, [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 2)
        object_list.append(brick)
    for j in range(140, 100 , -20):
      for i in range(25, GAME_SIZE[0], 50):
        brick = Brick(object_list, GAME_SIZE, Vector2(i,j), 48, 18, [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 3)
        object_list.append(brick)
    for j in range(100, 60 , -20):
      for i in range(25, GAME_SIZE[0], 50):
        brick = Brick(object_list, GAME_SIZE, Vector2(i,j), 48, 18, [random.randint(0,255), random.randint(0,255), random.randint(0,255)], 4)
        object_list.append(brick)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    debug_create_objects(object_list)

    done = True
    play = False

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
                if event.key == pygame.K_r:
                    # TODO: Add behavior when button pressed
                    object_list = []
                    debug_create_objects(object_list)
                    play = False
                if event.key == pygame.K_p:
                    # TODO: Add behavior when button pressed
                    play = not play
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        if play:
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
