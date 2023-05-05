import pygame

class Bullet:

    def __init__(self, player_rect, screen):
        self.size = 6
        self.velocity = 10
        self.color = (255, 252, 87)
        self.screen = screen

        self.rect = pygame.Rect(
            player_rect.x + 23, player_rect.y, self.size, self.size)

    def update(self):
        self.rect.y -= self.velocity

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
