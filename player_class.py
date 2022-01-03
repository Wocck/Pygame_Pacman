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
        self.x_change = 0
        self.y_change = 0

        self.width = settings.TILESIZE
        self.height = settings.TILESIZE

        self.image = pygame.image.load('pac_man.png')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.starting_pos

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_change += settings.PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            self.x_change -= settings.PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.y_change -= settings.PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.y_change += settings.PLAYER_SPEED
