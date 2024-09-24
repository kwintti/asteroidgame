import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.is_colliding(player):
                print("Game Over")
                return
            for shot in shots:
                if item.is_colliding(shot):
                    item.kill()
                    shot.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        ret_ml = clock.tick(60)
        dt = ret_ml / 1000


if __name__ == "__main__":
    main()
