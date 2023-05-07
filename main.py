import pygame
import time
import random

width, height = 1366, 768
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Birthday!")

bg = pygame.image.load("bg.png")

def draw():
    win.blit(bg, (0,0))
    pygame.display.update()
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
