import pygame
import time
import random

width, height = 1366, 768
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")

bg = pygame.transform.scale((pygame.image.load("bg.png")), (width, height))

player_width = 40
player_height = 60


def draw(player):
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 200, 200), player)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(663, height - player_height, player_width, player_height)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()
