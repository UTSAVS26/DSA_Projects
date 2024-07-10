import pygame
import time
from src.settings import *
from src.snake import Snake
from src.food import Food

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(FONT_STYLE, 25)
score_font = pygame.font.SysFont(SCORE_FONT_STYLE, 35)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    snake = Snake()
    food = Food()

    direction = 'RIGHT'

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake.length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'

        if snake.segments[-1][0] >= WIDTH or snake.segments[-1][0] < 0 or \
           snake.segments[-1][1] >= HEIGHT or snake.segments[-1][1] < 0:
            game_close = True

        snake.move(direction)
        if snake.segments[-1] == food.position:
            food.respawn()
            snake.length += 1

        screen.fill(BLACK)
        food.draw(screen)
        snake.draw(screen)
        display_score(snake.length - 1)

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()