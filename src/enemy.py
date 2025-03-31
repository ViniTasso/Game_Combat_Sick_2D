import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, speed):
        super().__init__()
        image = pygame.image.load(imagem)
        self.image = pygame.transform.scale(image, (40, 40))

        self.rect = self.image.get_rect(center=(x, y))
        
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def update(self):
        type_moviment = 3
        if type_moviment == 1: #movimento horizontal constante
            self.rect.x += self.speed  # Exemplo de movimento lateral
            if self.rect.left < 0 or self.rect.right > 800: #atualizar depois SCREEN_WIDTH:
                self.speed *= -1  # Inverte a direção ao bater na borda
        elif type_moviment == 2: #movimento aleatório
            self.rect.x += random.choice([-5, 5])
            self.rect.y += random.choice([-5, 5])


