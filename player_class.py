import pygame
import settings
import math
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.layer = settings.PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.starting_pos = (x, y)
        self.width = settings.TILESIZE
        self.height = settings.TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(settings.RED)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.starting_pos

    def update(self):
        pass

    def movement(self):
        keys = pygame.key.get_pressed()
