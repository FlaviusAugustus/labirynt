import colors
import utils
import pygame
import random



class Enemy:
    size = 25
    vel_x = 0
    vel_y = 0
    did_move = False
    pos = {}

    def __init__(self, color, step, maze, settings, screen):
        self.color = color
        self.step = step
        self.maze = maze
        self.settings = settings
        self.screen = screen

    def spawn(self):
        # good_pos = False
        # while not good_pos:
        #     check = 0
        #     pos = utils.random_pos(self.maze)
        #     walls = self.maze.list_of("walls")
        #     walls = [[i.x, i.y] for i in walls]
        #
        #     checked1 = False
        #     while not checked1:
        #
        #         if [pos["x"], pos["y"]-25] not in walls:
        #             pos["y"] -= 25
        #
        #         if [pos["x"], pos["y"]-25] in walls:
        #             checked1 = True
        #
        #
        #     checked2 = False
        #     while not checked2:
        #         if [pos["x"], pos["y"] + 25] not in walls:
        #             pos["y"] += 25
        #             check += 1
        #         else:
        #             checked2 = True
        #
        #     if check >= 5:
        #         good_pos = True
        #         self.pos = pos
        self. pos = utils.random_pos(self.maze)
        self.visual_repr = pygame.Rect(self.pos["x"], self.pos["y"], self.size, self.size)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update()

    def vanish(self):
        pygame.draw.rect(self.screen.screen, colors.black, self.visual_repr)
        pygame.display.update()

    def get_direction(self):
        self.direction = random.choice([1, -1])
        if self.direction == 1:
            self.vel_x = self.settings.enemy_vel_i
            self.vel_y = 0
        elif self.direction == -1:
            self.vel_y = self.settings.enemy_vel_i
            self.vel_x = 0


    def move(self):
        for i in self.maze.list_of("walls"):
            if self.visual_repr.colliderect(i):
                self.vel_y = -self.vel_y
                self.vel_x = -self.vel_x

                self.vanish()
                self.visual_repr = self.visual_repr.move(self.vel_x, -self.vel_y)
                pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)

                pygame.draw.rect(self.screen.screen,colors.white, (i.x, i.y, 25, 25))
                pygame.display.update()

        self.vanish()
        self.visual_repr = self.visual_repr.move(self.vel_x, -self.vel_y)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update(self.visual_repr)



