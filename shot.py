import circleshape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=SHOT_RADIUS)

    rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += dt * pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
