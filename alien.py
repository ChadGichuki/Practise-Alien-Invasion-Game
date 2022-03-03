import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to model an alien"""

    def __init__(self, ai_settings, screen):
        """Initialize Alien attributes"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set starting position at tope left of screen
        # but with space equal to its width and height

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Accurate positioning
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at the position on the screen"""
        self.screen.blit(self.image, self.rect)
