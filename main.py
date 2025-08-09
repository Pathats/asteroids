import pygame

from constants import *
def main():
    color = "black"
    pygame.init()
    print(
        "Starting Asteroids!\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
        )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(color)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        




if __name__ == "__main__":
    main()
