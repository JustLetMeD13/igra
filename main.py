# main.py

import pygame
import sys
from screen import Screen
from controls import Player

# Инициализация Pygame
pygame.init()

# Основные параметры
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание объектов
screen = Screen(WIDTH, HEIGHT, "My Roguelike Game")
player = Player(WIDTH // 2, HEIGHT // 2, 50, 5)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Получение состояния нажатия клавиш
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Отрисовка элементов
        screen.fill(WHITE)
        screen.draw_rect(RED, player.get_rect())

        # Обновление экрана
        screen.update()
        clock.tick(60)

# Запуск игры
if __name__ == "__main__":
    main()