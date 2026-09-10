import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

# the asteroid class a child class of Circleshape
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # draws the asteriod onto the screen
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # makes the asteroid move in a straight line
    def update(self, dt) -> None:
        self.position += self.velocity * dt
