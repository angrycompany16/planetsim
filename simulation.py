import pygame
from constants import *

class World:
    def __init__(self) -> None:
        self.screen_surf = pygame.Surface((WIDTH, HEIGHT))
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def process(self, dt) -> None:
        self.screen_surf.fill((20, 20, 40))

        for planet in self.planets:
            planet.process(dt, self.screen_surf)
            planet.find_acceleration(filter(lambda x: x != planet, self.planets))


class Planet:
    def __init__(self, radius : int, mass : float, pos_0 : pygame.Vector2, vel_0 : pygame.Vector2, acc_0 : pygame.Vector2, color : pygame.Color) -> None:
        self.radius = radius
        self.mass = mass
        self.pos = pos_0
        self.prev_pos = pos_0
        self.vel = vel_0
        self.acc = acc_0
        self.color = color

    def process(self, dt, screen_surf) -> None:
        # Apply gravitational forces, update pos and stuff
        self.pos += self.vel * dt + 0.5 * self.acc * dt * dt
        self.vel += self.acc * dt
        
        pygame.draw.circle(screen_surf, self.color, self.pos / METERS_PER_PIXEL, self.radius / METERS_PER_PIXEL)

    def find_acceleration(self, planets):
        for planet in planets:
            self.acc = -G * self.mass * planet.mass / pygame.Vector2.length(self.pos - planet.pos) * pygame.Vector2.normalize(self.pos - planet.pos)
            print(self.acc)