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

        self.x = x * settings.TILE_SIZE + 5
        self.y = y * settings.TILE_SIZE + 5
        self.width = settings.COIN_SIZE
        self.height = settings.COIN_SIZE

        self.image = pygame.image.load(settings.COIN_IMG_10P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
