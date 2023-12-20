import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 20
snake_speed = 5

# Colors
text_color = (255, 255, 255)
food_color = (217, 9, 85)
snake_color = (211, 242, 5)
background = (2, 156, 84)

# Initialize display
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game Using Python')

clock = pygame.time.Clock()

font = pygame.font.SysFont('bahnschrift', 24)


def make_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, snake_color, [x, y, SNAKE_SIZE, SNAKE_SIZE])


def display_score(score):
    score_text = font.render("Score: " + str(score), True, text_color)
    dis.blit(score_text, [10, 10])


def message(msg, color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE

    score = 0

    while not game_over:
        while game_close:
            dis.fill(background)
            message("You Lost! Press Q-Quit or C-Play Again", food_color)
            display_score(score)
            make_snake(snake_list)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = SNAKE_SIZE

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(background)

        pygame.draw.rect(dis, food_color, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        make_snake(snake_list)
        display_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            length_of_snake += 1
            score += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
