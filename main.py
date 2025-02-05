import sys
import pygame
from shot import Shot
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)            
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collides(player):
                print(":::::::Game over!:::::::")
                sys.exit()
            for shot in shots:
                if asteroid.check_collides(shot):
                    shot.kill() 
                    asteroid.split()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
