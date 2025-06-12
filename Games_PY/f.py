import pygame
import random

pygame.init()
pygame.mixer.init()

# Tela e nome
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fuja dos Quadrados!!!")

# Set de cores
ROXO = (128, 0, 128)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Jogador(quadrado)
player = pygame.Rect(50, HEIGHT // 2, 50, 50)

# Obstaculos
obstaculos = []

# Velocidade
vel_jogador = 5
vel_obstaculo = 5

# Relógio
clock = pygame.time.Clock()

# Set de fonte
fonte = pygame.font.SysFont("arial", 30)

# Som de colisão, quando bater é para sair um som
som_colisao = pygame.mixer.Sound("colisao.wav")

# Função def de criação de obstáculo
def criar_obstaculo():
    x = WIDTH
    y = random.randint(0, HEIGHT - 50)
    return pygame.Rect(x, y, 50, 50)

# Temporizador de obstáculos
ADD_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_EVENT, 1000)

# Função principal do jogo
def jogar():
    pontos = 0
    obstaculos = []
    player.y = HEIGHT // 2
    vel_obs = vel_obstaculo
    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == ADD_EVENT:
                obstaculos.append(criar_obstaculo())

        # Teclas up e down do teclado, seta cim e baixo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= vel_jogador
        if keys[pygame.K_DOWN] and player.y < HEIGHT - player.height:
            player.y += vel_jogador

        # Movimento dos obstáculos, vir direita p/ esquerda
        for obs in obstaculos:
            obs.x -= vel_obs

        # Remover obstáculos fora da tela
        obstaculos = [obs for obs in obstaculos if obs.x > -50]

        # Verificar colisão(bugado)
        perdeu = any(player.colliderect(obs) for obs in obstaculos)

        # Desenhar
        screen.fill(ROXO)
        pygame.draw.rect(screen, VERDE if not perdeu else VERMELHO, player)
        for obs in obstaculos:
            pygame.draw.rect(screen, BRANCO, obs)

        # Pontuação
        pontos += 1
        texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        screen.blit(texto, (10, 10))

        pygame.display.flip()

        if perdeu:
            som_colisao.play()
            texto_fim = fonte.render(f"GAME OVER BB, TENTE NOVAMENTE! Pontos: {pontos}", True, BRANCO)
            screen.blit(texto_fim, (WIDTH//2 - 150, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(3000)
            rodando = False

        # Aumenta dificuldade ao longo do tempo(EXPERIMENTAL, funcionou)
        if pontos % 300 == 0:
            vel_obs += 1

        clock.tick(60)

# Loop infinito do jogo
while True:
    jogar()