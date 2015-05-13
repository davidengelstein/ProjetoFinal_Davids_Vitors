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

fps = 60

velocidade_fundo = 5
posição_inicial_fundo_y = -600
posição_inicial_fundo_x = 0

car_positiony = 475
car_positionx = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165

imgcarro = pygame.image.load('car8bits2.png')


def fundo(x,y):
    DisplayDoJogo.blit(Imagem_Fundo,(x,y))
    
    
def imagem_carro(a,b):
    DisplayDoJogo.blit(imgcarro,(a,b))

    

DisplayDoJogo = pygame.display.set_mode((largura_da_tela,altura_da_tela))
    

Imagem_Fundo = pygame.image.load('fundo.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))


Não_Rodar_Jogo = False




while not Não_Rodar_Jogo:

    for tecla in pygame.event.get():
        
        if tecla.type == pygame.QUIT:
            Não_Rodar_Jogo = True
        
        if tecla.type == pygame.KEYDOWN:
            
            if tecla.type == pygame.K_LEFT:
                car_positionx = 200  
 
            elif tecla.type == pygame.K_RIGHT:
                car_positionx = 540
        
        if tecla.type == pygame.KEYUP:
            
            if tecla.type == pygame.K_LEFT or pygame.K_RIGHT:
                car_positionx = 375
    
    
    print(tecla)
    fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)    
    posição_inicial_fundo_y += velocidade_fundo    
    
    
    
    if posição_inicial_fundo_y == 0:
        posição_inicial_fundo_y = -600
        
    
    imagem_carro(car_positionx,car_positiony)
    
    
    pygame.display.update()
    framespersecond.tick(fps)


pygame.quit()
quit()