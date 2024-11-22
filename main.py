# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock instnce to manage the frame rates
    clock = pygame.time.Clock()
    dt = 0


    # Creating and adding sprites to designated groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Creating instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2 )
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (000, 000, 000),)


# Add another collision check to the game loop.
# Loop over each asteroid, and for each asteroid,
#   loop over each bullet.
# If a bullet and an asteroid collide,
# call the .kill() method on both objects to remove them from the game.

        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                raise SystemExit("Game over!")

            for shot in shots:
                if shot.detect_collision(asteroid):
                    shot.kill()
                    asteroid.split()


        for sprite in drawable:
            sprite.draw(screen)



        dt = clock.tick(60) / 1000
        pygame.display.flip() # To be called last


if __name__ == "__main__":
    main()