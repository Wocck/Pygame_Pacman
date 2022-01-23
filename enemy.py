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
        self.image = pygame.image.load(settings.ENEMY_IMG_20P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.dir = random.randint(1, 4)

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.width
                    self.dir = random.choice([1, 2, 3])
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.dir = random.choice([1, 2, 4])
            if (self.rect.x, self.rect.y) in settings.XY_CROSS:
                self.dir = random.choice([1, 2, self.dir])
            if (self.rect.x, self.rect.y) in settings.UP_CROSS_X_DIR:
                self.dir = random.choice([1, self.dir])
            if (self.rect.x, self.rect.y) in settings.DOWN_CROSS_X_DIR:
                self.dir = random.choice([2, self.dir])
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.height
                    self.dir = random.choice([2, 3, 4])
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.dir = random.choice([1, 3, 4])
            if (self.rect.x, self.rect.y) in settings.XY_CROSS:
                self.dir = random.choice([3, 4, self.dir])
            if (self.rect.x, self.rect.y) in settings.LEFT_CROSS_Y_DIR:
                self.dir = random.choice([3, self.dir])
            if (self.rect.x, self.rect.y) in settings.RIGHT_CROSS_Y_DIR:
                self.dir = random.choice([4, self.dir])

    def movement(self):
        if self.dir == 1:   # Moving up
            self.y_change -= settings.ENEMY_SPEED
        elif self.dir == 2:     # Moving down
            self.y_change += settings.ENEMY_SPEED
        elif self.dir == 3:     # Moving left
            self.x_change -= settings.ENEMY_SPEED
        elif self.dir == 4:     # Moving right
            self.x_change += settings.ENEMY_SPEED
