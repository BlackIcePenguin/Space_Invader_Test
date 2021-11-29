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
    def __init__(self, row_val, column_val):
        pygame.sprite.Sprite.__init__(self)
        if row_val > 3.1:
            self.image_path = GREEN_ALIEN
        if 1.1 < row_val < 3.1:
            self.image_path = YELLOW_ALIEN
        if row_val < 1.1:
            self.image_path = RED_ALIEN
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.enemy_edge = SCREEN_WIDTH // 10
        self.screen_divider = (SCREEN_WIDTH - self.enemy_edge) // 12
        self.rect.center = self.enemy_edge + self.screen_divider * column_val, self.rect.height * row_val * 1.2
        self.y_velo = 0
        self.x_velo = 3

    def update(self):
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.x_velo *= -1
            self.rect.y += self.rect.height
        self.rect.x += self.x_velo


class Missile(pygame.sprite.Sprite):
    def __init__(self, display, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.y_velo = 3.5

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.y_velo

        if self.rect.bottom <= 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, display, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.y_velo = 3.5

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, RED, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y += self.y_velo

        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()


class Block(pygame.sprite.Sprite):
    def __init__(self, display, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, self.color, [self.rect.x, self.rect.y, BLOCK_WIDTH, BLOCK_HEIGHT])

    def update(self):
        pass
