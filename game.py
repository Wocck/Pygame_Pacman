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
    '''
    Function bliting Multiline text to surface.
    Contain arguments:
    :param surface: pygame.display where text should be blit
    :type surface: pygame.display
    :param text: text to blit
    :type text: str
    :param pos: (x, y) positoon tuple
    :param font: pygame.font.Font font to render text with

    '''
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
    '''
    Class Game. Contains all game related stuff and initializes pygame.
    Contains all game and menu handling, updating sprites and drawing methods.
    Contains attributes:
    :param screen_intro: Menu screen display
    :param clock: pygame.time.Clock() (to set FPS)
    :param score_font: font for displaying text
    :param running: Boolean controling whole program
    :param running_highscores: Boolean controling high scores window
    :param intro_img: pygame.image contains menu image
    :param highscore_list: list containing all high scores loaded from csv file
    :type highscore_list: ScoreTable
    :param self.won: Boolean controls if Pacman won or lost game

    '''
    def __init__(self) -> None:
        pygame.init()
        self.screen_intro = pygame.display.set_mode(
            (settings.INTRO_WIDTH, settings.INTRO_HEIGHT)
        )
        self.maze_image = pygame.image.load(settings.MAZE_IMG).convert()
        self.clock = pygame.time.Clock()
        font_name = settings.FONT_TWO
        self.score_font = pygame.font.Font(font_name, 40)
        self.running = True
        self.running_highscores = False
        self.intro_img = pygame.image.load(settings.INTRO_IMG).convert()
        self.highscore_list = ScoreTable(load(settings.HIGHSCORES_CSV))
        self.won = False

    def create_map(self):
        '''
        Method creating maze  with Ghosts, Pacman, Coins, Energizers
        and Blocks from settings.MAP list
        '''
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

    def new(self):
        '''
        Method creating sprites groups and calling create_map method

        '''
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()
        self.energizers = pygame.sprite.LayeredUpdates()
        self.player_sprit = pygame.sprite.LayeredUpdates()
        self.create_map()

    def events(self):
        '''
        Method with Game Loop events, checking if player didn't exit from game
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def update(self):
        '''
        Method updating all_sprites group
        '''
        self.all_sprites.update(self.player)

    def draw(self):
        '''
        Method drawing maze, score and all_sprites group and updating display
        '''
        self.screen.fill(settings.BLACK)
        self.screen.blit(self.maze_image, (0, 0))
        self.draw_score()
        self.all_sprites.draw(self.screen)
        self.clock.tick(settings.FPS)
        pygame.display.update()

    def draw_score(self):
        '''
        Method drawing Score while playing Game
        '''
        score = self.player.points
        text = f"Score = {score}"
        text_surface = self.score_font.render(text, False, settings.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.x = 170
        text_rect.y = 630
        self.screen.blit(text_surface, text_rect)

    def main(self):
        '''
        Just Game loop controlled by playing boolean
        calling all game related methods
        '''
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        '''
        Game over Method kills (deletes) all sprites, saves highscores list
        and runs intro screen Method with True and player_score
        '''
        player_score = self.player.points
        for sprite in self.all_sprites:
            sprite.kill()
        self.highscore_list.add_score(self.player.points)
        save(settings.HIGHSCORES_CSV, self.highscore_list.score_table)
        self.intro_screen(True, player_score)

    def high_scores(self):
        '''
        Method displaying highscores window
        Creates button and list of highscores to display
        than checks if player quited, than if player clicked 'back' button
        than blits to screen highscores with blit_multiline_text() function
        :returns: True if player exited with 'back' button if closed False
        :rtype: bool
        '''
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
                    self.score_font
                )
                pygame.display.update()
        return True

    def intro_screen(self, second, player_score=None):
        '''
            Method displaying Menu screen
            param: second: determines if this is first execution of method
            type: second: bool
            param: player_score: saved player score to display in menu window
            type: player_score: int
            Creates 2 buttons for Playing and entering high scores window
            If second execution (or third,...) display game result and points
            Than display rest of menu window with buttons
            If Highscores button is prest run highscores method
            if Play button is pressed exit while loop and create new game
            The only way to exit this method is to run new game or close window

        '''
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
