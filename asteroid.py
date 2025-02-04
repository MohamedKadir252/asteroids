import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        mouvement = self.velocity * dt
        self.position += mouvement
