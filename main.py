import pygame
import os

pygame.init()
pygame.display.set_caption("Fake jump")

FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
BG_COLOR = (154, 151, 255)

PLAYER_TEXTURE = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "player.png")), (50, 50))


def draw_window(player):
    WIN.fill(BG_COLOR)
    WIN.blit(PLAYER_TEXTURE, (player.x, player.y))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(player)

    pygame.quit()


if __name__ == "__main__":
    main()
