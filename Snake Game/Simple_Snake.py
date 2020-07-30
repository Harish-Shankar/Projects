import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()


def snake(snake_player, snake_position, window):
    for i in snake_position:
        pygame.draw.rect(window, (2, 73, 255), [i[0], i[1], snake_player, snake_player])


def main():
    width = 600
    height = 400
    window = pygame.display.set_mode((width, height))
    snake_player = 10
    snake_position = []
    snake_length = 1
    speed = 15

    food_x = (random.randrange(0, width - snake_player) // 10) * 10
    food_y = (random.randrange(0, height - snake_player) // 10) * 10
    pygame.display.set_caption("Snake")

    flag = False
    game_end = False

    x = width//2
    y = height//2
    x_change = 0
    y_change = 0

    while not flag:
        while game_end:
            window.fill((0, 0, 0))
            retry_font = pygame.font.SysFont("Georgia", 35)
            msg = retry_font.render("You Lost! Press 'R' to play again", True, (134, 51, 252))
            window.blit(msg, [width//6, height//3])

            score_font = pygame.font.SysFont("Georgia", 35)
            value = score_font.render("Your Score: " + str(snake_length-1), True, (0, 124, 26))
            window.blit(value, [width//3, height//5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
                if event.type == pygame.QUIT:
                    flag = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_player
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_player
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_player
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_player

        if x >= width or x < 0 or y >= height or y < 0:
            game_end = True

        x += x_change
        y += y_change
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 139, 2), [food_x, food_y, snake_player, snake_player])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_position.append(snake_head)

        if len(snake_position) > snake_length:
            del snake_position[0]
        for i in snake_position[:-1]:
            if i == snake_head:
                game_end = True

        snake(snake_player, snake_position, window)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = (random.randrange(0, width - snake_player) // 10) * 10
            food_y = (random.randrange(0, height - snake_player) // 10) * 10
            snake_length += 1
        clock.tick(speed)
    pygame.quit()
    quit()


main()
