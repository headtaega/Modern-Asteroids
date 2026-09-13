import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player_class import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

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

    # makes the game run on x FPS
    clock = pygame.time.Clock()
    dt = 0.0

    # groups to uncluster the code
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, drawable_group, updatable_group)

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

        # checks if player has collided with an asteroid
        for asteroid in asteroids_group:
            if asteroid.collides_with(player_object):
                log_event("player_hit")
                print("Game over")
                sys.exit()
            else:
                continue

        # cheks if an bullet has hit an asteroid and 
        # in that case removes both of them   
        for current_asteroid in asteroids_group:
            for shot in shots_group:
                if shot.collides_with(current_asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    current_asteroid.split(Asteroid)
                else:
                    continue
        
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