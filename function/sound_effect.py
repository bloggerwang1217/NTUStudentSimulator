import pygame
from pygame import mixer

pygame.mixer.init()

click_sound = pygame.mixer.Sound("音效/遊戲中的點擊聲.mp3")
enter_game_sound = pygame.mixer.Sound("音效/進入遊戲按鈕！.mp3")

def play_background_music(filename):
    pygame.mixer.music.load((f"音效/{filename}.mp3"))
    pygame.mixer.music.play()

def play_event_background_music(name1, name2):
    pygame.mixer.music.load((f"音效/{name1}/{name2}.mp3"))
    pygame.mixer.music.play()

def play_button_sound():
    click_sound.play()

def enter_game_button_sound():
    enter_game_sound.play()