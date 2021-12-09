import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Bomb, Block, HealthBar

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")


class Score:
    def __init__(self, display):
        self.display = display

    def draw_score(self, value):
        score_value = font_medium.render(f'Aliens Killed : {value}', True, WHITE)
        self.display.blit(score_value, [540, 10])

    def end_score(self, value):
        score_value1 = end_font.render(f'YOU DIED', True, RED)
        score_value2 = end_font.render(f'Your final score was {value} points', True, WHITE)
        score_value3 = end_font.render(f'Thanks for playing', True, WHITE)
        play_again1 = end_font.render(f'Press SPACE to start a new game', True, WHITE)
        play_again2 = end_font.render(f'Press any other key to quit', True, WHITE)
        self.display.blit(score_value1, [295, 50])
        self.display.blit(score_value2, [160, 150])
        self.display.blit(score_value3, [220, 425])
        self.display.blit(play_again1, [130, 700])
        self.display.blit(play_again2, [160, 800])

    def draw_timer(self, time_count):
        time_text = end_font.render(f'Time until next wave : {int(time_count / 60)}', True, WHITE)
        self.display.blit(time_text, [170, 300])
        if time_count <= 0:
            return True
        else:
            pass


def start():
    pass


points = Score(screen)


def game_play():
    # Sounds
    fire_sound = pygame.mixer.Sound("assets/shoot.wav")
    enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")
    player_hurt = pygame.mixer.Sound("assets/ShipHit.wav")

    # Sprite Groups
    player_group = pygame.sprite.Group()
    missile_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    bomb_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    health_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()  # Group for all sprites

    # Player
    player = Player(PLAYER)  # Create player object
    player_group.add(player)  # Load object into group
    all_sprites.add(player)

    # Enemy
    round_multiplier = 1
    for row_val in range(1, 6):
        for column_val in range(0, 12):
            enemy = Enemy(row_val, column_val, round_multiplier)
            enemy_group.add(enemy)
            # all_sprites.add(enemy)

    # Blocks
    for row_val in range(0, LAYOUT_LENGTH):
        for column_val in range(0, LAYOUT_HEIGHT):
            if LAYOUT[column_val][row_val] == '1':
                block = Block(screen, row_val * BLOCK_WIDTH, column_val * BLOCK_HEIGHT, BLUE)
                block_group.add(block)
                all_sprites.add(block)

    # Health Bar
    player_health = 3
    for val in range(0, player_health):
        life = HealthBar(screen, 20 + 80 * val, 10, PLAYER)
        health_group.add(life)
        all_sprites.add(life)

    clock = pygame.time.Clock()

    enemy_reload = 0
    player_reload = 0
    shot_fired = False
    countdown = False
    score = 0
    time_count = 360
    running = True
    while running:
        # Get all input events (Keyboard, Mouse, Joystick, etc
        if player_reload > 0:
            player_reload -= 1
        for event in pygame.event.get():

            # Look for specific event
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_reload <= 0:
                        player_reload = 10
                        missile = Missile(screen, player.rect.centerx - MISSILE_WIDTH / 2, player.rect.top - 18)
                        missile_group.add(missile)
                        all_sprites.add(missile)
                        fire_sound.play()
                if event.key == pygame.K_k:
                    player.kill()
                if event.key == pygame.K_1:
                    for enemy in enemy_group:
                        enemy.kill()

        # Game logic (Objects fired, object movement) goes here
        enemy_reload += 1
        if enemy_reload >= 30:
            enemy_reload = 0
            shot_fired = False
        for enemy in enemy_group:
            if shot_fired is False:
                check = random.randint(0, len(enemy_group) * 4)
                if check <= 1:
                    bomb = Bomb(screen, enemy.rect.centerx - MISSILE_WIDTH / 2, enemy.rect.bottom - 18)
                    bomb_group.add(bomb)
                    all_sprites.add(bomb)
                    shot_fired = True

        for item in list(enemy_group):
            if pygame.sprite.spritecollide(item, missile_group, True):
                enemy_kill.play()
                score += 1
                item.kill()
        player_death = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        player_damage = pygame.sprite.groupcollide(player_group, bomb_group, False, True)
        for item in list(block_group):
            if pygame.sprite.spritecollide(item, bomb_group, True):
                item.health -= 1
            if pygame.sprite.spritecollide(item, missile_group, True):
                item.health -= 1
        if not enemy_group:
            countdown = True
        if player_damage:
            player_health -= 1
            lost_life = health_group.sprites()[player_health]
            lost_life.kill()
            player_hurt.play()
        if player_death or player_health <= 0 or not player_group:
            end = True
            while end:
                screen.fill(BLACK)
                points.end_score(score)
                pygame.display.flip()
                for z in pygame.event.get():
                    if z.type == pygame.QUIT:
                        return 0
                    if z.type == pygame.KEYDOWN:
                        if z.key == pygame.K_SPACE:
                            return 100
                        else:
                            return 0
            running = False
        # Add drawings here
        collision = False
        for enemy in enemy_group:
            if enemy.rect.right >= SCREEN_WIDTH:
                collision = True
            elif enemy.rect.left <= 0:
                collision = True

        screen.fill(BLACK)
        if countdown:
            time_count -= 1
            points.draw_timer(time_count)
            if points.draw_timer(time_count) is True:
                round_multiplier += 0.2
                for row_val in range(1, 6):
                    for column_val in range(0, 12):
                        enemy = Enemy(row_val, column_val, round_multiplier)
                        enemy_group.add(enemy)
                time_count = 360
                countdown = False
        points.draw_score(score)
        enemy_group.draw(screen)
        missile_group.draw(screen)
        bomb_group.draw(screen)
        player_group.draw(screen)
        block_group.draw(screen)
        health_group.draw(screen)
        enemy_group.update(collision)
        all_sprites.update()

        pygame.display.flip()

        clock.tick(FPS)


playing = True
while playing:
    if game_play() == 100:
        pass
    else:
        playing = False


pygame.quit()
