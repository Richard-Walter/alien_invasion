import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):

        super(Alien, self).__init__()
        """Initialise the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()   # pygame treats elements as rectangles

        # Start each new alien at the top left of the screen
        self.rect.centerx = self.rect.width
        self.rect.bottom = self.rect.height

        # Store aliens exact position
        self.x = float(self.rect.x)

        # # Movement flag
        # self.moving_right = False
        # self.moving_left = False

    def update(self):

        """Move the alien right or left"""
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):

        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):

        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            print("At the edge of the right screen")
            return True
        elif self.rect.left <= 0:
            print("At the edge of the left screen")
            return True


