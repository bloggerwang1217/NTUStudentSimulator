import pygame
from pygame import mixer
from pathlib import Path

pygame.mixer.init()

click_sound = pygame.mixer.Sound(Path("sound_effect/click_sound.mp3"))
enter_game_sound = pygame.mixer.Sound(Path("sound_effect/enter_game_sound.mp3"))
get_letter_sound = pygame.mixer.Sound(Path("sound_effect/get_letter_sound.mp3"))

def play_background_music(filename):
    pygame.mixer.music.load(Path(f"sound_effect/{filename}.mp3"))
    pygame.mixer.music.play()


def play_event_background_music(name1, name2):
    pygame.mixer.music.load(Path(f"sound_effect/{name1}/{name2}.mp3"))
    pygame.mixer.music.play()


def play_achievement_music(filename):
    pygame.mixer.music.load(Path(f"sound_effect/achievement/{filename}.mp3"))
    pygame.mixer.music.play()


def play_button_sound():
    click_sound.play()


def enter_game_button_sound():
    enter_game_sound.play()


def play_get_letter_sound():
    get_letter_sound.play()