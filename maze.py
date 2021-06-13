import random
import pygame
import colors


class Maze:
    sprite_size = 25
    walls = []

    def __init__(self, m_height, m_width):
        self.m_height = m_height
        self.m_width = m_width


    def generate(self):
        height = self.m_height // 50
        width = self.m_width // 50
        maze = []

        random_row = random.randrange(1, height - 1)
        random_pos_in_row = random.randrange(1, width - 1)

        for i in range(height):
            maze.append(list("#" * width))

        rand_range = random.randrange(int((width - 2) * (height - 2) * 0.5), (width - 2) * (height - 2) - 3)

        for i in range(rand_range):
            if i == 0:
                maze[random_row][random_pos_in_row] = " "
                latest_blank_spot_pos = [random_row, random_pos_in_row]
                continue
            choices = [1, 2, 3, 4]

            random_way = random.choice(choices)
            if random_way == 1 and maze[latest_blank_spot_pos[0] - 1][latest_blank_spot_pos[1]] != " " and \
                    latest_blank_spot_pos[0] - 1 != 0:

                maze[latest_blank_spot_pos[0] - 1][latest_blank_spot_pos[1]] = " "
                latest_blank_spot_pos[0] -= 1

            elif random_way == 2 and latest_blank_spot_pos[1] + 1 != width - 1 and latest_blank_spot_pos[1] + 1 != " ":
                maze[latest_blank_spot_pos[0]][latest_blank_spot_pos[1] + 1] = " "
                latest_blank_spot_pos[1] += 1

            elif random_way == 3 and maze[latest_blank_spot_pos[0] + 1][latest_blank_spot_pos[1]] != " " and \
                    latest_blank_spot_pos[0] + 1 != height - 1:

                maze[latest_blank_spot_pos[0] + 1][latest_blank_spot_pos[1]] = " "
                latest_blank_spot_pos[0] += 1

            elif random_way == 4 and latest_blank_spot_pos[1] - 1 != 0 and latest_blank_spot_pos[1] - 1 != " ":
                maze[latest_blank_spot_pos[0]][latest_blank_spot_pos[1] - 1] = " "
                latest_blank_spot_pos[1] -= 1

        self.maze = maze


    def create_boss_fight_map(self):
        self.maze = [["#", "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#", "#","#","#","#","#","#","#","#","#","#","#","#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
               ["#", "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#", "#","#","#","#","#","#","#","#","#","#","#","#"]]








    def display(self, screen):
        y = -50
        for row in self.maze:
            y += 50
            x = 0
            for row_element in row:
                if row_element == "#":
                    self.draw_wall(x, y, screen.screen)
                x += 50
        pygame.display.update()

    def draw_wall(self, x, y, screen):
        pygame.draw.rect(screen, colors.white, (x, y, 50, 50))

    def list_of(self, components):
        walls = []
        air = []
        y = -50
        for row in self.maze:
            y += 50
            x = 0
            for row_element in row:
                if row_element == "#" and components == "walls":
                    walls.append(pygame.Rect(x, y, 25, 25))
                    walls.append(pygame.Rect(x + 25, y, 25, 25))
                    walls.append(pygame.Rect(x + 25, y + 25, 25, 25))
                    walls.append(pygame.Rect(x, y + 25, 25, 25))
                elif row_element == " " and components == "air":
                    air.append([x, y])
                    air.append([x + 25, y])
                    air.append([x + 25, y + 25])
                    air.append([x, y + 25])
                x += 50
        if components == "walls":
            return walls
        elif components == "air":
            return air