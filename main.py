import pygame
import sys

from buttons import Buttons

pygame.init()

WIDTH, HEIGHT = (1440, 900)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RoadMap of IT Specialist')

# кнопки менюшки
play_button = Buttons(WIDTH / 2 - (252 / 2), 150, 252, 200, "Play", "images/button.png", "images/button.png",
                      "sounds/click.mp3")

settings_button = Buttons(WIDTH / 2 - (252 / 2), 300, 252, 200, "Settings", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

exit_button = Buttons(WIDTH / 2 - (252 / 2), 450, 252, 200, "Exit", "images/button.png", "images/button.png",
                        "sounds/click.mp3")

# бэк
background = pygame.image.load('images/bg4.jpg')

# бесконченый цикл музыки
pygame.mixer.init()
pygame.mixer.music.load('sounds/perfect-beauty-191271.mp3')
pygame.mixer.music.play(-1)

# иконка игры
icon = pygame.image.load('images/6549993.png')
pygame.display.set_icon(icon)

# шрифт
font = pygame.font.Font("fonts/Lemands.ttf", 40)

# функция перехода
def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # увелечение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()

def show_text(text, x, y, color, font_path="fonts/Lemands.ttf", font_size=24):
    pygame.font.init()
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_options(options):
    option_y = HEIGHT - 120
    for i, option in enumerate(options):
        show_text(f"{i + 1}. {option}", WIDTH // 2, option_y)
        option_y += 40

def prompt(question, options):
    screen.fill(0,0,0)
    show_text(question, WIDTH // 2, HEIGHT // 2 - 50, 40)
    draw_options(options)
    pygame.display.flip()

def main_menu():
    global event
    running = True
    while running:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('RoadMap of IT Specialist', True, 252)
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == play_button:
                print("Play pressed")
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Settings pressed")
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            # цикл кнопок
            for btn in [play_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [play_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

        pygame.display.update()

def settings_menu():

    sound_on = True

    # create buttons
    audio_button = Buttons(WIDTH / 2 - (252 / 2), 100, 252, 200, "Audio", "images/button.png", "images/button.png","sounds/click.mp3")
    video_button = Buttons(WIDTH / 2 - (252 / 2), 200, 252, 200, "Video", "images/button.png", "images/button.png","sounds/click.mp3")
    back_button = Buttons(WIDTH / 2 - (252 / 2), 300, 252, 200, "Back", "images/button.png", "images/button.png","sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (-800, -1200))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('SETTINGS', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # back to menu
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == audio_button:
                sound_on = not sound_on
                if sound_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def new_game():

    early_study_button = Buttons(300, 250, 900, 200, "Start preparing early and study the material on your own", "images/button.png",
                                 "images/button.png",
                                 "sounds/click.mp3")

    late_study_button = Buttons(300, 400, 900, 200, "Put it off until later and hope for a paid training course", "images/button.png",
                                "images/button.png",
                                "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png","sounds/click.mp3")

    running = True
    while running:
        screen.fill((0,0,0))

        screen.blit(background, (-100, -1300))

        font = pygame.font.Font(None, 84)
        text_surface = font.render('Welcome to RoadMap of IT specialist!', True, (30, 144, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("You are finishing school. And you must pass the ENT, choose a preparation method:", 150, 200, 252,"fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == early_study_button:
                fade()
                ENT100()

            if event.type == pygame.USEREVENT and event.button == late_study_button:
                fade()
                ENT70()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, early_study_button, late_study_button]:
                btn.handle_event(event)

        for btn in [back_button, early_study_button, late_study_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def ENT100():
    aitu_button = Buttons(300, 450, 252, 200, "AITU", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    sdu_button = Buttons(900, 450, 252, 200, "SDU", "images/button.png", "images/button.png",
                         "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png","sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-800, -1200))

        font = pygame.font.Font(None, 54)
        text_surface = font.render('Congratulations ! You scored 100 points on ENT, you have a good choice.', True, (30, 144, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("Which university will you choose ?", 500, 200, 252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == aitu_button:
                fade()
                aitu_se()

            if event.type == pygame.USEREVENT and event.button == sdu_button:
                fade()
                sdu_cs()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, aitu_button, sdu_button]:
                btn.handle_event(event)

        for btn in [back_button, aitu_button, sdu_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def ENT70():

    aitu_cb_button = Buttons(300, 450, 252, 200, "AITU CB", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    enu_se_button = Buttons(900, 450, 252, 200, "ENU SE", "images/button.png", "images/button.png",
                         "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1550, -555))

        font = pygame.font.Font(None, 54)
        text_surface = font.render('Congratulations! You scored 70 points on ENT, you have a good choice of University.', True,
                                   (30, 144, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("Which university will you choose ?", 500, 200, 252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == enu_se_button:
                fade()
                fail()

            if event.type == pygame.USEREVENT and event.button == aitu_cb_button:
                fade()
                aitu_se()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, enu_se_button, aitu_cb_button]:
                btn.handle_event(event)

        for btn in [back_button, enu_se_button, aitu_cb_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def aitu_se():

    aitu_button_shyryn = Buttons (300, 450, 252, 200, "Tutkyshbaeva Shyryn", "images/button.png",
                                 "images/button.png",
                                 "sounds/click.mp3")

    aitu_button_random = Buttons(900, 450, 252, 200, "Random teacher", "images/button.png",
                                 "images/button.png",
                                 "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-2000, -600))

        font = pygame.font.Font(None, 54)
        text_surface = font.render('Welcome to Astana IT University, one of the best universities in Kazakhstan.', True,
                                   (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("You have the choice of a Programming teacher.", 450, 200, 252, "fonts/Lemands.ttf", 36)

        show_text("Which teacher will you choose?", 500, 300, 252, "fonts/Lemands.ttf",42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == aitu_button_shyryn:
                fade()
                aitu_se_shyryn_passion()

            if event.type == pygame.USEREVENT and event.button == aitu_button_random:
                fade()
                fail()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, aitu_button_shyryn, aitu_button_random]:
                btn.handle_event(event)

        for btn in [back_button, aitu_button_shyryn, aitu_button_random]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def aitu_se_shyryn_passion():

    aitu_button_shyryn_right_study = Buttons(300, 450, 252, 200, "Active",
                                             "images/button.png", "images/button.png",
                                             "sounds/click.mp3")

    aitu_button_shyryn_wrong_study = Buttons(900, 450, 252, 200, "Passive",
                                             "images/button.png", "images/button.png",
                                             "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-550, -300))

        font = pygame.font.Font(None, 54)
        text_surface = font.render('Now your teacher is Tutkyshbaeva Shyryn? ', True,
                                   (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("How would your study ? ", 550, 200,
                  252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == aitu_button_shyryn_right_study:
                fade()
                success()

            if event.type == pygame.USEREVENT and event.button == aitu_button_shyryn_wrong_study:
                fade()
                success()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, aitu_button_shyryn_right_study, aitu_button_shyryn_wrong_study]:
                btn.handle_event(event)

        for btn in [back_button, aitu_button_shyryn_right_study, aitu_button_shyryn_wrong_study]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def sdu_cs():

    sdu_button_city = Buttons(300, 300, 252, 200, "City", "images/button.png", "images/button.png",
                              "sounds/click.mp3")

    sdu_button_kaskelen = Buttons(900, 300, 252, 200, "Kaskelen", "images/button.png",
                                  "images/button.png",
                                  "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1200, -600))

        font = pygame.font.Font(None, 64)
        text_surface = font.render('You chose SDU !', True,
                                   (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("Where you want to live ?", 550, 200, 252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == sdu_button_city:
                fade()
                sdu_cs_city_hobbies()

            if event.type == pygame.USEREVENT and event.button == sdu_button_kaskelen:
                fade()
                sdu_cs_kaskelen_personality()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, sdu_button_kaskelen, sdu_button_city]:
                btn.handle_event(event)

        for btn in [back_button, sdu_button_kaskelen, sdu_button_city]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def sdu_cs_kaskelen_personality():

    sdu_button_kaskelen_introvert = Buttons(300, 450, 252, 200, "introvert", "images/button.png",
                                            "images/button.png",
                                            "sounds/click.mp3")

    sdu_button_kaskelen_extravert = Buttons(900, 450, 252, 200, "extravert", "images/button.png",
                                            "images/button.png",
                                            "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1500, -300))

        font = pygame.font.Font(None, 64)
        text_surface = font.render('You chose SDU !', True,
                                   (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("What is your personality ?", 550, 200, 252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == sdu_button_kaskelen_extravert:
                fade()
                medium()

            if event.type == pygame.USEREVENT and event.button == sdu_button_kaskelen_introvert:
                fade()
                fail()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, sdu_button_kaskelen_introvert, sdu_button_kaskelen_extravert]:
                btn.handle_event(event)

        for btn in [back_button, sdu_button_kaskelen_introvert, sdu_button_kaskelen_extravert]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def sdu_cs_city_hobbies():

    sdu_button_city_work = Buttons(300, 450, 252, 200, "work", "images/button.png",
                                   "images/button.png",
                                   "sounds/click.mp3")

    sdu_button_city_study = Buttons(900, 450, 252, 200, "study", "images/button.png",
                                    "images/button.png",
                                    "sounds/click.mp3")

    back_button = Buttons(WIDTH / 2 - (252 / 2), 550, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1200, -600))

        font = pygame.font.Font(None, 64)
        text_surface = font.render('You chose SDU !', True,
                                   (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        show_text("What will you do beside study ?", 500, 200, 252, "fonts/Lemands.ttf", 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == sdu_button_city_work:
                fade()
                medium()

            if event.type == pygame.USEREVENT and event.button == sdu_button_city_study:
                fade()
                success()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            for btn in [back_button, sdu_button_city_work, sdu_button_city_study]:
                btn.handle_event(event)

        for btn in [back_button, sdu_button_city_work, sdu_button_city_study]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def success():
    back_button = Buttons(WIDTH / 2 - (252 / 2), 250, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    try_again_button = Buttons(WIDTH / 2 - (252 / 2), 350, 252, 300, "Try again", "images/button.png",
                               "images/button.png",
                               "sounds/click.mp3")

    exit_button = Buttons(WIDTH / 2 - (252 / 2), 500, 252, 200, "Exit", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1850, -200))

        show_text("Congratulations. You have chosen the right path. You are a successful IT specialist!", 300, 200, 252,
                  "fonts/Lemands.ttf", 36)

        show_text("Want to try again ?", 200, 478, 252,
                  "fonts/Lemands.ttf", 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            if event.type == pygame.USEREVENT and event.button == try_again_button:
                new_game()
                fade()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [try_again_button, exit_button, back_button]:
                btn.handle_event(event)

        for btn in [try_again_button, exit_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def medium():
    back_button = Buttons(WIDTH / 2 - (252 / 2), 250, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    try_again_button = Buttons(WIDTH / 2 - (252 / 2), 350, 252, 300, "Try again", "images/button.png",
                               "images/button.png",
                               "sounds/click.mp3")

    exit_button = Buttons(WIDTH / 2 - (252 / 2), 500, 252, 200, "Exit", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1850, -200))

        show_text("You are medium IT specialist! Your maximum is Kazakhstan companies", 300, 200, 252,
                  "fonts/Lemands.ttf", 36)

        show_text("Want to try again ?", 200, 478, 252,
                  "fonts/Lemands.ttf", 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            if event.type == pygame.USEREVENT and event.button == try_again_button:
                new_game()
                fade()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [try_again_button, exit_button, back_button]:
                btn.handle_event(event)

        for btn in [try_again_button, exit_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def fail():

    back_button = Buttons(WIDTH / 2 - (252 / 2), 250, 252, 300, "Back", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    try_again_button = Buttons(WIDTH / 2 - (252 / 2), 350, 252, 300, "Try again", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    exit_button = Buttons(WIDTH / 2 - (252 / 2), 500, 252, 200, "Exit", "images/button.png", "images/button.png",
                          "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (-1850, -200))

        show_text("Unfortunately you have failed your path to become IT specialist =(", 300, 200, 252,
                  "fonts/Lemands.ttf", 36)

        show_text("Want to try again ?", 200, 478, 252,
                  "fonts/Lemands.ttf", 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()

            if event.type == pygame.USEREVENT and event.button == try_again_button:
                new_game()
                fade()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [try_again_button, exit_button, back_button]:
                btn.handle_event(event)

        for btn in [try_again_button, exit_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()


