import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), SCREEN_SIZE[1] - 350),
                                    Vector2(4*random.random() - 2, 4),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    block1_size = random.randint(40, 100)
    block1_difficulty = 1
    block1_color = [0, 0, 255]
    block1 = KineticBlock(
        Vector2(random.randint(block1_size, SCREEN_SIZE[0]-block1_size),
            random.randint(block1_size, SCREEN_SIZE[1]-300)), 
        block1_size, block1_size, block1_color, block1_difficulty)
    object_list.append(block1)

    block2_size = random.randint(40, 100)
    block2_difficulty = 3
    block2_color = [0, 255, 0]
    block2 = KineticBlock(
        Vector2(random.randint(block2_size, SCREEN_SIZE[0]-block2_size),
            random.randint(block2_size, SCREEN_SIZE[1]-300)), 
        block2_size, block2_size, block2_color, block2_difficulty)
    object_list.append(block2)

    block3_size = random.randint(40, 100)
    block3_difficulty = 2
    block3_color = [100, 0, 100]
    block3 = KineticBlock(
        Vector2(random.randint(int(block3_size/2), SCREEN_SIZE[0]-int(block3_size/2)),
            random.randint(block3_size, SCREEN_SIZE[1]-300)), 
        block3_size, block3_size, block3_color, block3_difficulty)
    object_list.append(block3)

    unbreakable_size = random.randint(40, 100)
    unbreakable = UnbreakableBlock(
        Vector2(random.randint(int(unbreakable_size/2), SCREEN_SIZE[0]-int(unbreakable_size/2)),
            random.randint(unbreakable_size, SCREEN_SIZE[1]-300)), 
        unbreakable_size, unbreakable_size, [0, 0, 0])
    object_list.append(unbreakable)

    ghost_size = random.randint(40, 100)
    ghost = GhostBlock(
        Vector2(random.randint(int(ghost_size/2), SCREEN_SIZE[0]-int(ghost_size/2)),
            random.randint(ghost_size, SCREEN_SIZE[1]-300)), 
        ghost_size, ghost_size, [0, 0, 0])
    object_list.append(ghost)

    paddle = Paddle(Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-15), 100, 30, [0, 0, 0])
    object_list.append(paddle)

def continue_playing(obj_list):
    for obj in obj_list:
        if isinstance(obj, KineticBlock):
            return True
    print("YOU WIN!")
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)

    playing = True
 
    while playing:
        left = False
        right = False
        
        playing = continue_playing(object_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                playing = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            if hasattr(object, 'defeated'):
                if object.defeated == True:
                    object_list.remove(object)
            object.update(left=left, right=right)
            object.check_collision()

            if hasattr(object, 'game_over'):
                if object.game_over == True:
                    print('GAME OVER')
                    playing = False
 
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
