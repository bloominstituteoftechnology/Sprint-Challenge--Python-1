import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(7, 7),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(300,400), 80, 50, [0, 255, 0])
    object_list.append(block)

    x = 25
    for y in range(0, 18): # row of blocks no 1
        block = DestructableBlock(object_list,Vector2((x), 20), 40, 40, [0, 255, 0])
        object_list.append(block)
        x += 45
        continue
    x = 25
    for y in range(0, 18):  # row of blocks no 2
        if y % 3 == 0:
            block = AbsolutelyPositivelIndustructibleBlock(Vector2((x), 65), 40, 40, [0, 255, 0])
            object_list.append(block)
        else: 
            block = NotSoDestructableBlock(object_list,Vector2((x), 65), 40, 40, [0, 255, 0])
            object_list.append(block)
        x += 45
    x = 25
    for y in range(0, 18):  # row of blocks no 3
        block = DestructableBlock(object_list, Vector2((x), 110), 40, 40, [0, 255, 0])
        object_list.append(block)
        x += 45

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Nando's Breakout")
    screen = pygame.display.set_mode(SCREEN_SIZE)
    myfont = pygame.font.SysFont('Comic Sans MS', 32)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)

    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        score = (56 - len(object_list)) * 10
        
        textsurface = myfont.render(f'Points: {score}', True, (255, 255, 255))
        screen.blit(textsurface,(100,100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        for object in object_list:
            if isinstance(object, Block):
                object.update(left, right)
                object.check_collision()
            else:
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
