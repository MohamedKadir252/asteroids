import pygame
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=COLORS,
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

def generate_random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))
COLORS = generate_random_color()