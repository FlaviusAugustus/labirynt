import pygame
import colors
import utils


class Prize:
    size = 25
    color = colors.yellow
    scored = False
    pos = {}

    def __init__(self, screen, maze):
        self.screen = screen
        self.maze = maze


    def spawn(self):
        air = self.maze.list_of("air")
        self.pos = {"x": min(air)[0], "y": min(air)[1]}
        self.visual_repr = pygame.Rect(self.pos["x"], self.pos["y"], self.size, self.size)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update()

    def spawn_random_pos(self):
        self.pos = utils.random_pos(self.maze)
        self.visual_repr = pygame.Rect(self.pos["x"], self.pos["y"], self.size, self.size)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update()

    def update(self):
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update()

    def vanish(self):
        pygame.draw.rect(self.screen.screen, (0, 0, 0), self.visual_repr)
        pygame.display.update()


