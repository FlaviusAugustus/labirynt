import utils
import pygame
import random
import colors


class Sprites:

    def __init__(self, maze, enemy, screen, settings):
        self.maze = maze
        self.enemy = enemy
        self.screen = screen
        self.settings = settings

    def move(self, enemies):
        if len(enemies) == 0:
            return
        for enemy in enemies:
            enemy.move()

    def spawn_multiple(self, sprites):
        for sprite in sprites:
            sprite.spawn()

    def vanish(self, prize, enemies, player):
        player.vanish()
        prize.vanish()
        for enemy in enemies:
            enemy.vanish()

    def get_enemy_list(self):
        enemies = []
        for i in range(self.settings.enemies_count):
            enemies.append(self.enemy(colors.red, self.screen, self.maze, self.settings, self.screen))

        return enemies

    def handle_collisions(self, enemies, player, walls, settings, prize, screen):


        if any(player.visual_repr.colliderect(i) for i in walls):
            player.alive = False
            screen.outro_screen(player)
            player.points_scored = 0

        for enemy in enemies:
            if player.collision_with_enemy(enemy):
                player.alive = False
                prize.scored = False
                screen.outro_screen(player)
                player.points_scored = 0


        if player.visual_repr.colliderect(prize.visual_repr):
            prize.scored = True
            player.points_scored += 1
            utils.clear_screen(screen)
            self.vanish(prize, enemies, player)




# gra w zycie, dynamiczny rozmiar planszy, jesli komorka sasiaduje z bokiem planszy to wszystko za krawedzia jest martwe

