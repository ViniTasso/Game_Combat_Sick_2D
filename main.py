
import sys
import os

from src.game import Game

# Adiciona 'src/' ao caminho do Python para encontrar os módulos corretamente
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


if __name__ == "__main__":
    game = Game()
    game.run()