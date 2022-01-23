import pygame
import settings
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE
        self.y = y * settings.TILE_SIZE
        self.width = settings.ENEMY_SIZE
        self.height = settings.ENEMY_SIZE

        self.x_change = 0
        self.y_change = 0
        self.image = pygame.image.load(settings.GHOST_20P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.dir = random.randint(1, 4)

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.collide_blocks(self.dir)

        self.x_change = 0
        self.y_change = 0

    def collide_blocks(self, direction):
        pos = (self.rect.x, self.rect.y)
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction in (3, 4):
            # Crossing if's
            if pos in settings.UP_SIDE_CROSS:
                self.dir = random.choice([2, self.dir])
            elif pos in settings.DOWN_SIDE_CROSS:
                self.dir = random.choice([1, self.dir])
            elif pos in settings.LEFT_SIDE_CROSS or\
                    pos in settings.RIGHT_SIDE_CROSS:
                self.dir = random.choice([1, 2])
            elif pos in settings.CROSS:
                self.dir = random.choice([1, 2, self.dir])
            elif pos in settings.LEFT_UP_CORNER or\
                    pos in settings.RIGHT_UP_CORNER:
                self.dir = 2
            elif pos in settings.LEFT_DOWN_CORNER or\
                    pos in settings.RIGHT_DOWN_CORNER:
                self.dir = 1
            elif hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.width
                    self.dir = random.choice([1, 2, 3])
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.dir = random.choice([1, 2, 4])
        elif direction in (1, 2):
            if pos in settings.UP_SIDE_CROSS or\
                    pos in settings.DOWN_SIDE_CROSS:
                self.dir = random.choice([3, 4])
            elif pos in settings.LEFT_SIDE_CROSS:
                self.dir = random.choice([self.dir, 4])
            elif pos in settings.RIGHT_SIDE_CROSS:
                self.dir = random.choice([self.dir, 3])
            elif pos in settings.CROSS:
                self.dir = random.choice([self.dir, 3, 4])
            elif pos in settings.LEFT_UP_CORNER or\
                    pos in settings.LEFT_DOWN_CORNER:
                self.dir = 4
            elif pos in settings.RIGHT_UP_CORNER or\
                    pos in settings.RIGHT_DOWN_CORNER:
                self.dir = 3
            elif hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.height
                    self.dir = random.choice([2, 3, 4])
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.dir = random.choice([1, 3, 4])

    def movement(self):
        if self.dir == 1:   # Moving up
            self.y_change -= settings.ENEMY_SPEED
        elif self.dir == 2:     # Moving down
            self.y_change += settings.ENEMY_SPEED
        elif self.dir == 3:     # Moving left
            self.x_change -= settings.ENEMY_SPEED
        elif self.dir == 4:     # Moving right
            self.x_change += settings.ENEMY_SPEED
