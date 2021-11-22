import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")

# Sounds
fire_sound = pygame.mixer.Sound("assets/shoot.wav")
enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")

# Sprite Groups
player_group = pygame.sprite.Group()  # Create sprite group for player
missile_group = pygame.sprite.Group()  # Create sprite group for missile
enemy_group = pygame.sprite.Group()  # Create sprite group for missile
all_sprites = pygame.sprite.Group()  # Group for all sprites

# Player
player = Player(PLAYER)  # Create player object
player_group.add(player)  # Load object into group
all_sprites.add(player)

# Enemy
for row_val in range(1, 6):
    for column_val in range(0, 12):
        enemy = Enemy(row_val, column_val)
        print(row_val)
        enemy_group.add(enemy)
        all_sprites.add(enemy)

# font_medium = pygame.font.Font(unifont.ttf, 16) Does Not Work RN

clock = pygame.time.Clock()

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
    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    if enemy_kills:
        enemy_kill.play()
    pygame.sprite.groupcollide(player_group, enemy_group, True, False)
    # Add drawings here
    screen.fill(BLACK)

    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    all_sprites.update()

    pygame.display.flip()

    clock.tick(FPS)

# Runs when main game loop ends
pygame.quit()

