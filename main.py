import pygame
from player_class import Player
import settings
from maze_grid import Block


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WIN_WIDTH, settings.WIN_HEIGHT)
        )
        self.maze_image = pygame.image.load('maze.png').convert()
        self.clock = pygame.time.Clock()
        self.font_name = '8-BIT WONDER.TTF'
        self.running = True

    def create_map(self):
        for i, row in enumerate(settings.map):
            for j, column in enumerate(row):
                if column == '.':
                    Block(self, j, i)
                elif column == 'P':
                    Player(self, j * 20, i * 20)    # 1 dot == 20 Pixels
                else:
                    pass

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.maze = pygame.sprite.LayeredUpdates()
        self.create_map()

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
        self.screen.blit(self.maze_image, (0, 0))
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
