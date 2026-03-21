from constants import *
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rangle = random.uniform(20, 50)
            first_new_movement = self.velocity.rotate(rangle)
            second_new_movement = self.velocity.rotate(-rangle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_new = Asteroid(self.position.x, self.position.y, new_radius)
            second_new = Asteroid(self.position.x, self.position.y, new_radius)

            first_new.velocity = first_new_movement * 1.2
            second_new.velocity = second_new_movement * 1.2