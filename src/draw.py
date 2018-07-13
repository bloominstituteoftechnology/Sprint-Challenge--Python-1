import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]

#define colors
RED = [255, 0, 0]
RED_ORANGE = [255, 125, 0]
ORANGE = [255, 185, 0]
YELLOW = [255, 255, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

#define width and height

HEIGHT_GAME_BLOCK= 40
WIDTH_GAME_BLOCK= 400

# MARGIN?? set here if want it

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(200, SCREEN_SIZE[0] - 200), random.randint(250, SCREEN_SIZE[1] - 250)),
                                    Vector2(4, 4),
                                    [33, 120, 125], 10)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    paddle = PaddleBlock(object_list, Vector2(150, 749), 120, 15, [104, 104, 104])
    object_list.append(paddle)
        
    gameblock_red = GameBlock(1, object_list, Vector2(0, 0), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, RED)
    object_list.append(gameblock_red)
    gameblock_red = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, 0), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, RED)
    object_list.append(gameblock_red)

    gameblock_redorange = GameBlock(1, object_list, Vector2(0, HEIGHT_GAME_BLOCK), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, RED_ORANGE)
    object_list.append(gameblock_redorange)
    
    gameblock_redorange = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, RED_ORANGE)
    object_list.append(gameblock_redorange)

    gameblock_orange = GameBlock(1, object_list, Vector2(0, HEIGHT_GAME_BLOCK*2), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, ORANGE)
    object_list.append(gameblock_orange)
    
    gameblock_orange = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK*2), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, ORANGE)
    object_list.append(gameblock_orange)

    gameblock_yellow = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK*3), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, YELLOW)
    object_list.append(gameblock_yellow)

    gameblock_yellow = GameBlock(1, object_list, Vector2(0, HEIGHT_GAME_BLOCK*3), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, YELLOW)
    object_list.append(gameblock_yellow)

    gameblock_green = GameBlock(1, object_list, Vector2(0, HEIGHT_GAME_BLOCK*4), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, GREEN)
    object_list.append(gameblock_green)

    gameblock_green = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK*4), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, GREEN)
    object_list.append(gameblock_green)

    gameblock_blue = GameBlock(1, object_list, Vector2(0, HEIGHT_GAME_BLOCK*5), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, BLUE)
    object_list.append(gameblock_blue)

    gameblock_blue = GameBlock(1, object_list, Vector2(WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK*5), WIDTH_GAME_BLOCK, HEIGHT_GAME_BLOCK, BLUE)
    object_list.append(gameblock_blue)
        


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Breakout-Clone")
    # pygame.mouse.set_pos(0, 0) # for ease of getting coordinates for build
    pygame.mouse.set_visible(0) #turns off mouse pointer
    pygame.font.SysFont("Arial", 128, bold=True)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    done = False

    while not done: # TODO:  Create more elegant condition for loop xx
        left = False
        right = False
        motion = False        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                print("Thank you for playing!")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                    print("left arrow was pressed!")
                elif event.key == pygame.K_RIGHT:
                    right = True
                    print("right arrow was pressed!")
                elif event.key == pygame.K_ESCAPE:
                    done = True
                    print("You've escaped the game!")
            # elif event.type == pygame.MOUSEMOTION: # for ease of gettin coordinates for setup
            #     #get mouse position
            #     x, y = pygame.mouse.get_pos()
            #     print(x, y)
            #     continue
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
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
