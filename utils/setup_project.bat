@echo off
setlocal

:: Define a pasta principal do jogo
set GAME_DIR=microworld_game

:: Criação das pastas
echo Criando pastas...
mkdir %GAME_DIR% 2>nul
mkdir %GAME_DIR%\assets 2>nul
mkdir %GAME_DIR%\assets\images 2>nul
mkdir %GAME_DIR%\assets\sounds 2>nul
mkdir %GAME_DIR%\assets\fonts 2>nul
mkdir %GAME_DIR%\src 2>nul
mkdir %GAME_DIR%\utils 2>nul

:: Criando arquivos com conteúdo básico
echo Criando arquivos...

(
echo # Arquivo principal do jogo
echo import pygame
echo from src.game import Game
echo.
echo game = Game()
echo game.run()
) > %GAME_DIR%\main.py

(
echo # Configurações do jogo
echo SCREEN_WIDTH = 800
echo SCREEN_HEIGHT = 600
echo FPS = 60
) > %GAME_DIR%\src\settings.py

(
echo # Lógica principal do jogo
echo import pygame
echo.
echo class Game:
echo     def __init__(self):
echo         pygame.init()
echo         self.screen = pygame.display.set_mode((800, 600))
echo         self.clock = pygame.time.Clock()
echo.
echo     def run(self):
echo         running = True
echo         while running:
echo             for event in pygame.event.get():
echo                 if event.type == pygame.QUIT:
echo                     running = False
echo             self.screen.fill((255, 255, 255))
echo             pygame.display.flip()
echo             self.clock.tick(60)
echo         pygame.quit()
) > %GAME_DIR%\src\game.py

(
echo # Classe do jogador
echo import pygame
echo.
echo class Player(pygame.sprite.Sprite):
echo     def __init__(self):
echo         super().__init__()
echo         self.image = pygame.Surface((50, 50))
echo         self.image.fill((0, 0, 255))
echo         self.rect = self.image.get_rect(center=(400, 500))
echo.
echo     def update(self, keys):
echo         if keys[pygame.K_LEFT]:
echo             self.rect.x -= 5
echo         if keys[pygame.K_RIGHT]:
echo             self.rect.x += 5
) > %GAME_DIR%\src\player.py

(
echo # Classe dos inimigos
echo import pygame
echo import random
echo.
echo class Enemy(pygame.sprite.Sprite):
echo     def __init__(self, x, y):
echo         super().__init__()
echo         self.image = pygame.Surface((40, 40))
echo         self.image.fill((255, 0, 0))
echo         self.rect = self.image.get_rect(center=(x, y))
echo.
echo     def update(self):
echo         self.rect.x += random.choice([-2, 2])
) > %GAME_DIR%\src\enemy.py

(
echo # Código da Fase 1
echo from src.settings import *
echo.
echo print('Fase 1 iniciada')
) > %GAME_DIR%\src\level1.py

(
echo # Código da Fase 2
echo print('Fase 2 iniciada')
) > %GAME_DIR%\src\level2.py

(
echo # Código da Fase 3
echo print('Fase 3 iniciada')
) > %GAME_DIR%\src\level3.py

(
echo # Código da Fase 4
echo print('Fase 4 iniciada')
) > %GAME_DIR%\src\level4.py

(
echo # Funções auxiliares
echo def load_image(path):
echo     return pygame.image.load(path)
) > %GAME_DIR%\utils\helpers.py

(
echo # Gerenciador de som
echo import pygame
echo.
echo class SoundManager:
echo     def __init__(self):
echo         pygame.mixer.init()
echo.
echo     def play_sound(self, sound_file):
echo         sound = pygame.mixer.Sound(sound_file)
echo         sound.play()
) > %GAME_DIR%\utils\sound_manager.py

(
echo # Microworld Game
echo Este é um jogo educativo sobre vírus e doenças.
) > %GAME_DIR%\README.md

echo Estrutura do projeto criada com sucesso!
pause
