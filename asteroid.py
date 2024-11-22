import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,  self.radius, 2)


    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity_1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            velocity_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

            new_asteroid_1.velocity = velocity_1 * 1.2
            new_asteroid_2.velocity = velocity_2 * 1.2