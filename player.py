import pygame
import colors


class Player:
    alive = True
    did_move = False
    points_scored = 0
    vel_x = 0
    vel_y = 0
    pos = {}

    def __init__(self, color, screen, maze, settings, prize):
        self.color = color
        self.screen = screen
        self.maze = maze
        self.settings = settings
        self.prize = prize

    def spawn(self):
        air = self.maze.list_of("air")
        self.pos = {"x": max(air)[0], "y": max(air)[1]}
        self.visual_repr = pygame.Rect(self.pos["x"], self.pos["y"], self.settings.player_size, self.settings.player_size)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update()

    def vanish(self):
        pygame.draw.rect(self.screen.screen, colors.black, self.visual_repr)
        pygame.display.update()

    def update(self):
        self.visual_repr = self.visual_repr.move(self.vel_x, self.vel_y)
        pygame.draw.rect(self.screen.screen, self.color, self.visual_repr)
        pygame.display.update(self.visual_repr)

    def is_collided_with(self, rect):
        return self.pos == rect.pos

    def collision_with_enemy(self, enemy):
        if self.visual_repr.colliderect(enemy.visual_repr):
            self.alive = False
            self.screen.outro_screen(self)
            self.points_scored = 0

    def collision_with_prize(self):
        if self.visual_repr.colliderect(self.prize.visual_repr):
            self.prize.vanish()
            self.prize.scored = True
            self.points_scored += 1

    def collisions(self, enemy):
        self.collision_with_prize()
        self.collision_with_enemy(enemy)
        self.collision_with_wall()

    def collision_with_wall(self):
        if any(self.visual_repr.colliderect(i) for i in self.maze.list_of("walls")):
            self.alive = False
            self.screen.outro_screen(self)
            self.points_scored = 0

    def control(self, pressed_keys):

        if pressed_keys["a"]:
            pressed_keys["a"] = False
            self.vel_x = -self.settings.player_vel_i
            self.vel_y = 0

        elif pressed_keys["d"]:
            pressed_keys["d"] = False
            self.vel_x = self.settings.player_vel_i
            self.vel_y = 0

        elif pressed_keys["w"]:
            pressed_keys["w"] = False
            self.vel_y = -self.settings.player_vel_i
            self.vel_x = 0

        elif pressed_keys["s"]:
            pressed_keys["s"] = False
            self.vel_y = self.settings.player_vel_i
            self.vel_x = 0

    def is_moving(self):
        if any(i != 0 for i in (self.vel_x, self.vel_y)):
            return True
        else:
            return False



# uporzadkowac move