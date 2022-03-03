import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire bullets if limit is not reached"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw the bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """update position of the bullets and delete old bullets"""
    bullets.update()

    # Delete bullets that have reached the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """Create a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_of_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens
    for alien_number in range(number_of_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
