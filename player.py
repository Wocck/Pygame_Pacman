import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=280, y=280) -> None:
        self.game = game
        self._layer = settings.PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.starting_pos = (x, y)
        self.x_change = 0
        self.y_change = 0

        self.width = settings.PLAYER_SIZE
        self.height = settings.PLAYER_SIZE

        self.image = pygame.image.load('pac_man_20pix.png')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.starting_pos

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

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

    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
