import pygame
import sys
import os
import entity


class Game:
    def __init__(self):
        self.status = 'game'
        self.score = 0
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'background.png')), (screen_width, screen_height))

        # entities
        self.meteors = []
        for i in range(8):
            self.meteors.append(entity.Meteor(screen))
        self.player = entity.Player(screen)

    def change_score(self, amount):
        self.score += amount

    def check_game_over(self):
        if self.player.hp <= 0:
            self.player.hp = 100
            self.score = 0
            # self.status = 'lose'
    
    def handele_collision(self):
        # player collision
        for m in self.meteors:
            if m.rect.colliderect(self.player.rect):
                m.reset()
                self.player.take_damage()

        # bullet collision
        for b in self.player.bullets:
            for m in self.meteors:
                if m.rect.colliderect(b.rect):
                    m.reset()
                    self.change_score(1)
                    
                    # temp fix for a collision error
                    if b in self.player.bullets:
                        self.player.bullets.remove(b)
    
    def render(self):
        screen.blit(self.background, (0, 0))
        for b in self.player.bullets:
            b.render()

        self.player.render()

        for m in self.meteors:
            m.render()

    def update(self):
        if self.status == 'lose':
            self.lose.run()
        else:
            self.player.update()
            for m in self.meteors:
                m.update()
            self.handele_collision()
            self.check_game_over()


# pygame setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("Space pew pew")

screen_width, screen_height = 270, 480
font = pygame.font.SysFont('Arial', 40)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.shoot()
    game.render()
    game.update()

    pygame.display.update()
    clock.tick(60)
