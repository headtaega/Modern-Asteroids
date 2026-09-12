import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

# child class of circleshape
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # draws the bullet onto the screen
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    # makes the bullet move in a straight line
    def update(self, dt) -> None:
        self.position += self.velocity * dt