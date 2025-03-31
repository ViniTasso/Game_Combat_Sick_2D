
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from src.settings import *

from src.settings import SCREEN_WIDTH, C_ORANGE, MENU_OPTION, WHITE, C_YELLOW

class Menu:

    def __init__(self, screen):
        self.screen = screen #em outros projetos chamam a var de "window"
        self.surf = pygame.image.load("assets/images/bg_menu.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        #self.screen.blit(pygame.image.load("assets/images/background.png"), (0, 0))

    def run(self):
        menu_option = 0

        #inicializa a música
        pygame.mixer_music.load('./assets/sounds/fase1.mp3')
        pygame.mixer_music.play(-1)

        #inicializa menu
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Combat", C_ORANGE, ((SCREEN_WIDTH / 2), 70))
            self.menu_text(50, "Sick", C_ORANGE, ((SCREEN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((SCREEN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], WHITE, ((SCREEN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip() #Atualiza Screen

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

    def about(self):
        
        while(True):
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Combat", C_ORANGE, ((SCREEN_WIDTH / 2), 70))
            self.menu_text(50, "Sick", C_ORANGE, ((SCREEN_WIDTH / 2), 120))
            self.menu_text(20, "PRESSIONE ENTER PARA SAIR", WHITE, ((SCREEN_WIDTH / 2), 550))
            print("em sobre o jogo")
            auxilia_montagem = ["É um jogo educativo!",
                "A maior missão é demonstrar como as contaminações ocorrem,",
                "e como é possível prevenir, ou até mesmo tratar certos casos.",
                "Jogo Criado inteiramente pelo autor Vinícius Tasso RU:4632546.",
                "A primeira fase trata-se da Influenza, vulgo Gripe.",
                "A segunda fase está em desenvolvimento e será sobre salmonela."
            ]
            for i in range(len(auxilia_montagem)):
                self.menu_text(20, auxilia_montagem[i], WHITE, ((SCREEN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip() #Atualiza Screen
            #check event to leave
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER
                        return ""

    def fases_game(self):
            
            while(True):
                self.screen.blit(source=self.surf, dest=self.rect)
                self.menu_text(50, "Combat", C_ORANGE, ((SCREEN_WIDTH / 2), 70))
                self.menu_text(50, "Sick", C_ORANGE, ((SCREEN_WIDTH / 2), 120))
                self.menu_text(20, "PRESSIONE ENTER PARA SAIR", WHITE, ((SCREEN_WIDTH / 2), 550))

                auxilia_montagem = ["Por enquanto só tem uma fase!",
                    "ainda será construido outras fases e mais objetivos.",
                    "Por enquanto, o foco principal foi",
                    "na relação entre as classes.",
                    "Não foi trabalhado a apresentação, front-end, porem muitas",
                    "funcionalidades são facilmente replicadas.",
                    "Obrigado pela compreensão!"
                ]
                for i in range(len(auxilia_montagem)):
                    self.menu_text(20, auxilia_montagem[i], WHITE, ((SCREEN_WIDTH / 2), 200 + 25 * i))

                pygame.display.flip() #Atualiza Screen
                #check event to leave
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Close Window
                        quit()  # end pygame
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:  # ENTER
                            return ""
    def config(self):
            
            while(True):
                self.screen.blit(source=self.surf, dest=self.rect)
                self.menu_text(50, "Combat", C_ORANGE, ((SCREEN_WIDTH / 2), 70))
                self.menu_text(50, "Sick", C_ORANGE, ((SCREEN_WIDTH / 2), 120))
                self.menu_text(20, "PRESSIONE ENTER PARA SAIR", WHITE, ((SCREEN_WIDTH / 2), 550))

                auxilia_montagem = ["CONFIGURAÇÕES:",
                    f"O FPS do jogo esta configurado em: {FPS} FPS's",
                    "A tela esta configurada para a seguinte dimensão:",
                    f"WIDTH: {SCREEN_WIDTH}, e o HEIGHT: {SCREEN_HEIGHT}.",
                    "As configurações ainda não são ajustáveis!"
                ]
                for i in range(len(auxilia_montagem)):
                    self.menu_text(20, auxilia_montagem[i], WHITE, ((SCREEN_WIDTH / 2), 200 + 25 * i))

                pygame.display.flip() #Atualiza Screen
                #check event to leave
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Close Window
                        quit()  # end pygame
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:  # ENTER
                            return ""
