import pygame
from src.settings import settings


class Button:
    '''
    Class Button. Contains attributes:
    :param font: pygame.font
    :param content: text
    :param x: pixel position x
    :param y: Pixel position y
    :param width: Pixel width of button
    :param height: Pixel height of button
    :param fg: foreground
    :param bg: background
    :param image: pygame.Surface

    '''
    def __init__(self, x, y, width, height, fg, bg, content, fontsize) -> None:
        font = settings.FONT_TWO
        self.font = pygame.font.Font(font, fontsize)
        self.content = content

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(
            center=(self.width/2+5, self.height/2+5)
        )
        # 5 cause of font made diffrence
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        '''
        Method checking if mouse pressed button
        '''
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
        return False
