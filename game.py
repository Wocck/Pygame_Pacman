import pygame
from enemy import Enemy
from player import Player
import settings
from maze_grid import Block, Coin


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WIN_WIDTH, settings.WIN_HEIGHT)
        )
        self.maze_image = pygame.image.load(settings.MAZE_IMG).convert()
        self.clock = pygame.time.Clock()
        self.font_name = settings.FONT_ONE
        self.score_font = pygame.font.Font(self.font_name, 35)
        self.running = True

    def create_map(self):
        for i, row in enumerate(settings.MAP):
            for j, column in enumerate(row):
                if column == ".":
                    Block(self, j, i)
                elif column == "P":
                    self.player = Player(self, j, i)
                elif column == "#":
                    Coin(self, j, i)
                elif column == "E":
                    Enemy(self, j, i)
                elif column == "G":
                    print(f'({j*20}, {i*20}),')

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.maze = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()
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
        self.screen.fill(settings.BLACK)
        self.screen.blit(self.maze_image, (0, 0))
        self.draw_score()
        self.all_sprites.draw(self.screen)
        self.clock.tick(settings.FPS)
        pygame.display.update()

    def draw_score(self):
        score = self.player.points
        text = f"Score = {score}"
        text_surface = self.score_font.render(text, False, settings.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.x = 0
        text_rect.y = 620
        self.screen.blit(text_surface, text_rect)

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
