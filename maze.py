import pygame
import settings


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.BLOCK_LAYER
        self.groups = self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE
        self.y = y * settings.TILE_SIZE
        self.width = settings.TILE_SIZE
        self.height = settings.TILE_SIZE
        self.image = pygame.Surface([self.width, self.height])

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Coin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.COINS_LAYER
        self.groups = self.game.coins, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE + 7.5
        self.y = y * settings.TILE_SIZE + 7.5
        self.width = settings.COIN_SIZE
        self.height = settings.COIN_SIZE

        self.image = pygame.image.load(settings.COIN_IMG_5P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Energizer(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.COINS_LAYER
        self.groups = self.game.energizers, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE + 2.5
        self.y = y * settings.TILE_SIZE + 2.5
        self.width = 15
        self.height = 15

        self.image = pygame.image.load(settings.FLASH_15P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
