import random
from constants import POWERUP_LINE_WIDTH, POWERUP_SPAWN_TIMER, POWERUP_KINDS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event
import pygame

class Powerups(pygame.sprite.Sprite):
    
    def __init__(self, x, y, powerup_kinds) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.powerup_kinds = powerup_kinds

    def draw(self, screen):
        if self.powerup_kinds == 1:
            pygame.draw.rect(screen, "blue", (self.position.x, self.position.y, 20, 20), POWERUP_LINE_WIDTH)
        elif self.powerup_kinds == 2:
            pygame.draw.rect(screen, "red", (self.position.x, self.position.y, 21, 21), POWERUP_LINE_WIDTH)
        else:
            pygame.draw.rect(screen, "yellow", (self.position.x, self.position.y, 22, 22), POWERUP_LINE_WIDTH)









# ill see later if i need them
#class shield_powerup(Powerups):
    #def __init__(self, x, y, powerup_kinds):
        #super().__init__(x, y, powerup_kinds)

#class rapid_fire_powerup(Powerups):
    #def __init__(self, x, y, powerup_kinds):
        #super().__init__(x, y, powerup_kinds)

#class invincibility_powerup(Powerups):
    #def __init__(self, x, y, powerup_kinds):
        #super().__init__(x, y, powerup_kinds)