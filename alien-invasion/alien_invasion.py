import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    play_button = Button(settings, screen, "Play")
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()