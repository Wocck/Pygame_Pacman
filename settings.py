# Main Window
WIN_WIDTH = 560
WIN_HEIGHT = 680
TILE_SIZE = 20

# Layers
PLAYER_LAYER = 5
ENEMY_LAYER = 4
COINS_LAYER = 3
MAZE_LAYER = 2
BLOCK_LAYER = 1

# FPS
FPS = 60

# PLAYER
PLAYER_SPEED = 3
PLAYER_SIZE = 18

# ENEMIES
ENEMY_SPEED = 2
ENEMY_SIZE = 20

# COINS
COIN_SIZE = 5

# IMAGES
PACMAN_IMG_20P = 'images/pac_man_20pix.png'
PACMAN_REL_IMG_20P = 'images/pac_man_real_20pix.png'
PACMAN_IMG_18P = 'images/pac_man_18pix.png'
PACMAN_IMG_17P = 'images/pac_man_17pix.png'
REAL_PACMAN_18P = 'images/real_pacman_18pix.png'
PACMAN_UP = 'images/pacman_up.png'
PACMAN_DOWN = 'images/pacman_d.png'
PACMAN_RIGHT = 'images/pacman_r.png'
PACMAN_LEFT = 'images/pacman_l.png'

MAZE_IMG = 'images/maze.png'
COIN_IMG_16P = 'images/virus_2.png'
COIN_IMG_5P = 'images/coin_5pix.png'
COIN_IMG_10P = 'images/dot_10pix.png'
ENEMY_IMG_20P = 'images/enemy_20pix.png'
GHOST_20P = 'images/ghost_20pix.png'
BLUE_GHOST_20P = 'images/blue_ghost_20pix.png'
FLASH_20P = 'images/flash_20pix.png'
FLASH_15P = 'images/flash_15pix.png'

# FONTS
FONT_ONE = 'fonts/8-BIT WONDER.TTF'
FONT_TWO = 'fonts/ARCADE.TTF'
FONT_THREE = 'fonts/arial.ttf'

# COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)

# Maze Grid
MAP = [
    '............................',
    '.O###########..###########O.',
    '.#....#.....#..#.....#....#.',
    '.#....#.....#..#.....#....#.',
    '.#....#.....#..#.....#....#.',
    '.##########################.',
    '.#....#..#........#..#....#.',
    '.#....#..#........#..#....#.',
    '.######..####..####..######.',
    '......#.....#..#.....#......',
    '......#.....#..#.....#......',
    '......#..##########..#......',
    '......#..#...00...#..#......',
    '......#..#.0.EE.0.#..#......',
    '......####.0.00.0.####......',
    '......#..#.0.EE.0.#..#......',
    '......#..#........#..#......',
    '......#..##########..#......',
    '......#..#........#..#......',
    '......#..#........#..#......',
    '.O###########..###########O.',
    '.#....#.....#..#.....#....#.',
    '.#....#.....#..#.....#....#.',
    '.###..################..###.',
    '...#..#..#........#..#..#...',
    '...#..#..#........#..#..#...',
    '.######..####..####..######.',
    '.#..........#..#..........#.',
    '.#..........#..#..........#.',
    '.############PG############.',
    '............................'
]

# ``|`` =
UP_SIDE_CROSS = [
    (120, 20),
    (420, 20),
    (180, 100),
    (360, 100),
    (180, 460),
    (360, 460)
]

# _|_
DOWN_SIDE_CROSS = [
    (240, 100),
    (300, 100),
    (240, 220),
    (300, 220),
    (180, 400),
    (360, 400),
    (240, 460),
    (300, 460),
    (60, 520),
    (480, 520),
    (240, 580),
    (300, 580)
]

# |-
LEFT_SIDE_CROSS = [
    (420, 160),
    (120, 280),
    (360, 280),
    (180, 340),
    (120, 460)
]

# -|
RIGHT_SIDE_CROSS = [
    (120, 160),
    (180, 280),
    (420, 280),
    (360, 340),
    (420, 460)
]

# -|-
CROSS = [
    (120, 100),
    (420, 100),
    (120, 400),
    (420, 400)
]

# R = |``
LEFT_UP_CORNER = [
    (20, 20),
    (300, 20),
    (300, 160),
    (180, 220),
    (20, 400),
    (300, 400),
    (480, 460),
    (20, 520),
    (300, 520)
]

# L = ``|
RIGHT_UP_CORNER = [
    (240, 20),
    (520, 20),
    (240, 160),
    (360, 220),
    (240, 400),
    (520, 400),
    (60, 460),
    (240, 520),
    (520, 520)
]

# M = |_
LEFT_DOWN_CORNER = [
    (20, 160),
    (180, 160),
    (20, 460),
    (180, 520),
    (420, 520),
    (20, 580)
]

# N = _|
RIGHT_DOWN_CORNER = [
    (360, 160),
    (520, 160),
    (520, 460),
    (120, 520),
    (360, 520),
    (520, 580)
]

ENEMY_INIT_POS = [
    (13, 13),
    (14, 13),
    (13, 15),
    (14, 15)
]
