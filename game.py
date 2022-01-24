import pygame
from enemy import Enemy
from menu import Button
from player import Player
import settings
from maze_grid import Block, Coin, Energizer


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen_intro = pygame.display.set_mode(
            (settings.INTRO_WIDTH, settings.INTRO_HEIGHT)
        )
        self.maze_image = pygame.image.load(settings.MAZE_IMG).convert()
        self.clock = pygame.time.Clock()
        self.font_name = settings.FONT_TWO
        self.score_font = pygame.font.Font(self.font_name, 40)
        self.running = True
        self.intro_img = pygame.image.load(settings.INTRO_IMG).convert()

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
                elif column == "O":
                    Energizer(self, j, i)
                # elif column == "G":
                #     print(f'{j*20}, {i*20}')

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.maze = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()
        self.energizers = pygame.sprite.LayeredUpdates()
        self.player_sprit = pygame.sprite.LayeredUpdates()
        self.create_map()

    def events(self):
        # Game Loop Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def update(self):
        # Game Loop Updates
        self.all_sprites.update(self.player)

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.screen.blit(self.maze_image, (0, 0))
        self.draw_score()
        self.all_sprites.draw(self.screen)
        self.clock.tick(settings.FPS)
        pygame.display.update()

    def draw_score(self):
        score = self.player.points
        text = f"Score = {score}/287"
        text_surface = self.score_font.render(text, False, settings.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.x = 170
        text_rect.y = 630
        self.screen.blit(text_surface, text_rect)

    def main(self):
        # Game Loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        # self.running = False

    def game_over(self):
        for sprite in self.all_sprites:
            sprite.kill()
        self.intro_screen(True)

    def intro_screen(self, second):
        intro = True
        play_button = Button(
            290, 300, 110, 50, settings.WHITE, settings.BLUE, 'PLAY', 42
        )
        self.screen_intro = pygame.display.set_mode(
            (settings.INTRO_WIDTH, settings.INTRO_HEIGHT)
        )
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen_intro.blit(self.intro_img, (0, 0))
            self.screen_intro.blit(play_button.image, play_button.rect)
            self.clock.tick(settings.FPS)
            pygame.display.update()
        self.screen = pygame.display.set_mode(
            (settings.WIN_WIDTH, settings.WIN_HEIGHT)
        )
        if second and self.running:
            self.new()
            self.main()
