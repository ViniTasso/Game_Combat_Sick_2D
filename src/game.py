


from src.menu import Menu
from src.player import Player
from src.influenza import Influenza
from src.itens import Item
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, BLACK, MENU_OPTION
import pygame
import random
from pygame import Surface, Rect
from pygame.font import Font

class Game:
    # Carregar imagens
    player_img = pygame.image.load("assets/images/player.png")
    influenza_img = pygame.image.load("assets/images/influenza.png")
    mask_img = pygame.image.load("assets/images/mask.png")
    vaccine_img = pygame.image.load("assets/images/vaccine.png")
    background = pygame.image.load("./assets/images/bg_fase_1.png")
    

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Microworld - Fase 1: Combate à Influenza")
        self.surf = self.background.convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.exec = 0
        self.timer = 0
        self.frame = 0
        self.message_stack = []
        self.ultimo_respaw = 1
    
    def repel_objects(self, obj1, obj2, distance=25):
        """_summary_
            Essa função apenas repele os objetos que encostaram um no outro.
            
        Args:
            obj1 (_type_): _description_
            obj2 (_type_): _description_
            distance (int, optional): Define a distância que o objeto ira afastar em pixel. Defaults to 25.
        """
        dx = obj1.rect.x - obj2.rect.x
        dy = obj1.rect.y - obj2.rect.y
        if dx == 0 and dy == 0:
            dx, dy = 1, 1  # Para evitar divisão por zero

        magnitude = (dx**2 + dy**2) ** 0.5
        dx /= magnitude
        dy /= magnitude

        obj1.rect.x += int(dx * distance)
        obj1.rect.y += int(dy * distance)
        obj2.rect.x -= int(dx * distance)
        obj2.rect.y -= int(dy * distance)

    def colisao_enemy(self, enemies: pygame.sprite.Group, player, all_sprites):
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                # 1️⃣ Repulsão entre o player e o inimigo
                self.repel_objects(player, enemy)

                # 2️⃣ Criar dois novos inimigos perto do local do inimigo original
                if (self.timer - self.ultimo_respaw) > 2: #para evitar que o inimigo encurrale o jogador e crie infinito
                    self.ultimo_respaw = self.timer
                    print("respaw")
                    if self.player.has_mask:
                        quant_enemy = range(0)
                    else:
                        quant_enemy = range(3)
                    for _ in quant_enemy:
                        new_x = enemy.rect.x + random.randint(-50, 50)
                        new_y = enemy.rect.y + random.randint(-50, 50)
                        new_enemy = Influenza(new_x, new_y)
                        enemies.add(new_enemy)
                        
                    enemies.update()
                    all_sprites.add(enemies)
                    all_sprites.draw(self.screen)
                    # 3️⃣ Perder 1 ponto de vida
                    player.life -= 1
                    self.add_message_stack(f"Vida do jogador: {player.life}",20,BLACK)

    def show_message(self, screen, text, duration=2, font_size=24):
        """
        ATENCION
            Essa função não esta sendo utilizada pois foi criado outra mais eficiente com pilha de sequencia.

            Essa função ainda poderá ser utilizada para momentos em que se deseja apresentar informações 
                informações em outros lugares na tela, sem que seja na parte inferior.
            Para isso, ainda falta padronizar como ela será chamada, e definir o controle de tempo que será mostrada
            Uma alternativa é ainda utilizar a pilha de mensagens, porem criar um novo teste, para que se for uma mensagem
                que não será mostrada na parte inferior da tela, ela poderá ser instanciada a qualquer momento 
                e controlada pelo tempo da função que já existe.
                

        Exibe uma mensagem temporária na parte inferior da tela.

        Parâmetros:
        - screen: Superfície do pygame onde o texto será desenhado.
        - text: Texto a ser exibido.
        - duration: Tempo (em segundos) que a mensagem ficará visível.
        - font_size: Tamanho da fonte do texto.
        """
        font = pygame.font.Font(pygame.font.get_default_font, font_size)
        text_surface = font.render(str(text), True, (0, 0, 0))  # Texto preto
        text_rect = text_surface.get_rect()

        # Dimensões do retângulo de fundo
        rect_width = text_rect.width + 20
        rect_height = text_rect.height + 20
        rect_x = (SCREEN_WIDTH - rect_width) // 2  # Centraliza horizontalmente
        rect_y = SCREEN_WIDTH - rect_height - 10  # Posiciona na parte inferior

        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

        # Tempo de exibição
        #start_time = time.time()
        
        # running = True
        # while running:
            #screen.fill((0, 0, 0))  # Limpa a tela (altere para manter o cenário original)

            # Desenha o retângulo branco
        pygame.draw.rect(screen, (255, 255, 255), rect)
            
            # Renderiza o texto dentro do retângulo
        screen.blit(text_surface, (rect_x + 10, rect_y + 10))
            # Verifica se o tempo de exibição terminou
            # if time.time() - start_time > duration:
            #     running = False
        return screen
    
    def make_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        

        rect_width = text_rect.width + 20
        rect_height = text_rect.height + 20
        rect_x = (SCREEN_WIDTH - rect_width) // 2  # Centraliza horizontalmente
        rect_y = SCREEN_WIDTH - rect_height - 200  # Posiciona na parte inferior

        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)

        self.screen.blit(source=text_surf, dest=(rect_x + 10, rect_y + 10))

    def control_message_stack(self):
        #quantos segundos estava quando ele entrou?
        #qual o tempo atual? muda o frame.
        if len(self.message_stack) > -1: 
            for text in self.message_stack:
                if text[5] == -2:
                    continue
                elif text[5] == -1:
                    text[5] = self.timer
                    self.make_text(text[0],text[1],text[2], text[3])
                    break
                elif (self.timer - text[5]) >= text[4]:
                    text[5] = -2
                    continue
                else:
                    self.make_text(text[0],text[1],text[2], text[3])
                    break
        
    def add_message_stack(self, text: str, size: int, color, position : tuple =((SCREEN_WIDTH / 2), 120), time=2 ):
        """_summary_ Para verificar se a mensagem já está na fila.
        Como a atualização é por frame, é necessário ter um controle de mensagens com tempo.
            Se utilizar o timer.start() ele para toda atualização de frame. e não permite o restante do jogo aparecer.
            Esse controle, gerencia as mensagens que vão aparecer, sem pausar o jogo.
        
        Testa se a mensagem já está na pilha e adiciona na lista. 
        """
        exist_not_showed = False
        if len(self.message_stack) > 0: #se tem algum texto na fila faz o teste para não adicionar o mesmo texto todo frame
            for i in self.message_stack:
                if (i[1] == text) and (i[5] == -1):
                    exist_not_showed = True
                    print("Mensagem já existe!")
                    break
                
        if not exist_not_showed:
            self.message_stack.append([size, text, color, position, time, -1])
            

    def control_time(self):
        # cada 1 segundos (~60 frames se FPS=60)
        self.frame += 1
        if self.frame >= (FPS / 2): #se FPS=30 a cada 15 frame da um segundo. (Fiz teste com cronometro)
            self.timer += 1
            self.frame = 0  # Reinicia o contador de frame

    def run(self):
        #Inicia primeiro pelo Menu
        while(True):
            menu = Menu(self.screen)
            opcao = menu.run()
            if opcao == MENU_OPTION[3]:
                menu.about()
            elif opcao == MENU_OPTION[1]:
                menu.fases_game()
            elif opcao == MENU_OPTION[2]:
                menu.config()
            elif opcao == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                break
        
        self.player = Player()
        # Criar grupos de sprites
        all_sprites = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        items = pygame.sprite.Group()
        
        
        # Criar o jogador
        all_sprites.add(self.player)

        # Criar inimigos Influenza
        for i in range(5):  # Número de vírus na tela
            enemy = Influenza(random.randint(100, 700), random.randint(100, 400))
            all_sprites.add(enemy)
            enemies.add(enemy)

        
        # Criar máscara e vacina
        mask = Item(300, 300, self.mask_img)
        vaccine = Item(630, 500, self.vaccine_img)
        all_sprites.add(mask, vaccine)
        items.add(mask, vaccine)

        # Criar inimigos Influenza que protege a vacina
        for i in range(5):  # Número de vírus na tela
            rect = vaccine.get_rect()
            enemy = Influenza(rect[0],rect[1])
            all_sprites.add(enemy)
            enemies.add(enemy)

        #mensagens do início do jogo
        self.add_message_stack("Sua batalha começou!!!", 20, BLACK)
        self.add_message_stack("Sua missão é se vacinar contra a Influenza!", 20, BLACK)
        self.add_message_stack("CUIDADO !!", 20, BLACK, time=1)
        self.add_message_stack("Quando se contaminar", 20, BLACK, time=1)
        self.add_message_stack("O VÍRUS IRÁ SE MULTIPLICAR!",20, BLACK, time=1)
        self.add_message_stack("Se conseguir usar máscara, sua missão será mais fácil.", 20, BLACK)
        self.add_message_stack("Boa Sorte!!!", 20, BLACK)

        while self.running:
            self.screen.blit(source=self.surf, dest=self.rect)
            
            if not self.game_over:

                self.clock.tick(FPS)
                # Movimento do jogador
                keys = pygame.key.get_pressed()
                self.player.update(keys)

                # Atualiza inimigos
                enemies.update()

                # Colisão com máscara
                if pygame.sprite.collide_rect(self.player, mask) and mask.alive():
                    self.player.has_mask = True
                    self.add_message_stack("Agora você tem uma máscara de proteção! Parabéns!", 20, BLACK, ((SCREEN_WIDTH / 2), 120), 2)
                    self.add_message_stack("Você não prolifera mais a doença,", 20, BLACK, ((SCREEN_WIDTH / 2), 120), 1)
                    self.add_message_stack("Mas...", 20, BLACK, ((SCREEN_WIDTH / 2), 120), 1)
                    self.add_message_stack("Você ainda pode se contaminar!", 20, BLACK, ((SCREEN_WIDTH / 2), 120), 2)
                    self.add_message_stack("Procure sua vacina agora mesmo!", 20, BLACK, ((SCREEN_WIDTH / 2), 120), 2)
                    
                    mask.kill()  # Remove a máscara do grupo de sprites após pegar all_sprites.remove(mask) #a mesma coisa que o kill porem remove só do grupo


                # Colisão com vacina
                if pygame.sprite.collide_rect(self.player, vaccine) and vaccine.alive():
                    self.player.vaccinate = True
                    self.add_message_stack("Parabéns!",20, BLACK, time=1)
                    self.add_message_stack("Você se vacinou! E agora, muita coisa mudou!",20, BLACK,time=3)
                    self.add_message_stack("Você não sente mais o efeito da Gripe!!",20, BLACK)
                    self.add_message_stack("Agora você está imunizado contra a influenza!",20, BLACK,time=3)
                    self.add_message_stack("FAÇA O TESTE! Vá até a Influenza!",20, BLACK, time=2)
                    self.add_message_stack("Você VENCEU a fase!", 20, BLACK, time=5)
                    self.add_message_stack("PRESSIONE ENTER PARA FINALIZAR", 20, BLACK, time=120)
                    vaccine.kill()

                
                # Colisão com inimigos
                if pygame.sprite.spritecollide(self.player, enemies, False) and not self.player.vaccinate:
                    self.add_message_stack("Agora está Gripado!", 20, BLACK)
                    # Funcão de repulsão e criar novos inimigos
                    self.colisao_enemy(enemies, self.player, all_sprites)
                    if self.player.life < 0:
                        self.running = False  # Fecha o jogo

                # Desenhar elementos na tela
                #self.screen.fill(WHITE)
                all_sprites.draw(self.screen)
                pygame.display.flip()
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        if keys[pygame.K_RETURN] and self.player.vaccinate:
            pygame.quit()
            quit()
        self.control_time() #contador geral do jogo
        self.control_message_stack()

    def draw(self):
        #self.screen.fill((0, 0, 0))
        #self.player.draw(self.screen)
        pygame.display.flip()

