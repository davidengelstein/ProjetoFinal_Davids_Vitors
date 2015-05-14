# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:53 2015

@author: vitor_000
"""

import pygame
import random

pygame.init()
pygame.display.set_caption('Davitors') #Nome do jogo a ser decidido

framespersecond = pygame.time.Clock()

black = (0,0,0)
largura_da_tela = 800 #eixox
altura_da_tela = 600

fps = 60

imgcarro = pygame.image.load('car8bits2.png')
lourenco = pygame.image.load('lor.png')
miranda = pygame.image.load('mir.png')
orfali = pygame.image.load('orf.png')


def fundo(x,y):
    DisplayDoJogo.blit(Imagem_Fundo,(x,y))
    
    
def imagem_carro(a,b):
    DisplayDoJogo.blit(imgcarro,(a,b))
    

def lourenco1(r,s):
    DisplayDoJogo.blit(lourenco,(r,s))


DisplayDoJogo = pygame.display.set_mode((largura_da_tela,altura_da_tela))
    

Imagem_Fundo = pygame.image.load('fundo.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))


Não_Rodar_Jogo = False



def loop_jogo():
    velocidade_fundo = 5
    posição_inicial_fundo_y = -600
    posição_inicial_fundo_x = 0
    
    posição_lourencoX = random.choice([210,375,540])
    posição_lourencoY = random.randrange(-600,-100)
    velocidade_lourenco = velocidade_fundo
        
    car_positiony = 475
    car_positionx = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165
    
    Não_Rodar_Jogo = False

    while not Não_Rodar_Jogo:
    
        for tecla in pygame.event.get():
            
            if tecla.type == pygame.QUIT:
                Não_Rodar_Jogo = True
            
            if tecla.type == pygame.KEYDOWN:
                
                if car_positionx == 375 and tecla.key == pygame.K_LEFT:
                    car_positionx = 210
                    
                elif car_positionx == 210 and tecla.key == pygame.K_RIGHT:
                    car_positionx = 375
                    
                elif car_positionx == 375 and tecla.key == pygame.K_RIGHT:
                    car_positionx = 540
                    
                elif car_positionx == 540 and tecla.key == pygame.K_LEFT:
                    car_positionx = 375
                    
    #        if tecla.type == pygame.KEYUP:
    #            
    #            if tecla.key == pygame.K_LEFT or tecla.key == pygame.K_RIGHT:
    #                car_positionx = 375
        
        
        
        fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)    
        posição_inicial_fundo_y += velocidade_fundo    
        
        
        
        if posição_inicial_fundo_y == 0:
            posição_inicial_fundo_y = -600
        
        if posição_lourencoY > altura_da_tela:
            posição_lourencoY = 0 - random.randrange(300,900)
            posição_lourencoX = random.choice([210,375,540])
          
        imagem_carro(car_positionx,car_positiony)
        lourenco1(posição_lourencoX,posição_lourencoY)
        
        pygame.display.update()
        framespersecond.tick(fps)

loop_jogo()
pygame.quit()
quit()