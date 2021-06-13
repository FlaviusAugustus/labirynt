import random


class Settings:

    enemies_count = 2
    gamemode = "medium"
    window_width = 1450
    window_height = 1050

    player_type = "normal"
    player_size = 1

    enemy_vel_i = 1


    def set_gamemode(self):
        if self.gamemode == "easy":
            self.enemies_count = 1
            self.player_vel_i = random.randrange(3, 4)
            self.enemy_vel_i = random.randrange(1, 2)

        elif self.gamemode == "medium":
            self.enemies_count = random.randrange(1,2)
            self.player_vel_i = random.randrange(4,5)
            self.enemy_vel_i = random.randrange(2,3)

        elif self.gamemode == "hard":
            self.enemies_count = random.randrange(2,3)
            self.player_vel_i = random.randrange(5,6)
            self.enemy_vel_i = random.randrange(2,4)

    def set_player_size(self):
        if self.player_type == "normal":
            self.player_size = 15
        if self.player_type == "small":
            self.player_size = 10
        if self.player_type == "big":
            self.player_size = 25

