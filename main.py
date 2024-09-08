import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка окна и иконки
pygame.display.set_caption("Меткий стрелок")
icon = pygame.image.load("img/2689911.png")
pygame.display.set_icon(icon)

# Загрузка изображения курсора и скрытие стандартного курсора
cursor_img = pygame.image.load("img/darts.png")
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)

# Загрузка изображения мишени и случайный выбор размеров
target_img = pygame.image.load("img/target.png")
target_width = random.randint(30, 150)
target_height = target_width
img_size = (target_width, target_height)
scaled_img = pygame.transform.smoothscale(target_img, img_size)

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный цвет фона
color_bg = (random.randint(50, 100), random.randint(50, 200), random.randint(50, 200))

# Настройка шрифта для отображения счета
font = pygame.font.Font(None, 36)
score = 0  # Начальный счет
strel = 10  # Количество оставшихся стрел
game_over = font.render("GAME OVER", True, (255, 0, 0))  # Текст "GAME OVER"

running = True  # Основной цикл игры

target_speed = 15  # Скорость перемещения мишени
target_new_x = target_x  # Новые координаты мишени
target_new_y = target_y

# Основной игровой цикл
while running:
    screen.fill(color_bg)  # Заполнение фона цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False

        if strel == 0:  # Если стрелы закончились
            screen.blit(game_over, (350, 290))  # Отображаем текст "GAME OVER"
            pygame.display.flip()  # Обновление экрана
            pygame.time.delay(2000)  # Задержка на 2 секунды
            score = 0  # Начальный счет
            strel = 10  # Количество оставшихся стрел

        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем координаты мыши
            strel -= 1  # Уменьшаем количество оставшихся стрел

            # Проверка попадания в мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет

                # Получаем новые случайные координаты и размеры мишени
                target_width = random.randint(30, 150)
                target_height = target_width
                target_new_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_new_y = random.randint(0, SCREEN_HEIGHT - target_height)
                img_size = (target_width, target_height)
                scaled_img = pygame.transform.smoothscale(target_img, img_size)

    # Плавное перемещение мишени
    if target_x != target_new_x or target_y != target_new_y:
        target_x += (target_new_x - target_x) / target_speed ** 2
        target_y += (target_new_y - target_y) / target_speed

    # Отображение мишени на экране
    screen.blit(scaled_img, (target_x, target_y))
    cursor_rect.topleft = pygame.mouse.get_pos()  # Установка позиции курсора

    # Отображение счета
    score_text = font.render(f"Попаданий: {score} Осталось стрел: {strel}", True, (255, 255, 255))
    screen.blit(score_text, (20, 10))

    # Отображение курсора
    screen.blit(cursor_img, cursor_rect)
    pygame.display.update()  # Обновление экрана

pygame.quit()  # Завершение работы Pygame