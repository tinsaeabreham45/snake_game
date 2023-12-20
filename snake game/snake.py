import pygame
import time
import random

pygame.init()
# my constant
width, height = 600, 400
snake_size = 20
snake_speed = 10

# my color

background = (2, 156, 84)
snake_color = (211, 242, 5)
food_color = (217, 9, 85)
text_color = (255, 255, 255)

# creating and initializing the window
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Python Snake Game')
clock = pygame.time.Clock()

font = pygame.font.SysFont('bahnschrift', 28)


# make snake

def make_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, snake_color, [x, y, snake_size, snake_size])


# game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []  # body of snake's
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    foody = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:
        while game_close:
            dis.fill(background)
            # message("You Lost! Press Q-Quit or C-Play Again", food_color)
            make_snake(snake_list)
            pygame.display.update()
            # issue handling loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        # Game conditions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_size
                    x1_change = 0

        # check the snake head if it is out of the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            # some message is displayed now

        x1 += x1_change
        y1 += y1_change
        dis.fill(background)

        # generating food
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_size, snake_size])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # checking the collision between the heads and the body

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        make_snake(snake_list)
        pygame.display.update()

        # if x1 == foodx and y1 == foody:
        #     foodx = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
        #     foody = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
        #     length_of_snake += 1
    # never generate a new food

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
