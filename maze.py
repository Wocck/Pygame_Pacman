import pygame
import settings


class Block(pygame.sprite.Sprite):
    '''
    Class Block. Contains attributes:
    :param game: Game to be assigned with
    :param _layer: sets sprite layer
    :param groups: contains object sprite groups
    :param x: pixel position x (1 dot in settings.MAP equals 20 pixels)
    :param y: Pixel position y (1 dot in settings.MAP equals 20 pixels)
    :param width: Pixel width of sprite
    :param height: Pixel height of sprite
    :param image: just pygame.surface
    '''
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
    '''
    Class Block. Contains attributes:
    :param game: Game to be assigned with
    :param _layer: sets sprite layer
    :param groups: contains object sprite groups
    :param x: pixel position x (1 dot in settings.MAP equals 20 pixels)
    :param y: Pixel position y (1 dot in settings.MAP equals 20 pixels)
    :param width: Pixel width of sprite
    :param height: Pixel height of sprite
    :param image: coin image
    '''
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.COINS_LAYER
        self.groups = self.game.coins, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE + 7.5  # +7.5 for centering
        self.y = y * settings.TILE_SIZE + 7.5  # +2.5 for centering
        self.width = settings.COIN_SIZE
        self.height = settings.COIN_SIZE

        self.image = pygame.image.load(settings.COIN_IMG_5P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Energizer(pygame.sprite.Sprite):
    '''
    Class Block. Contains attributes:
    :param game: Game to be assigned with
    :param _layer: sets sprite layer
    :param groups: contains object sprite groups
    :param x: pixel position x (1 dot in settings.MAP equals 20 pixels)
    :param y: Pixel position y (1 dot in settings.MAP equals 20 pixels)
    :param width: Pixel width of sprite
    :param height: Pixel height of sprite
    :param image: Energizer image
    '''
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.COINS_LAYER
        self.groups = self.game.energizers, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE + 2.5  # +2.5 for centering
        self.y = y * settings.TILE_SIZE + 2.5  # +2.5 for centering
        self.width = 15
        self.height = 15

        self.image = pygame.image.load(settings.FLASH_15P).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
