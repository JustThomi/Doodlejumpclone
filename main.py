import pygame
import os
import random


pygame.init()
pygame.font.init()
pygame.display.set_caption("Space pew pew")

FPS = 60
WIDTH, HEIGHT = 270, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont('Arial', 40)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_VELOCITY = 5

BULLET_VELOCITY = 10
BULLET_COLLOR = (255, 0, 0)
BG_COLOR = (154, 151, 255)

METEOR_VELOCITY = 3
METEOR_WIDTH, METEOR_HEIGHT = 30, 30
SCROLL_SPEED = 5

METEOR_TEXTURE = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "meteor.png")), (METEOR_WIDTH, METEOR_HEIGHT))

PLAYER_TEXTURE = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "player.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))


def draw_window(player, bullets, meteor, p_hp):
    hp_text = FONT.render(str(p_hp), False, (255, 255, 255))
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(hp_text, (WIDTH/2 - hp_text.get_width()/2,
             HEIGHT/2 - hp_text.get_height()))
    WIN.blit(PLAYER_TEXTURE, (player.x, player.y))

    for b in range(len(bullets)):
        pygame.draw.rect(WIN, BULLET_COLLOR, bullets[b])

    for m in range(len(meteor)):
        WIN.blit(METEOR_TEXTURE, (meteor[m].x, meteor[m].y))

    pygame.display.update()


def draw_lose_screen(game_over):
    text = FONT.render(game_over, False, (255, 255, 255))
    WIN.fill((38, 38, 91))
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2))

    pygame.display.update()
    pygame.time.wait(3000)


def player_controller(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_UP] and player.y > 0:
        player.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and player.y < HEIGHT - player.height:
        player.y += PLAYER_VELOCITY


def reset_meteor(m):
    m.x = random.randrange(WIDTH - METEOR_WIDTH)
    m.y = random.randrange(-METEOR_WIDTH, -60, -METEOR_WIDTH)


def handle_bullets(bullets, meteors):
    for b in bullets:
        b.y -= BULLET_VELOCITY

        for m in meteors:
            if m.colliderect(b):
                reset_meteor(m)
        if b.y < 0:
            bullets.remove(b)


def handle_meteor(meteor):
    for m in meteor:
        m.y += METEOR_VELOCITY

        if m.y > HEIGHT:
            reset_meteor(m)


def main():
    run = True
    clock = pygame.time.Clock()

    game_over = "You lost"
    hit_points = 10

    player = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    bullets = []
    meteors = [pygame.Rect(random.randrange(0, WIDTH - METEOR_WIDTH,
                           METEOR_WIDTH), random.randrange(0, -60, -METEOR_WIDTH), METEOR_WIDTH, METEOR_HEIGHT) for i in range(8)]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(
                        player.x + player.width/2, player.y, 7, 7)
                    bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()

        for m in meteors:
            if m.colliderect(player):
                reset_meteor(m)
                hit_points -= 1

        if hit_points <= 0:
            draw_lose_screen(game_over)
            main()

        player_controller(keys_pressed, player)
        handle_bullets(bullets, meteors)
        handle_meteor(meteors)
        draw_window(player, bullets, meteors, hit_points)

    pygame.quit()


if __name__ == "__main__":
    main()
