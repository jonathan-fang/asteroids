import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # start pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:

        # Update game state
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Render
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
