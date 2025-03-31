import pygame

class Weapon:
    def __init__(self, image_path, damage):
        self.image = pygame.image.load(image_path)
        self.damage = damage

    def use(self, enemy):
        enemy.health -= self.damage
