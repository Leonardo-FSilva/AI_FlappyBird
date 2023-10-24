import pygame
import os
import random


TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('resource','pipe.png')))
IMAGEM_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('resource','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('resource','bg.png')))
IMAGEMS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('resource','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('resource','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('resource','bird3.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGEMS_PASSARO
    
    # Bird animation
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, X:int, Y:int) -> None:
        self.x = X
        self.y = Y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura+50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
        

class Cano:
    pass

class Chao:
    pass

