# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:53 2015
@author: vitor_000,vitor_kitahara
"""

import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Davitors') #Nome do jogo a ser decidido

framespersecond = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

largura_da_tela = 800 #eixox
altura_da_tela = 600

fps = 60

imgcarro = pygame.image.load('car8bits2.png')
lourenco = pygame.image.load('lor.png')
miranda = pygame.image.load('mir.png')
orfali = pygame.image.load('orf.png')
fred = pygame.image.load('fred1.png')
haddad = pygame.image.load('had1.png')
heloisa = pygame.image.load('helo2.png')
vinicius = pygame.image.load('vinicius1.png')
musica = pygame.mixer.music.load('uptown8bits.wav')
faustao = pygame.mixer.Sound('Faustao.wav')
Imagem_Fundo = pygame.image.load('8bitsRoad.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))

def desvio(contar):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(contar),True,green)
    DisplayDoJogo.blit(text,(0,0))

def mensagem(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText, red)
    TextRect.center = ((screenX/2),(screenY/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    loop_jogo()

def bater():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(faustao)
    mensagem('ERROOOOU!!!')

def fundo(x,y):
    DisplayDoJogo.blit(Imagem_Fundo,(x,y))
        
def imagem_carro(a,b):
    DisplayDoJogo.blit(imgcarro,(a,b))
    
def lourenco1(r,s):
    DisplayDoJogo.blit(lourenco,(r,s))

def miranda1(r,s):
    DisplayDoJogo.blit(miranda,(r,s))
    
def orfali1(r,s):
    DisplayDoJogo.blit(orfali,(r,s))
    
def fred1(r,s):
    DisplayDoJogo.blit(fred,(r,s))
    
def haddad1(r,s):
    DisplayDoJogo.blit(haddad,(r,s))

def vinicius1(r,s):
    DisplayDoJogo.blit(vinicius,(r,s))
    
def heloisa1(r,s):
    DisplayDoJogo.blit(heloisa,(r,s))
    
    
DisplayDoJogo = pygame.display.set_mode((largura_da_tela,altura_da_tela))
    

Não_Rodar_Jogo = False



def loop_jogo():
    pygame.mixer.music.play()
    
    velocidade_fundo = 5
    posição_inicial_fundo_y = -600
    posição_inicial_fundo_x = 0
    
    posição_lourencoX = random.choice([210,375,540])
    posição_lourencoY = random.randrange(-2000,0)
    velocidade_lourenco = velocidade_fundo
    
    posição_mirandaX = random.choice([210,375,540])
    posição_mirandaY = random.randrange(-3000,0)
    velocidade_miranda = velocidade_fundo
    
    posição_orfaliX = random.choice([210,375,540])
    posição_orfaliY = random.randrange(-2000,0)
    velocidade_orfali = velocidade_fundo
    
    posição_fredX = random.choice([210,375,540])
    posição_fredY = random.randrange(-2500,0)
    velocidade_fred = velocidade_fundo
    
    posição_haddadX = random.choice([210,375,540])
    posição_haddadY = random.randrange(-10000,0)
    velocidade_haddad = velocidade_fundo
    
    posição_viniciusX = random.choice([210,375,540])
    posição_viniciusY = random.randrange(-5000,0)
    velocidade_vinicius = velocidade_fundo
    
    posição_heloisaX = random.choice([210,375,540])
    posição_heloisaY = random.randrange(-2500,0)
    velocidade_heloisa = velocidade_fundo
    
    car_positionY = 475
    car_positionX = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165
    carX = 57
    carY = 106
    Score = 0
    
    Não_Rodar_Jogo = False

    while not Não_Rodar_Jogo:
    
        for tecla in pygame.event.get():
            
            if tecla.type == pygame.QUIT:
                Não_Rodar_Jogo = True
            
            if tecla.type == pygame.KEYDOWN:
                
                if car_positionX == 375 and tecla.key == pygame.K_LEFT:
                    car_positionX = 210
                    
                elif car_positionX == 210 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 375
                    
                elif car_positionX == 375 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 540
                    
                elif car_positionX == 540 and tecla.key == pygame.K_LEFT:
                    car_positionX = 375
                    

        fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)    
        posição_inicial_fundo_y += velocidade_fundo

        desvio(Score)

        if car_positionX > 637 - carX or car_positionX < 157:
            bater()
                            
        if car_positionY > altura_da_tela - carY or car_positionY < 0:
            bater()
                
        if posição_inicial_fundo_y == 0:
            posição_inicial_fundo_y = -600
        
        if posição_lourencoY > altura_da_tela:
            posição_lourencoY = 0 - random.randrange(100,4000)
            posição_lourencoX = random.choice([210,375,540])
            Score += 1
            
        if posição_mirandaY > altura_da_tela:
            posição_mirandaY = 0 - random.randrange(100,3000)
            posição_mirandaX = random.choice([210,375,540])
            Score += 1
        
        if posição_orfaliY > altura_da_tela:
            posição_orfaliY = 0 - random.randrange(100,1000)
            posição_orfaliX = random.choice([210,375,540])
            Score += 1
            
        if posição_fredY > altura_da_tela:
            posição_fredY = 0 - random.randrange(100,2500)
            posição_fredX = random.choice([210,375,540])
            Score += 1
        
        if posição_haddadY > altura_da_tela:
            posição_haddadY = 0 - random.randrange(100,10000)
            posição_haddadX = random.choice([210,375,540])
            Score += 1
            
        if posição_viniciusY > altura_da_tela:
            posição_viniciusY = 0 - random.randrange(100,5000)
            posição_viniciusX = random.choice([210,375,540])
            Score += 1
        
        if posição_heloisaY > altura_da_tela:
            posição_heloisaY = 0 - random.randrange(100,2500)
            posição_heloisaX = random.choice([210,375,540])
            Score += 1
            
        imagem_carro(car_positionX,car_positionY)
        
        lourenco1(posição_lourencoX,posição_lourencoY)
        miranda1(posição_mirandaX,posição_mirandaY)
        orfali1(posição_orfaliX,posição_orfaliY)
        fred1(posição_fredX,posição_fredY)
        haddad1(posição_haddadX,posição_haddadY)
        vinicius1(posição_viniciusX,posição_viniciusY)
        heloisa1(posição_heloisaX,posição_heloisaY)
        
        posição_lourencoY += velocidade_lourenco        
        posição_mirandaY += velocidade_miranda
        posição_orfaliY += velocidade_orfali
        posição_fredY += velocidade_fred           
        posição_haddadY += velocidade_haddad   
        posição_viniciusY += velocidade_vinicius
        posição_heloisaY += velocidade_heloisa

        
        
        pygame.display.update()
        framespersecond.tick(fps)

loop_jogo()
pygame.quit()
quit()

