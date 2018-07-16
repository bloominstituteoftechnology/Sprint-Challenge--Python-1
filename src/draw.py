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
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    paddle = Paddle(Vector2(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 50), 100, 50, [0, 0, 255])
    object_list.append(paddle)

    for i in range(5):
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        for j in range(3):
            regularblock = RegularBlock(Vector2(40 + (i*75), 100 + (j * 40)), 70, 30, color, object_list)
            object_list.append(regularblock)

    rainbowblock = RainbowBlock(Vector2(200, 250), 200, 50, [255, 0, 0], object_list)
    object_list.append(rainbowblock)
    
    object_list += [kinetic, paddle, regularblock, rainbowblock]

# Had fun tweaking the size and shape of everything. I decided on a 3X5 grid of blocks and then kept playing around with the vectors until they looked like the right size.
# They kind of skew to the left, but close enough for now.
# The compiler errors told me I needed to add line 31 to fill the object_list below. 
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []
 
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        
        paddle = object_list[1]
# The compiler told me I needed the line above.

        if keys[pygame.K_LEFT]:
            paddle.position.x = max(50, paddle.position.x - 5)
            paddle.update()

        if keys[pygame.K_RIGHT]:
            paddle.position.x = min(SCREEN_SIZE[0] - 50, paddle.position.x + 5)
            paddle.update()

# I was just doing paddle.position.x +- 5 for moving the paddle but found that it would go off the screen so I tried to limit the movement
# Resource: https://www.tutorialspoint.com/python/number_max.htm
# This helped a lot! Once I figured out max, min was easy.

        for object in object_list:
            object.check_collision()
            object.update()
# Nothing moved until I added object.update(). Which makes sense, but it took me a couple of tries to figure out that this was the right place to put it.

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
