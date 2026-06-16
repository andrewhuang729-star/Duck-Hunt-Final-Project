# Pygame Collision
# Author: Ubial
# Date: 7 May

import random

import pygame

pygame.init()

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# CONSTANTS
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
NUM_BLOCKS = 50


class Block(pygame.sprite.Sprite):
    def __init__(self, colour: tuple[int, int, int]):
        super().__init__()

        self.image = pygame.Surface((20, 7))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)


def main():
    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collision!")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # Populate sprite groups
    for _ in range(NUM_BLOCKS):
        block = Block(GREEN)
        all_sprites.add(block)
        block_sprites.add(block)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites.update()

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    main()
