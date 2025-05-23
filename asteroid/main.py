# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    game_is_running = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while game_is_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill("black")
        pygame.display.flip()
    
if __name__ == "__main__":
    main()