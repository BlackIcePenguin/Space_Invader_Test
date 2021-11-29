import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Bomb, Block

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")

# Sounds
fire_sound = pygame.mixer.Sound("assets/shoot.wav")
enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")
player_hurt = pygame.mixer.Sound("assets/ShipHit.wav")

# Sprite Groups
player_group = pygame.sprite.Group()  # Create sprite group for player
missile_group = pygame.sprite.Group()  # Create sprite group for missile
enemy_group = pygame.sprite.Group()  # Create sprite group for missile
bomb_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()  # Group for all sprites

# Player
player = Player(PLAYER)  # Create player object
player_group.add(player)  # Load object into group
all_sprites.add(player)

# Enemy
for row_val in range(1, 6):
    for column_val in range(0, 12):
        enemy = Enemy(row_val, column_val)
        enemy_group.add(enemy)
        all_sprites.add(enemy)

for row_val in range(0, 50):
    for column_val in range(0, 20):
        if LAYOUT[column_val][row_val] == '1':
            block = Block(screen, row_val, column_val, BLUE)
            block_group.add(block)
            all_sprites.add(block)

# font_medium = pygame.font.Font(unifont.ttf, 16) Does Not Work RN

clock = pygame.time.Clock()

player_health = 3
enemy_reload = 0
shot_fired = False

running = True

while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile = Missile(screen, player.rect.centerx - MISSILE_WIDTH / 2, player.rect.top - 18)
                missile_group.add(missile)
                all_sprites.add(missile)
                fire_sound.play()

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

    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    if enemy_kills:
        enemy_kill.play()
    player_death = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
    player_damage = pygame.sprite.groupcollide(player_group, bomb_group, False, True)
    if player_damage:
        player_health -= 1
        player_hurt.play()
    if player_death or player_health <= 0:
        player.kill()
    # Add drawings here
    screen.fill(BLACK)

    enemy_group.draw(screen)
    missile_group.draw(screen)
    bomb_group.draw(screen)
    player_group.draw(screen)
    block_group.draw(screen)
    all_sprites.update()

    pygame.display.flip()

    clock.tick(FPS)

# Runs when main game loop ends
pygame.quit()

