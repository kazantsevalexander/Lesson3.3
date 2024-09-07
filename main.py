import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Меткий стрелок")
icon = pygame.image.load("img/2689911.png")
pygame.display.set_icon(icon)

cursor_img = pygame.image.load("img/darts.png")
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)

target_img = pygame.image.load("img/target.png")
target_width = random.randint(30, 150)
target_height = target_width
img_size = (target_width, target_height)
scaled_img = pygame.transform.smoothscale(target_img, img_size)

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color_bg = (random.randint(50, 100), random.randint(50, 200), random.randint(50, 200))

font = pygame.font.Font(None, 26)  # Шрифт для отображения счета
score = 0
strel = 10

running = True

target_speed = 10  # Скорость перемещения мишени
target_new_x = target_x
target_new_y = target_y

while running:
    screen.fill(color_bg)
    # Получаем позицию мыши


    for event in pygame.event.get():
        if event.type == pygame.QUIT or strel == 0:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            strel -= 1
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                # Получаем новые случайные координаты и размеры
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

    screen.blit(scaled_img, (target_x, target_y))
    cursor_rect.topleft = pygame.mouse.get_pos()

    # Отображение счета
    score_text = font.render(f"Счет: {score} Осталось стрел: {strel}", True, (255, 255, 255))
    screen.blit(score_text, (20, 10))

    screen.blit(cursor_img, cursor_rect)
    pygame.display.update()

pygame.quit()