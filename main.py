import pygame
import player_class
import settings
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WIN_WIDTH, settings.WIN_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.font_name = '8-BIT WONDER.TTF'
        self.running = True

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        self.player = player_class.Player(self, 1, 2)

    def events(self):
        # Game Loop Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def update(self):
        # Game Loop Updates
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(settings.FPS)
        pygame.display.update()

    def main(self):
        # Game Loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
