import pygame
import sys
from hero import Hero

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.move_right = True
                if event.key == pygame.K_LEFT:
                    hero.move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hero.move_right = False
                if event.key == pygame.K_LEFT:
                    hero.move_left = False

        pygame.display.flip()
        screen.fill(0)
        hero.output_hero()
        hero.moving_hero(screen)

start_game()
