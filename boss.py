import pygame
import colors
import random
import utils


class Boss:
    vel_x = 5
    vel_y = 5
    size = 120
    pos = {"x": 100, "y": 100}
    color = colors.red
    alive = False
    hp = 3
    elements = []

    def __init__(self, screen, player, maze, prize, settings):
        self.screen = screen
        self.player = player
        self.maze = maze
        self.prize = prize
        self.settings = settings

    def spawn(self):
        self.visual_repr = pygame.Rect(self.pos["x"], self.pos["y"], self.size, self.size - 15)
        self.alive = True
        self.hp = 3
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update(self.visual_repr)

    def move(self):
        for element in self.elements:
            self.vanish()
            element = element.move(self.vel_x, self.vel_y)
            pygame.draw.rect(self.screen.screen, self.color, element)
            pygame.display.update(element)

    def vanish(self):
        pygame.draw.rect(self.screen.screen, colors.black, self.visual_repr)
        pygame.display.update(self.visual_repr)

    def create_collidepoints(self, rect):
        self.collidepoint_midtop = rect.collidepoint((self.visual_repr.midtop[0], self.visual_repr.midtop[1]-15))
        self.collidepoint_midbottom = rect.collidepoint(self.visual_repr.midbottom)
        self.collidepoint_midleft = rect.collidepoint((self.visual_repr.midleft[0]-5, self.visual_repr.midleft[1]))
        self.collidepoint_midright = rect.collidepoint(self.visual_repr.midright)

    def collisions(self):
        if self.visual_repr.colliderect(self.prize.visual_repr):
            self.prize.vanish()
            self.prize.scored = True
        elif self.player.visual_repr.colliderect(self.prize.visual_repr):
            self.hp -= 1
            self.divide()


        for wall in self.maze.list_of("walls"):
            self.create_collidepoints(wall)
            if self.collidepoint_midbottom or self.collidepoint_midtop:
                self.vel_y = -self.vel_y

            elif self.collidepoint_midleft or self.collidepoint_midright:
                self.vel_x = -self.vel_x

    def is_alive(self):
        if self.hp == 0:
            self.alive = False
        else:
            pass

    def divide(self):
        if self.hp == 2:
            self.vanish()
            self.elements = [pygame.Rect(self.visual_repr.midtop[0], self.visual_repr.midtop[1], self.size/2, self.size/2), pygame.Rect(self.visual_repr.midbottom[0], self.visual_repr.midbottom[1], self.size/2, self.size/2)]
            for element in self.elements:
                pygame.draw.rect(self.screen.screen, self.color, element)
            pygame.display.update(element)


    def random_vel(self):
        for element in self.elements:
            element.vel_x = random.choice([5, -5, 4, -4])
            element.vel_y = random.choice([5, -5, 4, -4])


    def set_pos(self):
        self.pos["x"] = self.maze.m_width / 2
        self.pos["y"] = self.maze.m_height /2


    def spawn_health_bar(self):
        self.health_bar = pygame.Rect(self.visual_repr.x, self.visual_repr.y - 10, self.size, 5)
        pygame.draw.rect(self.screen.screen, colors.red, self.health_bar)
        pygame.display.update(self.health_bar)


    def update_health_bar(self):
        self.health_bar_vanish()
        if self.hp == 3:
            self.health_bar.width = 120
        if self.hp == 2:
            self.health_bar.width = 80
        if self.hp == 1:
            self.health_bar.width = 40
        self.health_bar = self.health_bar.move(self.vel_x, self.vel_y)
        pygame.draw.rect(self.screen.screen, colors.red, self.health_bar)
        pygame.display.update(self.health_bar)


    def health_bar_vanish(self):
        pygame.draw.rect(self.screen.screen, colors.black, self.health_bar)
        pygame.display.update(self.health_bar)