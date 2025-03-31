# Gerenciador de som

import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
    
    def play_sound(self, sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()