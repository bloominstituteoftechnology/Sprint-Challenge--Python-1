import pygame
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 700]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(obj_list):
    kinetic = GameBall(1, obj_list, SCREEN_SIZE, Vector2(300, 300), Vector2(7, -7), [255, 10, 0], 20)
    obj_list.append(kinetic)

    paddle = Paddle(Vector2(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 50), 150, 35, [0, 0, 0], [])
    obj_list.append(paddle)

    for i in range(5):
       block_list = []
       color = [34,100,25]
       for j in range(4):
           block = KineticBlock(Vector2(72 + (i*124),100 + (j* 40)), 120, 30, color, obj_list)
           obj_list.append(block)
           print(obj_list)
  
def main():
    pygame.init()
    pygame.font.init()
    game_font = pygame.font.SysFont('', 28)
    pygame.display.set_caption("Breakout")
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    clock = pygame.time.Clock()
 
    obj_list = []
    
    debug_create_objects(obj_list)
 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            obj_list[1].move_left()
            pass
        if keys[pygame.K_RIGHT]:
            obj_list[1].move_right()
            pass
        for object in obj_list:
            object.update()
            object.check_collision()
 
        screen.fill(BACKGROUND_COLOR)
        for ball in obj_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
