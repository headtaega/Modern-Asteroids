import pygame
import random
from logger import log_event
from powerups_class import Powerups
from constants import POWERUP_SPAWN_TIMER, POWERUP_KINDS, SCREEN_HEIGHT, SCREEN_WIDTH

class Powerup_manager:
    containers: pygame.sprite.Group

    def __init__(self) -> None:
        self.spawn_timer = 0.0

    # generates a random point on the screen
    def get_random_point(self):
        return (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

    # cooldown, chooses kind, gets a random pos
    # checks if timer is okay and then spawns the powerup
    def update(self, dt) -> None:
            self.spawn_timer += dt
            if self.spawn_timer > POWERUP_SPAWN_TIMER:
                self.spawn_timer = 0
                x, y = self.get_random_point()
                self.kind = random.randint(1, POWERUP_KINDS)
                Powerups(x, y, self.kind)
    