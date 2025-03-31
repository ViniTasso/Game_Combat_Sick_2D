# Classe para os itens do jogo

import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((70, 70))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        
    def __init__(self,x, y, imagem):
        super().__init__()
        self.image = pygame.transform.scale(imagem, (70, 70))
        self.rect = self.image.get_rect(center=(x, y))

    def get_rect(self):
        return (self.rect.x, self.rect.y)
