import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800] # previously [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 10)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(100,750), 70, 15, [0, 0, 255]) # PADDLE
    # object_list.append(block)

    paddle = Paddle(Vector2(100,750), 70, 15, [0, 0, 255])
    object_list.append(paddle)

    for i in range(6):
        blue_bricks =KineticBlock(Vector2(120*i/2,100), 40, 20, [0, 0, 255])
        object_list.append(blue_bricks)

        for j in range(8):
            green_bricks = KineticBlock(Vector2(120*i/2,130), 40, 20, [50,205,50])
            object_list.append(green_bricks)

            for k in range(8):
                purple_bricks = KineticBlock(Vector2(120*i/2,160), 40, 20, [138,43,226])
                object_list.append(purple_bricks)

    
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

        paddle = object_list[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_LEFT:
            #         paddle.position.x += 5
            #     if event.key == pygame.K_RIGHT:
            #         paddle.position.x += 5
                
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True

        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left=left, right=right)
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
