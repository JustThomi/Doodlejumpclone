import pygame
import os
import random


pygame.init()
pygame.display.set_caption("Fake jump")

FPS = 60
WIDTH, HEIGHT = 270, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_VELOCITY = 10

BULLET_VELOCITY = 10
BULLET_COLLOR = (255, 0, 0)
BG_COLOR = (154, 151, 255)

SCROLL_SPEED = 5

PLAYER_TEXTURE = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "player.png")), (50, 50))


def draw_window(player, bullets):
    WIN.fill(BG_COLOR)
    WIN.blit(PLAYER_TEXTURE, (player.x, player.y))

    for i in range(len(bullets)):
        pygame.draw.rect(WIN, BULLET_COLLOR, bullets[i])

    pygame.display.update()

def player_controller(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_UP] and player.y > 0:
        player.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and player.y < HEIGHT - player.height:
        player.y += PLAYER_VELOCITY


def handle_bullets(bullets):
    for b in bullets:
        b.y -= BULLET_VELOCITY

        if b.y < 0:
            bullets.remove(b)


def main():
    run = True
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    bullets = []

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width/2 , player.y, 10, 10)
                    bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()

        player_controller(keys_pressed, player)
        handle_bullets(bullets)
        draw_window(player, bullets)

    pygame.quit()


if __name__ == "__main__":
    main()
