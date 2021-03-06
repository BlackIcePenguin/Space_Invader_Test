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
    def __init__(self, row_val, column_val, round_multiplier):
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
        self.rect.center = self.enemy_edge + self.screen_divider * column_val, self.rect.height * row_val * 1.2 + 60
        self.y_velo = 0
        self.x_velo = 1 * round_multiplier

    def update(self, collided):
        # if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
        self.collided = collided
        if self.collided:
            self.x_velo *= -1
            self.rect.y += self.rect.height / 2
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
        self.health = 3
        pygame.draw.rect(self.image, self.color, [self.rect.x, self.rect.y, BLOCK_WIDTH, BLOCK_HEIGHT])

    def update(self):
        if self.health <= 2:
            self.color = GREEN
        if self.health <= 1:
            self.color = RED
        if self.health <= 0:
            self.kill()
        self.image.fill(self.color)


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, display, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 3

    def update(self):
        pass


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = EXPLOSION_LIST[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.kill_center = center
        self.prev_update = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.prev_update > self.frame_rate:
            self.prev_update = current_time
            self.frame += 1
        if self.frame >= len(EXPLOSION_LIST):
            self.kill()
        else:
            self.image = EXPLOSION_LIST[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.kill_center


