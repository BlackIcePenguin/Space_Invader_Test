import pygame
import math
import random

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (11, 46, 2)
BROWN = (41, 21, 2)
YELLOW = (239, 184, 16)
MAGENTA = (204, 0, 153)
LIGHT_BROWN = (153, 102, 34)
SKY_BLUE = (179, 255, 255)
OCEAN_BLUE = (26, 117, 255)
PEACH = (255, 204, 153)
COLORS = [RED, GREEN, BLUE, WHITE]

# Create Math Constant
PI = math.pi

# To convert from Degrees to Radians -> angle * (pi / 180)

# Game Constants
FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Missile
MISSILE_WIDTH = 5
MISSILE_HEIGHT = 18

# Enemy Images
PLAYER = "assets/player.png"
RED_ALIEN = "assets/red.png"
GREEN_ALIEN = "assets/green.png"
YELLOW_ALIEN = "assets/yellow.png"

# Layout
LAYOUT = ["00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000001100000000011000000000011000000000110000000",
          "00000111111000001111110000001111110000011111100000",
          "00001111111100011111111000011111111000111111110000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000"]

LAYOUT_LENGTH = len(LAYOUT[0])
LAYOUT_HEIGHT = len(LAYOUT)
BLOCK_WIDTH = SCREEN_WIDTH / LAYOUT_LENGTH
BLOCK_HEIGHT = SCREEN_HEIGHT / LAYOUT_HEIGHT
