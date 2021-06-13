import pygame


class BossFight:


    def __init__(self, boss, screen, maze):
        self.boss = boss
        self. screen = screen
        self.maze = maze


    def create_map(self):
        height = self.maze.m_height // 50
        width = self.maze.m_width // 50

        map = []
        for i in range(height):
            if i == 0 or i == height - 1:
                map.append(["#", "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#", "#","#","#","#","#","#","#","#","#","#","#","#"])
            else:
                map.append(["#"," ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"])

        self.maze.maze = map





