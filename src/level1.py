# Código da Fase 1

import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.settings import *

print('Fase 1 iniciada')
class Fase_1:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("assets/images/bg_fase_1.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pass