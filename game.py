import pygame
from enemy import Enemy
from files import (
    ScoreTable,
    save,
    load
)
from menu import Button
from player import Player
import settings
from maze import Block, Coin, Energizer


def blit_multiline_text(surface, text, pos, font):
    color = settings.WHITE
    words = [word for word in text.splitlines()]
    max_width, max_height = surface.get_size()
    x, y = pos
    word_surface = font.render('HIGH SCORES', 0, color)
    surface.blit(word_surface, (x, y))
    y += 45
    for word in words:
        word_surface = font.render(word, 0, color)
        word_height = word_surface.get_size()[1]
        surface.blit(word_surface, (x, y))
        y += word_height + 2


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
        self.high_score_font = pygame.font.Font(self.font_name, 40)
        self.running = True
        self.running_highscores = False
        self.intro_img = pygame.image.load(settings.INTRO_IMG).convert()
        self.highscore_list = ScoreTable(load(settings.HIGHSCORES_CSV))
        self.won = False

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
        text = f"Score = {score}"
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

    def game_over(self):
        player_score = self.player.points
        for sprite in self.all_sprites:
            sprite.kill()
        self.highscore_list.add_score(self.player.points)
        save(settings.HIGHSCORES_CSV, self.highscore_list.score_table)
        self.intro_screen(True, player_score)

    def high_scores(self):
        if self.running_highscores:
            back_button = Button(
                290, 450, 110, 50, settings.WHITE, settings.BLUE, 'BACK', 42
            )
            highscores_str = str(self.highscore_list)
            while self.running_highscores:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running_highscores = False
                        self.running = False
                        return False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if back_button.is_pressed(mouse_pos, mouse_pressed):
                    self.running_highscores = False
                self.screen_intro.fill(settings.BLACK)
                self.screen_intro.blit(back_button.image, back_button.rect)
                blit_multiline_text(
                    self.screen_intro, highscores_str,
                    (230, 15),
                    self.high_score_font
                )
                pygame.display.update()
        return True

    def intro_screen(self, second, player_score=None):
        intro = True
        play_button = Button(
            290, 300, 110, 50, settings.WHITE, settings.BLUE, 'PLAY', 42
        )
        highscores_button = Button(
            220, 370, 260, 50, settings.WHITE, settings.BLUE, 'HIGH SCORES', 42
        )
        self.screen_intro = pygame.display.set_mode(
            (settings.INTRO_WIDTH, settings.INTRO_HEIGHT)
        )
        if second:
            won_text = self.score_font.render(
                'Congrats! You Won!', False, (255, 255, 255)
            )
            dead_text = self.score_font.render(
                'You Died :(', False, (255, 255, 255)
            )
            score_message = f'Score = {player_score}'
            score_text = self.score_font.render(
                score_message, False, (255, 255, 255)
            )
        while intro and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if highscores_button.is_pressed(mouse_pos, mouse_pressed):
                self.running_highscores = True
                intro = self.high_scores()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen_intro.blit(self.intro_img, (0, 0))
            self.screen_intro.blit(play_button.image, play_button.rect)
            self.screen_intro.blit(
                highscores_button.image, highscores_button.rect
            )
            if self.won and second:
                self.screen.blit(won_text, (190, 430))
                self.screen.blit(score_text, (260, 460))
            elif not self.won and second:
                self.screen.blit(dead_text, (260, 430))
                self.screen.blit(score_text, (260, 460))
            self.clock.tick(settings.FPS)
            pygame.display.update()
        self.screen = pygame.display.set_mode(
            (settings.WIN_WIDTH, settings.WIN_HEIGHT)
        )
        if second and self.running:
            self.won = False
            self.new()
            self.main()
