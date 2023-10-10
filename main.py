import pygame
from constants import *
from simulation import World, Planet

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity!")

    clock = pygame.time.Clock()

    world = World()
    world.add_planet(Planet(20_000_000, 4e13, pygame.Vector2(400000000, 100000000), pygame.Vector2(200_000_000, 0), pygame.Vector2(0, 0), pygame.Color(234, 127, 55)))
    world.add_planet(Planet(20_000_000, 4e13, pygame.Vector2(400000000, 700000000), pygame.Vector2(-200_000_000, 0), pygame.Vector2(0, 0), pygame.Color(100, 100, 55)))

    running = True
    while running:
        dt = clock.tick(60)

        world.process(dt / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(world.screen_surf, (0, 0))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
