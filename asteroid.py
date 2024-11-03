import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt