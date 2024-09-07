import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Меткий стрелок")
icon = pygame.image.load("img/2689911.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = random.randint(30, 150)
target_height = target_width
img_size = (target_width, target_height)
scaled_img = pygame.transform.smoothscale(target_img, img_size)

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color_bg = (random.randint(50, 100), random.randint(50, 200), random.randint(50, 200))

running = True

while running:
    screen.fill(color_bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_width = random.randint(30, 150)
                target_height = target_width
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                img_size = (target_width, target_height)
                scaled_img = pygame.transform.smoothscale(target_img, img_size)

    screen.blit(scaled_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()