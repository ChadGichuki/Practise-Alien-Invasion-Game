import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manages the bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's location"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet vetical position as a decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
