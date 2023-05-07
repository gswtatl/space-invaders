import pygame
import time
import random
pygame.font.init()

width, height = 1366, 768
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")

bg = pygame.transform.scale((pygame.image.load("bg.png")), (width, height))

player_width = 40
player_height = 60

player_vel = 20

star_width = 20
star_height = 30

star_vel = 10

font = pygame.font.SysFont("comicsans", 50)


def draw(player, elapsed_time, stars):
    win.blit(bg, (0, 0))
    time_text = font.render(f"Time: {round(elapsed_time)}s", True, "black")
    win.blit(time_text, (50, 25))
    pygame.draw.rect(win, (255, 0, 0), player)
    for star in stars:
        pygame.draw.rect(win, "blue", star)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(663, 510, player_width, player_height)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width <= width:
            player.x += player_vel

        for star in stars[:]:
            star.y += star_vel
            if star.y > height:
                stars.remove(star)
            elif star.y + star_height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = font.render("You lost!", True, "black")
            win.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            main()

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
