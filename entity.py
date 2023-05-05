import pygame
import os
import bullet
import random

class Player:
    def __init__(self, screen):
        # stats
        self.hp = 100
        self.speed = 5
        self.width, self.height = 50, 50
        self.screen = screen

        # sprite and body
        self.sprite = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player.png")), (self.width, self.height))
        self.rect = pygame.Rect(self.screen.get_width()/2, self.screen.get_height()/2, self.width, self.height)

        self.bullets = []


    def update(self, ):
        self.input()

        for b in self.bullets:
            b.update()
            # delete bullets
            if b.rect.y < 0:
                self.bullets.remove(b)

    def render(self):
        self.screen.blit(self.sprite, (self.rect.x, self.rect.y))
    
    def shoot(self):
        b = bullet.Bullet(self.rect, self.screen)
        self.bullets.append(b)

    def take_damage(self):
        self.hp -= 10

    def input(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d] and self.rect.x < self.screen.get_width() - self.width:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.y < self.screen.get_height() - self.height:
            self.rect.y += self.speed

class Meteor:
    def __init__(self, screen):
        # stats
        self.width, self.height = 30, 30
        self.velocity = random.randint(2, 5)
        self.screen = screen

        # sprite and body
        self.sprite = pygame.transform.scale(pygame.image.load(os.path.join("assets", "meteor.png")), (self.width, self.height))
        self.rect = pygame.Rect(random.randint(self.width, self.screen.get_width() - self.width), -10, self.width, self.height)


    def reset(self):
        self.rect.x = random.randint(self.width, self.screen.get_width() - self.width)
        self.rect.y = -10
        self.velocity = random.randint(2, 5)

    def update(self):
        if self.rect.y > self.screen.get_height():
            self.reset()
        self.rect.y += self.velocity
    
    def render(self):
        self.screen.blit(self.sprite, (self.rect.x, self.rect.y))