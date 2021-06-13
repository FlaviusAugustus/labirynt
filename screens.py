import pygame
import utils


class Screen:

    height = 1050
    width = 1450

    def __init__(self, screen, Button, settings):
        self.screen = screen
        self.Button = Button
        self.settings = settings

    def intro_screen(self):
        utils.clear_screen(self)

        start_button = self.Button(self.width // 2, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220), "Play", 50, (255, 255, 255), self.screen)
        settings_button = self.Button((self.width // 2) + 350, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220), "Settings", 50, (255, 255, 255), self.screen)
        quit_button = self.Button((self.width // 2) - 350, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220), "Quit", 50, (255, 255, 255), self.screen)

        start_button.create()
        settings_button.create()
        quit_button.create()

        visible = True
        while visible:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or quit_button.button.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.button.collidepoint(pygame.mouse.get_pos()):
                        visible = False
                    elif settings_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings_screen()
                        utils.clear_screen(self)

                        start_button.create()
                        settings_button.create()
                        quit_button.create()


                elif event.type == pygame.MOUSEMOTION:
                    start_button.blink_on_hover()
                    settings_button.blink_on_hover()
                    quit_button.blink_on_hover()

            big_message, text_rect_1 = utils.display_message("Maze", 115, (self.settings.window_width // 2, self.settings.window_height // 3))
            self.screen.blit(big_message, text_rect_1)

            pygame.display.update()
    
    
    def outro_screen(self, player):
        visible = True
        while visible:
            utils.clear_screen(self)
            big_message, text_rect_1 = utils.display_message(f"You Lost!, you scored {player.points_scored} points!", 70,
                                                       (self.settings.window_width // 2, self.settings.window_height // 2))
            small_message, text_rect_2 = utils.display_message("press ""esc"" to try again", 20,
                                                         (self.settings.window_width  // 2, self.settings.window_height // 2 + 50))
            self.screen.blit(big_message, text_rect_1)
            self.screen.blit(small_message, text_rect_2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    visible = False
                    utils.clear_screen(self)
                    pygame.display.update()


    def settings_screen(self):
        visible = True

        utils.clear_screen(self)
        medium_button = self.Button(self.width // 2, self.height // 4, 300, 75, (255, 255, 255), (220, 220, 220), "Medium", 50, (255, 255, 255), self.screen)
        hard_button = self.Button((self.width // 2) + 350, self.height // 4, 300, 75, (255, 255, 255), (220, 220, 220), "Hard", 50, (255, 255, 255), self.screen)
        easy_button = self.Button((self.width // 2) - 350, self.height // 4, 300, 75, (255, 255, 255), (220, 220, 220), "Easy", 50, (255, 255, 255), self.screen)

        small_button = self.Button(self.width // 2, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220), "Small", 50, (255, 255, 255), self.screen)
        normal_button = self.Button((self.width // 2) + 350, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220),"Normal", 50, (255, 255, 255), self.screen)
        big_button = self.Button((self.width // 2) - 350, self.height // 2, 300, 75, (255, 255, 255), (220, 220, 220), "Big", 50, (255, 255, 255), self.screen)

        buttons = [medium_button, hard_button, easy_button, small_button, normal_button, big_button]
        for button in buttons:
            button.create()

        if self.settings.gamemode == "easy":
            easy_button.is_chosen = True
        if self.settings.gamemode == "medium":
            medium_button.is_chosen = True
        if self.settings.gamemode == "hard":
            hard_button.is_chosen = True

        if self.settings.player_type == "small":
            small_button.is_chosen = True
        if self.settings.player_type == "normal":
            normal_button.is_chosen = True
        if self.settings.player_type == "big":
            big_button.is_chosen = True


        while visible:

            for button in buttons:
                button.show_chosen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    visible = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.gamemode = "easy"
                        easy_button.is_chosen = True
                        medium_button.is_chosen = False
                        hard_button.is_chosen = False

                    elif medium_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.gamemode = "medium"
                        medium_button.is_chosen = True
                        easy_button.is_chosen = False
                        hard_button.is_chosen = False

                    elif hard_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.gamemode = "hard"
                        hard_button.is_chosen = True
                        medium_button.is_chosen = False
                        easy_button.is_chosen = False


                    if small_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.player_type = "small"
                        small_button.is_chosen = True
                        normal_button.is_chosen = False
                        big_button.is_chosen = False

                    elif normal_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.player_type = "normal"
                        small_button.is_chosen = False
                        normal_button.is_chosen = True
                        big_button.is_chosen = False

                    elif big_button.button.collidepoint(pygame.mouse.get_pos()):
                        self.settings.player_type = "big"
                        small_button.is_chosen = False
                        normal_button.is_chosen = False
                        big_button.is_chosen = True

                elif event.type == pygame.MOUSEMOTION:

                    for button in buttons:
                        button.blink_on_hover()







            gamemode_text, text_rect_1 = utils.display_message("Game mode", 50, (self.settings.window_width  // 2, (self.settings.window_height // 4) - 120))
            size_text, text_rect_2 = utils.display_message("Player size", 50, (self.settings.window_width  // 2, (self.settings.window_height // 4)*2 - 120))
            self.screen.blit(gamemode_text, text_rect_1)
            self.screen.blit(size_text, text_rect_2)
            pygame.display.update()
        utils.clear_screen(self)
    
    
    def pause_screen(self):
        visible = True
        while visible:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    visible = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        visible = False
    
            utils.clear_screen(self)
            pause_text, text_rect_1 = utils.display_message("Paused", 115, (self.settings.window_width // 2, self.settings.window_height // 2))
            resume_text, text_rect_2 = utils.display_message("Press ""esc"" to continue", 25,
                                                       (self.settings.window_width // 2, self.settings.window_height // 2 + 50))
            self.screen.blit(pause_text, text_rect_1)
            self.screen.blit(resume_text, text_rect_2)
            pygame.display.update()