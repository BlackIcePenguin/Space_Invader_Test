import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")

player_group = pygame.sprite.Group()  # Create sprite group for player
player = Player("assets/sprite_ship_3.png")  # Create player object
player_group.add(player)  # Load object into group

clock = pygame.time.Clock()

running = True

while running:
    # Get all input events (Keyboard, Mouse, Joystick, etc
    for event in pygame.event.get():

        # Look for specific event
        if event.type == pygame.QUIT:
            running = False

    # Game logic (Objects fired, object movement) goes here

    # Add drawings here
    screen.fill(BLACK)

    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()

    clock.tick(FPS)

# Runs when main game loop ends
pygame.quit()

