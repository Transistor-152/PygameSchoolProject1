import pygame
import sys
import random

# 1. Запуск движка pygame
pygame.init()

# 2. Настройки окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лови яблоки!")
clock = pygame.time.Clock()

# 3. Цвета (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (50, 100, 200)

# 4. Параметры игрока (корзина)
player_width, player_height = 80, 20
player_x = WIDTH // 2
player_y = HEIGHT - 40
player_speed = 6
# 5. Параметры яблока
apple_size = 20
apple_x = random.randint(0, WIDTH - apple_size)
apple_y = 0
apple_speed = 3

# 6. Счёт и шрифт
score = 0
font = pygame.font.SysFont("arial", 32)

running = True
while running:
    # --- ОБРАБОТКА СОБЫТИЙ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- УПРАВЛЕНИЕ ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # --- ДВИЖЕНИЕ ЯБЛОКА ---
    apple_y += apple_speed

    # Если яблоко упало мимо
    if apple_y > HEIGHT:
        apple_x = random.randint(0, WIDTH - apple_size)
        apple_y = 0

    # --- ПРОВЕРКА ПОЙМАННОГО ЯБЛОКА (прямоугольники) ---
    if (apple_y + apple_size >= player_y and
        apple_x < player_x + player_width and
        apple_x + apple_size > player_x):
        score += 1
        apple_x = random.randint(0, WIDTH - apple_size)
        apple_y = 0

      # Постепенно ускоряем
    if apple_speed < 8:
        apple_speed += 0.3

    # --- ОТРИСОВКА ---
    screen.fill(WHITE)  # Очищаем экран

    # Рисуем корзину и яблоко
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (apple_x, apple_y, apple_size, apple_size))

    # Рисуем счёт
    score_text = font.render(f"Счёт: {score}", True, BLACK)
    screen.blit(score_text, (15, 15))
    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)  # 60 кадров в секунду

# 7. Закрытие игры
pygame.quit()
sys.exit()