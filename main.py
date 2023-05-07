import pygame
import time
import random

width, height = 1366, 768
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Birthday!")


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
