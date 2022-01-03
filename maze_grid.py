import pygame
import settings


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = settings.BLOCK_LAYER
        self.groups = self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.BLOCK_SIZE
        self.y = y * settings.BLOCK_SIZE
        self.width = settings.BLOCK_SIZE
        self.height = settings.BLOCK_SIZE

        self.image = pygame.Surface([self.width, self.height])

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
