import pygame
from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
         pygame.draw.circle(screen, "grey88", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        nx = self.position[0]
        ny = self.position[1]
        ang = random.uniform(0, 180)
        ang2 = 180 - ang
#        vel1 = pygame.Vector2(0, 1).rotate(ang)
 #       vel2 = pygame.Vector2(0, 1).rotate(ang2)
        nrad = self.radius - ASTEROID_MIN_RADIUS 
        roid1 = Asteroid(nx, ny, nrad)
        roid1.velocity = self.velocity.rotate(ang) * 1.2
        roid2 = Asteroid(nx, ny, nrad)
        roid2.velocity = self.velocity.rotate(ang2) * 1.2
        return roid1, roid2