import pygame
import settings
from enemy import Enemy


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self._layer = settings.PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.player_sprit

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * settings.TILE_SIZE
        self.y = y * settings.TILE_SIZE
        self.x_change = 0
        self.y_change = 0

        self.width = settings.PLAYER_SIZE
        self.height = settings.PLAYER_SIZE

        self.images_facing = [
            pygame.image.load(settings.PACMAN_UP).convert(),
            pygame.image.load(settings.PACMAN_DOWN).convert(),
            pygame.image.load(settings.PACMAN_LEFT).convert(),
            pygame.image.load(settings.PACMAN_RIGHT).convert()
        ]
        self.image = self.images_facing[3]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = 4
        self.points = 0

        self.boosted = False
        self.boost_start_time = 0
        self.kills = 0

    def update(self, player=None):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_coins()
        self.collide_energizer()
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_coins()
        self.collide_energizer()
        if self.boosted:
            self.check_boost_time()

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_change += settings.PLAYER_SPEED
            self.facing = 4
        if keys[pygame.K_LEFT]:
            self.x_change -= settings.PLAYER_SPEED
            self.facing = 3
        if keys[pygame.K_UP]:
            self.y_change -= settings.PLAYER_SPEED
            self.facing = 1
        if keys[pygame.K_DOWN]:
            self.y_change += settings.PLAYER_SPEED
            self.facing = 2

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

    def collide_coins(self):
        hits = pygame.sprite.spritecollide(self, self.game.coins, True)
        if hits:
            self.points += 1

    def animate(self):
        self.image = self.images_facing[self.facing-1]

    def collide_energizer(self):
        hits = pygame.sprite.spritecollide(self, self.game.energizers, True)
        if hits:
            self.boosted = True
            self.boost_start_time = pygame.time.get_ticks()
            hits = None

    def check_boost_time(self):
        if pygame.time.get_ticks() - self.boost_start_time > 8000:
            self.boosted = False
            self.boost_start_time = 0
            for i in range(self.kills):
                pos = settings.ENEMY_INIT_POS[i]
                Enemy(self.game, pos[0], pos[1])
            self.kills = 0
