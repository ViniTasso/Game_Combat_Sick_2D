
from overrides import override
from src.enemy import Enemy
from src.settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import random

class Influenza(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, imagem="assets/images/influenza.png", speed=2)
        self.speed = 2 #random.choice([-2, 2])
        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()  # Direção aleatória

        self.change_direction_timer = 0  # Contador para mudança de direção

    #def draw(self, screen):
    #    screen.blit(self.image, self.rect)

    @override
    def update(self):
        #super().update()
        # Movimenta o inimigo
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Rebater nas bordas da tela
        if self.rect.left <= 0 or self.rect.right >= 800:  # 800 → largura da tela
            self.direction.x *= -1  # Inverte a direção X
        if self.rect.top <= 0 or self.rect.bottom >= 600:  # 600 → altura da tela
            self.direction.y *= -1  # Inverte a direção Y

        # Muda a direção aleatoriamente a cada 2 segundos (~120 frames se FPS=60)
        self.change_direction_timer += 1
        if self.change_direction_timer > 30:
            self.change_direction()
            self.change_direction_timer = 0  # Reinicia o contador

    def change_direction(self):
        """Muda a direção para um valor aleatório, essa função gera valores entre 1 e -1 
                a probabilidade dos valores seguidos serem os mesmos e o personagem manter apenas uma direção 
                é grande, por isso, mudei para angulação. mantém a velocidade constante."""
        #self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        """Muda a direção para um valor aleatório, garantindo diversidade nos movimentos."""
        angle = random.uniform(0, 360)  # Gera um ângulo aleatório
        self.direction = pygame.Vector2(1, 0).rotate(angle)  # Cria movimento aleatório

        # Se estiver muito perto das bordas, força a direção para dentro da tela
        if self.rect.left < 50:
            self.direction.x = abs(self.direction.x)  # Força movimento para a direita
        elif self.rect.right > SCREEN_WIDTH - 50:
            self.direction.x = -abs(self.direction.x)  # Força movimento para a esquerda

        if self.rect.top < 50:
            self.direction.y = abs(self.direction.y)  # Força movimento para baixo
        elif self.rect.bottom > SCREEN_HEIGHT - 50:
            self.direction.y = -abs(self.direction.y)  # Força movimento para cima