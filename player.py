import pygame
from circleshape import *
from constants import *
from shot import *
class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_rate = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((dt*-1))
        if keys[pygame.K_a]:
            self.rotate((dt*-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if self.shot_rate <= 0:
            if keys[pygame.K_SPACE]:
                self.shoot(dt)
        if self.shot_rate > 0:
            self.shot_rate -= dt

    def shoot(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        sa = self.position + forward * self.radius
        sx = sa[0]  
        sy = sa[1] 
        rad = SHOT_RADIUS
        shot = Shot(sx, sy, rad)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shot_rate += PLAYER_SHOOT_COOLDOWN
        return shot