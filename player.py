import pygame
import settings
from enemy import Enemy


class Player(pygame.sprite.Sprite):
    '''
    Class Player. Contains attributes:
    :param game: Game to be assigned with
    :param _layer: sets sprite layer
    :param groups: contains object sprite groups
    :param x: pixel position x (1 dot in settings.MAP equals 20 pixels)
    :param y: Pixel position y (1 dot in settings.MAP equals 20 pixels)
    :param width: Pixel width of sprite
    :param height: Pixel height of sprite
    :param images_facing: 4 direction Images of Pacman
    :param x_change: value of x position change
    :param y_change: value of y position change
    :param image: Current Pacman Image
    :param rect: pygame.image.rect object
    :param facing: direction in which Pacman is moving
    :param points: Pacman points
    :param boosted: True if Pacman ate Energizer, else False
    :param boost_start_time: Time when Pacman ate Energizer
    :param kills: Pacman current kills (reset when boost ends)
    :param coins_eaten: Pacman coins score to check if ate all

    '''
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
        self.coins_eaten = 0

    def update(self, player=None):
        '''
        Pacman update Method calling Animate, Movement, Block, Coin
        and Energizer collison and checking if win
        '''
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_coins()
        self.collide_energizer()
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_coins()
        self.check_win()
        self.collide_energizer()
        if self.boosted:
            self.check_boost_time()

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        '''
        Pacman movement Method. Gets keybpard pressed keys.
        Sets x/y_change and facing attributes
        '''
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
        '''
        Pacman Block collison detection
        '''
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
        '''
        Pacman Coin collison detection and adding points
        '''
        hits = pygame.sprite.spritecollide(self, self.game.coins, True)
        if hits:
            self.points += 1
            self.coins_eaten += 1

    def check_win(self):
        if self.coins_eaten == 283:
            self.game.playing = False
            self.game.won = True

    def animate(self):
        '''
        changing image of Pacman (facing)
        '''
        self.image = self.images_facing[self.facing-1]

    def collide_energizer(self):
        '''
        Checks for collison with Energizer
        '''
        hits = pygame.sprite.spritecollide(self, self.game.energizers, True)
        if hits:
            self.boosted = True
            self.boost_start_time = pygame.time.get_ticks()
            hits = None

    def check_boost_time(self):
        '''
        Method checks if Pacman boost time has ended
        '''
        if pygame.time.get_ticks() - self.boost_start_time > 6000:
            self.boosted = False
            self.boost_start_time = 0
            for i in range(self.kills):
                pos = settings.ENEMY_INIT_POS[i]
                Enemy(self.game, pos[0], pos[1])
            self.kills = 0
