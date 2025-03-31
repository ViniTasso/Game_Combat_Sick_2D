import os

# Estrutura de pastas do jogo
folders = [
    "microworld_game",
    "microworld_game/assets",
    "microworld_game/assets/images",
    "microworld_game/assets/sounds",
    "microworld_game/assets/fonts",
    "microworld_game/src",
    "microworld_game/utils"
]

# Arquivos que serão criados
files = {
    "microworld_game/main.py": "# Arquivo principal do jogo\n\nimport pygame\nfrom src.game import Game\n\ngame = Game()\ngame.run()",
    "microworld_game/README.md": "# Microworld Game\n\nEste é um jogo educativo sobre vírus e doenças.",
    
    "microworld_game/src/__init__.py": "",
    "microworld_game/src/settings.py": "# Configurações do jogo\n\nSCREEN_WIDTH = 800\nSCREEN_HEIGHT = 600\nFPS = 60",
    "microworld_game/src/game.py": "# Lógica principal do jogo\n\nimport pygame\n\nclass Game:\n    def __init__(self):\n        pygame.init()\n        self.screen = pygame.display.set_mode((800, 600))\n        self.clock = pygame.time.Clock()\n\n    def run(self):\n        running = True\n        while running:\n            for event in pygame.event.get():\n                if event.type == pygame.QUIT:\n                    running = False\n            self.screen.fill((255, 255, 255))\n            pygame.display.flip()\n            self.clock.tick(60)\n        pygame.quit()",
    
    "microworld_game/src/player.py": "# Classe do jogador\n\nimport pygame\n\nclass Player(pygame.sprite.Sprite):\n    def __init__(self):\n        super().__init__()\n        self.image = pygame.Surface((50, 50))\n        self.image.fill((0, 0, 255))\n        self.rect = self.image.get_rect(center=(400, 500))\n    \n    def update(self, keys):\n        if keys[pygame.K_LEFT]:\n            self.rect.x -= 5\n        if keys[pygame.K_RIGHT]:\n            self.rect.x += 5",
    
    "microworld_game/src/enemy.py": "# Classe dos inimigos\n\nimport pygame\nimport random\n\nclass Enemy(pygame.sprite.Sprite):\n    def __init__(self, x, y):\n        super().__init__()\n        self.image = pygame.Surface((40, 40))\n        self.image.fill((255, 0, 0))\n        self.rect = self.image.get_rect(center=(x, y))\n    \n    def update(self):\n        self.rect.x += random.choice([-2, 2])",
    
    "microworld_game/src/items.py": "# Classe para os itens do jogo\n\nimport pygame\n\nclass Item(pygame.sprite.Sprite):\n    def __init__(self, x, y, color):\n        super().__init__()\n        self.image = pygame.Surface((30, 30))\n        self.image.fill(color)\n        self.rect = self.image.get_rect(center=(x, y))",
    
    "microworld_game/src/level1.py": "# Código da Fase 1\n\nfrom src.settings import *\n\nprint('Fase 1 iniciada')",
    "microworld_game/src/level2.py": "# Código da Fase 2\n\nprint('Fase 2 iniciada')",
    "microworld_game/src/level3.py": "# Código da Fase 3\n\nprint('Fase 3 iniciada')",
    "microworld_game/src/level4.py": "# Código da Fase 4\n\nprint('Fase 4 iniciada')",
    
    "microworld_game/utils/__init__.py": "",
    "microworld_game/utils/helpers.py": "# Funções auxiliares\n\ndef load_image(path):\n    return pygame.image.load(path)",
    "microworld_game/utils/sound_manager.py": "# Gerenciador de som\n\nimport pygame\n\nclass SoundManager:\n    def __init__(self):\n        pygame.mixer.init()\n    \n    def play_sound(self, sound_file):\n        sound = pygame.mixer.Sound(sound_file)\n        sound.play()",
}

# Criar pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criar arquivos
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Estrutura do projeto criada com sucesso!")
