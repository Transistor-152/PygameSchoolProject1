import pygame
import random
import sys

# ---
# ИНИЦИАЛИЗАЦИЯ
# ---
pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лови яблоки")

clock = pygame.time.Clock()

bg_menu = pygame.image.load('asa.png') # Задний фон меню
bg = pygame.image.load('bbc.png') # Задний фон игры

# ---
# ЦВЕТА
# ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 70, 70)
BLUE = (50, 100, 220)
GREEN = (50, 180, 50)

# ---
# ШРИФТЫ
# ---
title_font = pygame.font.Font('PixelImpacted-Regular.otf', 90)
font = pygame.font.Font('Zeequada-Regular.otf', 28)
small_font = pygame.font.Font('Zeequada-Regular.otf', 22)

# ---
# МЕНЮ
# ---
def menu():
    while True:
        screen.fill(WHITE)

        screen.blit(bg_menu, (0, 0))

        version = small_font.render("V 2.0", True, WHITE)
        screen.blit(version, (530, 20))

        title = title_font.render("Лови яблоки!", True, WHITE)
        screen.blit(title, (125, 50))

        text = font.render("Выберите сложность:", True, WHITE)
        screen.blit(text, (170, 130))

        easy = small_font.render("1 - Легко", True, WHITE)
        normal = small_font.render("2 - Нормально", True, WHITE)
        hard = small_font.render("3 - Сложно", True, WHITE)

        screen.blit(easy, (230, 190))
        screen.blit(normal, (230, 230))
        screen.blit(hard, (230, 270))
        info = small_font.render("ESC - Выход", True, WHITE)
        screen.blit(info, (220, 330))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    return 2, 7, "Легко"

                if event.key == pygame.K_2:
                    return 4, 6, "Нормально"

                if event.key == pygame.K_3:
                    return 6, 5, "Сложно"

# ЭКРАН GAME OVER
def game_over(score):
    while True:
        screen.fill(BLACK)

        over_text = title_font.render("GAME OVER", True, RED)
        score_text = font.render(f"Ваш счёт: {score}", True, WHITE)

        restart_text = small_font.render(
            "R - Играть снова | ESC - Выход",
            True,
            WHITE
        )

        screen.blit(over_text, (150, 120))
        screen.blit(score_text, (220, 200))
        screen.blit(restart_text, (150, 270))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_r:
                    return

# ОСНОВНАЯ ИГРА
def play():
    apple_speed, player_speed, difficulty = menu()

    # Игрок
    player_width = 80
    player_height = 20

    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - 50

    player_image = pygame.image.load('3246и34ц345м (1).png')

    # Яблоко
    apple_size = 20

    apple_x = random.randint(0, WIDTH - apple_size)
    apple_y = 0

    apple_image = pygame.image.load('5ш-Photoroom.png')

    # Счёт и жизни
    score = 0
    lives = 3

    running = True

    while running:

        # ---
        # СОБЫТИЯ
        # ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # ---
        # УПРАВЛЕНИЕ
        # ---
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # ---
        # ДВИЖЕНИЕ ЯБЛОКА
        # ---
        apple_y += apple_speed

        # Промах
        if apple_y > HEIGHT:
            lives -= 1

            apple_x = random.randint(
                0,
                WIDTH - apple_size
            )

            apple_y = 0

        # ---
        # ПОЙМАЛИ ЯБЛОКО
        # ---
        if (
            apple_y + apple_size >= player_y
            and apple_x < player_x + player_width
            and apple_x + apple_size > player_x
        ):
            score += 1

            apple_x = random.randint(
                0,
                WIDTH - apple_size
            )

            apple_y = 0

            # Постепенно увеличиваем скорость
            if apple_speed < 10:
                apple_speed += 0.2

        # ---
        # КОНЕЦ ИГРЫ
        # ---
        if lives <= 0:
            running = False

        # ---
        # ОТРИСОВКА
        # ---
        screen.blit(bg, (0, 0))
        # Корзина
        screen.blit(apple_image, (apple_x, apple_y))

        # Яблоко
        screen.blit(player_image, (player_x, player_y))

        # Счёт
        score_text = small_font.render(
            f"Счёт: {score}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))

        # Жизни
        lives_text = small_font.render(
            f"Жизни: {lives}",
            True,
            WHITE
        )
        screen.blit(lives_text, (450, 10))

        # Сложность
        diff_text = small_font.render(
            difficulty,
            True,
            WHITE
        )

        screen.blit(diff_text, (250, 10))

        pygame.display.flip()
        clock.tick(60)

    game_over(score)

# ЗАПУСК
while True:
    play()