import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT - self.rect.height

        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.change_x = 4
        elif keys[pygame.K_LEFT]:
            self.change_x = -4
        else:
            self.change_x = 0
        if self.rect.left + self.change_x <= 0 or self.rect.right + self.change_x >= SCREEN_WIDTH:
            self.change_x = 0


class Enemy(pygame.sprite.Sprite):
    # def __init__(self, image_path):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.image.load(image_path)
    #     self.rect = self.image.get_rect()
    pass


class Missile(pygame.sprite.Sprite):
    # def __init__(self, image_path):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.image.load(image_path)
    #     self.rect = self.image.get_rect()
    pass
