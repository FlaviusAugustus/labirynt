import math
import random
import pygame
import colors


def clear_screen(screen):
    screen.screen.fill(colors.black)


def display_message(text, size, pos):
    text_parameters = pygame.font.Font("freesansbold.ttf", size)
    message = text_parameters.render(text, True, colors.white)
    text_rect = message.get_rect()
    text_rect.center = pos

    return message, text_rect


def random_pos(maze):
    walls = maze.list_of("walls")
    good_pos = False
    while not good_pos:
        object_x = int(math.ceil(random.randrange(0, 950) / maze.sprite_size)) * maze.sprite_size
        object_y = int(math.ceil(random.randrange(0, 1000) / maze.sprite_size)) * maze.sprite_size
        if all([wall.x, wall.y] != [object_x, object_y] for wall in walls):
            good_pos = True
    return {"x": object_x, "y": object_y}


