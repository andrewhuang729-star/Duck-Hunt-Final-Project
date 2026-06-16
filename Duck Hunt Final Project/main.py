# Duck Hunt Game
# Author: Andrew Huang
# Date: May 27th 2026

import random

import pygame

pygame.init()
pygame.mixer.init()

# Colours (r,g,b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
WIDTH = 1024
HEIGHT = 540
SIZE = (WIDTH, HEIGHT)
FPS = 60

DUCK_SPEED = 5
MAX_ROUNDS = 10


# Chat helped with load sound
def load_sound(filename):
    """Load a sound from the Sounds folder"""
    try:
        return pygame.mixer.Sound("assets/Sounds/" + filename)
    except pygame.error:
        return None


# Class Duck
class Duck(pygame.sprite.Sprite):
    def __init__(self):
        """Duck"""
        super().__init__()

        # Loading game
        self.image_right = pygame.image.load(
            "assets/Images/duck-right.gif"
        ).convert_alpha()
        self.image_left = pygame.image.load(
            "assets/Images/duck-left.gif"
        ).convert_alpha()

        # Resize duck's image to fit game
        self.image_right = pygame.transform.scale(self.image_right, (96, 93))
        self.image_left = pygame.transform.scale(self.image_left, (96, 93))

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.x_vel = DUCK_SPEED
        self.y_vel = DUCK_SPEED

        self.reset()

    def reset(self):
        """Randomizing Duck Location"""
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(50, HEIGHT - 170)

        self.x_vel = random.choice([-DUCK_SPEED, DUCK_SPEED])
        self.y_vel = random.choice([-DUCK_SPEED, DUCK_SPEED])

        if self.x_vel < 0:
            self.image = self.image_left
        else:
            self.image = self.image_right

    def update(self):
        """Duck movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Duck hits left or right
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.x_vel *= -1

            if self.x_vel < 0:
                self.image = self.image_left
            else:
                self.image = self.image_right

        # If duck hits down or up
        if self.rect.top <= 50 or self.rect.bottom >= HEIGHT - 120:
            self.y_vel *= -1


# Class Crosshair (chat helped me with making the crosshair connect with the mouse)
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        """Crosshair"""
        super().__init__()

        self.image = pygame.image.load("assets/Images/target.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (36, 36))

        self.rect = self.image.get_rect()

    def update(self):
        """Crosshair with mouse"""
        self.rect.center = pygame.mouse.get_pos()


# Class dog
class Dog(pygame.sprite.Sprite):
    def __init__(self, duck_count):
        """Dog"""
        super().__init__()

        if duck_count == 1:
            self.image = pygame.image.load(
                "assets/Images/dog-duck1.png"
            ).convert_alpha()
            self.image = pygame.transform.scale(self.image, (172, 152))
        else:
            self.image = pygame.image.load(
                "assets/Images/dog-duck2.png"
            ).convert_alpha()
            self.image = pygame.transform.scale(self.image, (224, 152))

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT


# Chatgpt helped me draw all the text
def draw_text(screen, text, size, colour, x, y):
    """Draw text on the screen"""
    try:
        font = pygame.font.Font("assets/Fonts/game-font.otf", size)
    except pygame.error:
        font = pygame.font.SysFont("Arial", size)

    text_image = font.render(text, True, colour)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)

    screen.blit(text_image, text_rect)


# I used AI for help with making the round number match the amount of ducks.
# Understand know that this loop keeps making ducks and adding them to the sprite
# groups so they can move and be clicked.
def create_ducks(all_sprites, duck_sprites, round_number):
    """Create ducks for the round"""
    duck_count = round_number

    for _ in range(duck_count):
        duck = Duck()
        all_sprites.add(duck)
        duck_sprites.add(duck)

    return duck_count


# Chat helped with displaying the loading screen and switching to the actual game
def menu_screen(clock, screen):
    """Menu Screen loading"""
    loading_screen = pygame.image.load(
        "assets/Images/loading screen.png"
    ).convert_alpha()
    loading_screen = pygame.transform.scale(loading_screen, (512, 512))

    loading_rect = loading_screen.get_rect()
    loading_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Chat did all load the sounds into the function
    try:
        pygame.mixer.music.load("assets/Sounds/01. Title BGM(1).mp3")
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    # Menu loop
    while True:
        # Main event sound
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "done"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "done"

            # Player click to switch to game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()

                    start_sound = load_sound("02. GAme A - B Start.mp3")
                    if start_sound is not None:
                        start_sound.play()

                    return "game"

        # Game logic

        # Drawing to the screen
        screen.fill(BLACK)
        screen.blit(loading_screen, loading_rect)

        draw_text(screen, "CLICK TO START", 18, WHITE, WIDTH // 2, HEIGHT - 40)

        # Info screen
        pygame.display.flip()

        # Clock tick
        clock.tick(FPS)


# Chat helped me show the dog at the end of every round
def show_dog(clock, screen, background, duck_count):
    """Show the dog after the ducks are shot"""
    dog = Dog(duck_count)

    dog_sound = load_sound("03. Dog.mp3")
    if dog_sound is not None:
        dog_sound.play()

    start_time = pygame.time.get_ticks()

    # Dog loop
    while pygame.time.get_ticks() - start_time < 2000:
        # Main event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "done"

        # Game logic

        # Drawing to screen
        screen.blit(background, (0, 0))
        screen.blit(dog.image, dog.rect)

        # Update screen
        pygame.display.flip()

        # Clock tick
        clock.tick(FPS)

    return "game"


# Game over screen
def game_over_screen(clock, screen, background, score):
    """Show the game over screen"""
    game_over_sound = load_sound("10. Game Over.mp3")
    if game_over_sound is not None:
        game_over_sound.play()

    # Game over loop
    while True:
        # Main event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "done"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "done"

                if event.key == pygame.K_SPACE:
                    return "game"

        # Game logic

        #  Drawing to screen
        screen.blit(background, (0, 0))

        draw_text(screen, "GAME OVER", 54, BLACK, WIDTH // 2, 160)
        draw_text(screen, "SCORE: " + str(score), 34, BLACK, WIDTH // 2, 240)
        draw_text(screen, "SPACE TO PLAY AGAIN", 22, BLACK, WIDTH // 2, 320)
        draw_text(screen, "ESC TO QUIT", 22, BLACK, WIDTH // 2, 360)

        # Update screen
        pygame.display.flip()

        # Clock tick
        clock.tick(FPS)


def game(clock, screen, background):
    """Main game"""
    pygame.mouse.set_visible(False)

    shot_sound = load_sound("99 - Gunshot (SFX).mp3")
    hit_sound = load_sound("05. Got a Duck!.mp3")
    miss_sound = load_sound("08. Miss.mp3")
    clear_sound = load_sound("06. Clear.mp3")

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    duck_sprites = pygame.sprite.Group()

    # Variables
    score = 0
    round_number = 1
    bullets = round_number
    done = False

    duck_count = create_ducks(all_sprites, duck_sprites, round_number)

    crosshair = Crosshair()

    # Main game loop
    while not done:
        # Main event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mouse.set_visible(True)
                return score

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    return score

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if bullets > 0:
                        bullets -= 1

                        if shot_sound is not None:
                            shot_sound.play()

                        crosshair.update()

                        # Ai helped with checking crosshair touches duck
                        ducks_hit = pygame.sprite.spritecollide(
                            crosshair, duck_sprites, True
                        )

                        if ducks_hit:
                            score += len(ducks_hit)

                            if hit_sound is not None:
                                hit_sound.play()
                        else:
                            if miss_sound is not None:
                                miss_sound.play()

        # Game logic
        all_sprites.update()
        crosshair.update()

        # Next rounds
        if len(duck_sprites) == 0:
            if clear_sound is not None:
                clear_sound.play()

            result = show_dog(clock, screen, background, duck_count)

            if result == "done":
                pygame.mouse.set_visible(True)
                return score

            round_number += 1

            if round_number > MAX_ROUNDS:
                done = True
            else:
                all_sprites.empty()
                duck_sprites.empty()

                # Ai helped make rounds match duck count
                bullets = round_number
                duck_count = create_ducks(all_sprites, duck_sprites, round_number)

        elif bullets == 0 and len(duck_sprites) > 0:
            done = True

        # Drawing to screen
        screen.blit(background, (0, 0))

        duck_sprites.draw(screen)
        screen.blit(crosshair.image, crosshair.rect)

        draw_text(screen, "SCORE: " + str(score), 22, WHITE, 110, 30)
        draw_text(screen, "BULLETS: " + str(bullets), 22, WHITE, WIDTH - 140, 30)

        # Update screen
        pygame.display.flip()

        # Clock tick
        clock.tick(FPS)

    pygame.mouse.set_visible(True)
    return score


def main():
    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Duck Hunt")

    # Clock variable
    clock = pygame.time.Clock()

    # Game background
    background = pygame.image.load("assets/Images/duckhunt-bg-4k.png").convert()
    background = pygame.transform.scale(background, SIZE)

    while True:
        choice = menu_screen(clock, screen)

        if choice == "done":
            break
        elif choice == "game":
            final_score = game(clock, screen, background)
            choice = game_over_screen(clock, screen, background, final_score)

            if choice == "done":
                break

    pygame.quit()


if __name__ == "__main__":
    main()
