import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(image, (48, 60))
        self.rect = self.image.get_rect(center=(48, 60))
        self.speed = 5
        self.has_mask = False
        self.vaccinate = False
        self.life = 10

    def update(self, keys):
        #keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]  and self.rect.bottom < SCREEN_WIDTH: 
            self.rect.y += self.speed

    #def draw(self, screen): não é necessário pois controlo o draw no game
    #    screen.blit(self.image, self.rect)
