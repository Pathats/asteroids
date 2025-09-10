import random
from constants import ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            angle = random.uniform(20, 30)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x = self.position[0]
            y = self.position[1]
            asteroid_one = Asteroid(x, y, new_radius)
            asteroid_one.velocity = self.velocity.rotate(angle) * 2

            asteroid_two = Asteroid(x, y, new_radius)
            asteroid_two.velocity = self.velocity.rotate(-angle)
            

