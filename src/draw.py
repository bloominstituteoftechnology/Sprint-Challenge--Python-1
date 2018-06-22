import pygame
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    
   
  
    x = 25
    y = 25
    for i in range(4):
        for j in range(7):
            rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            block = KineticBlock(Vector2(x, y), 100, 25, rand_color)    
            object_list.append(block)
            x += 100 + 5
        x = 25
        y += 25 + 5
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)

    paddle = Paddle(Vector2(85,750), 100, 40, [0,0,0])
    object_list.append(paddle)

    pygame.mouse.set_visible(False)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.position.x -= 5
            paddle.rectangle = pygame.Rect(
                                    paddle.position.x,
                                    paddle.position.y,
                                    100,
                                    40)
        if keys[pygame.K_RIGHT]:
            paddle.position.x += 5
            paddle.rectangle = pygame.Rect(
                                    paddle.position.x,
                                    paddle.position.y,
                                    100,
                                    40)

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
