# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:53 2015

@author: vitor_000
"""

import pygame

pygame.init()
pygame.display.set_caption('Davitors') #Nome do jogo a ser decidido

framespersecond = pygame.time.Clock()

black = (0,0,0)
largura_da_tela = 800 #eixox
altura_da_tela = 600
velocidade_fundo = 5
posição_inicial_fundo = -600

DisplayDoJogo = pygame.display.set_mode((largura_da_tela,altura_da_tela))
    
def função_fundo():
    Imagem_Fundo = pygame.image.load('8bitsroad.png')
    Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,altura_da_tela))
    DisplayDoJogo.blit(Imagem_Fundo,(0,0))
    
    

função_fundo()

Não_Rodar_Jogo = False

while not Não_Rodar_Jogo:

    for tecla in pygame.event.get():
        if tecla.type == pygame.QUIT:
            Não_Rodar_Jogo = True
    

    pygame.display.update()
    framespersecond.tick(60)


pygame.quit()
quit()