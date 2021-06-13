import pygame
import colors
import random
from sprites import Sprites
from maze import Maze
from enemy import Enemy
from prize import Prize
from player import Player
from screens import Screen
from utils import clear_screen
from boss import Boss
from button import Button
from settings import Settings
from boss_fight import BossFight

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_caption("Maze")

settings = Settings()
screen = Screen(pygame.display.set_mode((settings.window_width, settings.window_height)), Button, settings)
maze = Maze(settings.window_height, settings.window_width)
sprites = Sprites(maze, Enemy, screen, settings)
prize = Prize(screen, maze)
player = Player(colors.blue, screen, maze, settings, prize)
boss = Boss(screen, player, maze, prize, settings)

pressed_keys = {"a": False, "d": False, "w": False, "s": False}


running = True
while running:

    screen.intro_screen()
    clear_screen(screen)
    player.alive = True

    while player.alive:
        player.vel_x = 0
        player.vel_y = 0

        if player.points_scored % 5 != 0  or player.points_scored == 0:
            boss.alive = False
            settings.set_gamemode()
            settings.set_player_size()
            clear_screen(screen)
            maze.generate()
            maze.display(screen)
            player.spawn()
            prize.spawn()
            prize.scored = False
            enemies = sprites.get_enemy_list()
            sprites.spawn_multiple(enemies)
            for enemy in enemies:
                enemy.get_direction()

        else:
            clear_screen(screen)
            maze.create_boss_fight_map()
            maze.display(screen)
            player.spawn()
            settings.player_vel_i = 5
            boss.spawn()
            boss.elements = [boss.visual_repr]
            boss.spawn_health_bar()
            boss.random_vel()
            boss.create_collidepoints(boss.visual_repr)
            pygame.display.update()

        while boss.alive and player.alive:
            prize.scored = False
            prize.spawn_random_pos()

            while not prize.scored and player.alive:
                pygame.time.delay(10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            screen.pause_screen()
                            clear_screen(screen)
                            maze.display(screen)
                            player.vel_x = 0
                            player.vel_y = 0

                        if event.key == pygame.K_a:
                            pressed_keys["a"] = True
                        elif event.key == pygame.K_d:
                            pressed_keys["d"] = True
                        elif event.key == pygame.K_w:
                            pressed_keys["w"] = True
                        elif event.key == pygame.K_s:
                            pressed_keys["s"] = True

                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            pressed_keys["a"] = False
                        if event.key == pygame.K_d:
                            pressed_keys["d"] = False
                        if event.key == pygame.K_w:
                            pressed_keys["w"] = False
                        if event.key == pygame.K_s:
                            pressed_keys["s"] = False

                player.control(pressed_keys)
                player.vanish()
                player.update()

                boss.move()
                boss.update_health_bar()

                prize.update()
                boss.collisions()
                boss.is_alive()
                player.collisions(boss.visual_repr)

        while not prize.scored and player.alive:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screen.pause_screen()
                        clear_screen(screen)
                        maze.display(screen)
                        player.vel_x = 0
                        player.vel_y = 0

                    if event.key == pygame.K_a:
                        pressed_keys["a"] = True
                    elif event.key == pygame.K_d:
                        pressed_keys["d"] = True
                    elif event.key == pygame.K_w:
                        pressed_keys["w"] = True
                    elif event.key == pygame.K_s:
                        pressed_keys["s"] = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        pressed_keys["a"] = False
                    if event.key == pygame.K_d:
                        pressed_keys["d"] = False
                    if event.key == pygame.K_w:
                        pressed_keys["w"] = False
                    if event.key == pygame.K_s:
                        pressed_keys["s"] = False

            player.control(pressed_keys)
            player.vanish()
            player.update()
            prize.update()
            sprites.move(enemies)
            # sprites.handle_collisions(enemies, player, maze.list_of("walls"), maze, prize, screen)
            for enemy in enemies:
                player.collisions(enemy)

            pygame.display.update()

pygame.quit()


# wydzielic kolizje, rozne typy ruchow przeciwnikow
