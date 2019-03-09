import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

    # Initialize game and create a screen object
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting, screen)
    pygame.display.set_caption("Alien Invasion")

    # Make a group to store bullet in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()



