import pygame
import random

# Configurações iniciais
pygame.init()
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong do SUPREMO SENHOR LEOZÃO")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Posições iniciais das raquetes e bola
raquete1_x, raquete1_y = 20, altura // 2
raquete2_x, raquete2_y = largura - 40, altura // 2
bola_x, bola_y = largura // 2, altura // 2
bola_vel_x, bola_vel_y = 0.5 * random.choice((1, -1)), 0.5 * random.choice((1, -1))

# Função para desenhar raquetes e bola
def desenhar_elementos():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (raquete1_x, raquete1_y - 30, 10, 180))
    pygame.draw.rect(tela, branco, (raquete2_x, raquete2_y - 30, 10, 180))
    pygame.draw.ellipse(tela, branco, (bola_x - 15, bola_y - 15, 30, 30))

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimentação das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1_y > 30:
        raquete1_y -= 1
    if teclas[pygame.K_s] and raquete1_y < altura - 30:
        raquete1_y += 1
    if teclas[pygame.K_UP] and raquete2_y > 30:
        raquete2_y -= 1
    if teclas[pygame.K_DOWN] and raquete2_y < altura - 30:
        raquete2_y += 1

    # Movimentação da bola
    bola_x += bola_vel_x
    bola_y += bola_vel_y

    # Colisões com as bordas
    if bola_y < 15 or bola_y > altura - 15:
        bola_vel_y = -bola_vel_y

    # Colisões com raquetes
    if 20 < bola_x < 30 and raquete1_y - 30 < bola_y < raquete1_y + 30:
        bola_vel_x = -bola_vel_x
    if largura - 30 < bola_x < largura - 20 and raquete2_y - 30 < bola_y < raquete2_y + 30:
        bola_vel_x = -bola_vel_x

    # Verificação de pontos
    if bola_x < 0:
        # Jogador da direita ganha um ponto
        bola_x, bola_y = largura // 2, altura // 2
        bola_vel_x, bola_vel_y = 0.5 * random.choice((1, -1)), 0.5 * random.choice((1, -1))

    if bola_x > largura:
        # Jogador da esquerda ganha um ponto
        bola_x, bola_y = largura // 2, altura // 2
        bola_vel_x, bola_vel_y = 0.5 * random.choice((1, -1)), 0.5 * random.choice((1, -1))

    # Desenha os elementos
    desenhar_elementos()

    pygame.display.update()
