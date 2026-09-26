import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player_class import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot
from powerups_class import Powerups
from powerup_manager import Powerup_manager

# EVERYTHING
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #creates the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Modern-Asteroid")

    # background
    background = pygame.image.load("background.png_original")

    powerup_manager = Powerup_manager()

    # makes the game run on x FPS
    clock = pygame.time.Clock()
    dt = 0.0

    # groups to uncluster the code
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    powerups_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, drawable_group, updatable_group)
    Powerups.containers = (powerups_group, drawable_group, updatable_group)

    # connects the asteroid field to the game loop
    asteroidfield_object = AsteroidField()

    # creates the player 
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:
        log_state()

        # closes the game from the x button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # makes the game run on 60 FPS
        dt = clock.tick(60) / 1000

        # updates everything updatable inside the Player class
        updatable_group.update(dt)

        #
        powerup_manager.update(dt)

        for current_powerup in powerups_group:
            # checks if the player is touching the powerup
            if current_powerup.position.distance_to(player_object.position) < 100:  # Larger collision area
                        
            # powerup timers
                if current_powerup.powerup_kinds == 1:
                    player_object.shield_active = True
                    player_object.shield_timer = 10.0

                elif current_powerup.powerup_kinds == 2:
                    player_object.rapid_fire_active = True
                    player_object.rapid_fire_timer = 10.0

                elif current_powerup.powerup_kinds == 3:
                    player_object.invincible_active = True
                    player_object.invincible_timer = 10.0
        
                log_event("picked up powerup")
                current_powerup.kill()
        
        print(f"Powerup manager spawning, timer: {powerup_manager.spawn_timer}")
        print(f"Powerups in group: {len(powerups_group)}")

        # check if an asteroid hits the player
        for current_asteroid in asteroids_group:
            if current_asteroid.collides_with(player_object):
                if player_object.shield_active:
                    log_event("asteroid blocked")

                    current_asteroid.kill()
                    player_object.shield_active = False
                else:
                    log_event("player_hit")
                    sys.exit()

        # checks if an bullet has hit an asteroid  
        for current_asteroid in asteroids_group:
            for shot in shots_group:
                if shot.collides_with(current_asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    current_asteroid.split(Asteroid)
        
        # puts the backround after the last frame 
        # to put the new frame on the screen
        screen.blit(background, (0, 0))

        # draws every object one at a time onto the screen 
        # from the Player class
        for drawable in drawable_group:
            drawable.draw(screen)

        # refreshes the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

# to run the game: uv run main.py
# start virtual machine: source .venv/bin/activate