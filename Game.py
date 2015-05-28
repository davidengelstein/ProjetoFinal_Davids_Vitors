# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:53 2015
@author: vitor_000,vitor_kitahara
"""

import pygame
import random
import time
from random import choice

pygame.init()
pygame.display.set_caption('Teachers Game Race') #Nome do jogo a ser decidido

framespersecond = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

blackb = (200,200,200)

yellow = (255,242,0)


largura_da_tela = 800 #eixox
altura_da_tela = 600

gameDisplay = pygame.display.set_mode((largura_da_tela,altura_da_tela))

fps = 1000

imgcarro = pygame.image.load('car8bits2.png')
lourenco = pygame.image.load('lor.png')
miranda = pygame.image.load('mir.png')
orfali = pygame.image.load('orf.png')
fred = pygame.image.load('fred1.png')
haddad = pygame.image.load('had1.png')
heloisa = pygame.image.load('helo2.png')
vinicius = pygame.image.load('vinicius1.png')
bala = pygame.image.load("bala.png")
cubo = pygame.image.load("caixinha.png")


moedass = pygame.image.load('moeda.png')

musica = pygame.mixer.music.load('uptown8bits.wav')
#faustao = pygame.mixer.Sound('faustao.wav')


Imagem_Fundo = pygame.image.load('8bitsRoad.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))

def tiros(tirosx,tirosy):
    gameDisplay.blit(bala,(tirosx,tirosy))

    

def cubos_contador(cont):
    font = pygame.font.SysFont(None, 40)
    text = font.render("tiros: "+str(cont), True, black)
    gameDisplay.blit(text,(0,28))

def func_cubos(cubosx,cubosy):
    gameDisplay.blit(cubo,(cubosx,cubosy))

def dinheiro(contar2):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Moedas: " + str(contar2),True,yellow)
    DisplayDoJogo.blit(text,(0,50))


def desvio(contar):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(contar),True,green)
    DisplayDoJogo.blit(text,(0,0))
    
def text_objects(text, font): #Não entendi muito bem essa função
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect() 

def mensagem(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((largura_da_tela/2),(altura_da_tela/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    loop_jogo()

def bater():
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(faustao)
    mensagem('ERROOOOU, SEU LIXO!!!')
    Score = 0


def moeda(x,y):
    DisplayDoJogo.blit(moedass,(x,y))

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
    Imagem_Fundo = pygame.image.load('fundo.png')   
    Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))
    def fundo(x,y):
        DisplayDoJogo.blit(Imagem_Fundo,(x,y))
    

    pygame.mixer.music.play()
        
    velocidade_fundo = 5

    

    posição_inicial_fundo_y = -600
    posição_inicial_fundo_x = 0

    moedaX = random.choice([210,375,540])
    moedaY = -600
    moedaH = 35
    moedaW = 46
    velocidade_moeda = velocidade_fundo
    
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
    
    prof_largura = 60
    prof_altura = 60
    
    car_positionY = 475
    car_positionX = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165
    carX = 57
    carY = 106
    Score = 0
    Moedas = 0
    
    cubosx = choice([275,330,525])
    cubosy = 0
    cubos_speed = velocidade_fundo
    cubos_compr=100
    cubos_larg=120
    
    tirosx = car_positionX
    tirosy = car_positionY
    tiros_speed= 1
    tiros_change = 0
    tiros_width = 10
    tiros_compr = 100
    
    contador = 0
    
    Não_Rodar_Jogo = False

    while not Não_Rodar_Jogo:
    
        for tecla in pygame.event.get():
            
            if tecla.type == pygame.QUIT:
                Não_Rodar_Jogo = True
            
            if tecla.type == pygame.KEYDOWN:
                
                if car_positionX == 375 and tecla.key == pygame.K_LEFT:
                    car_positionX = 210
                    if tirosy == car_positionY:                    
                        tirosx = 195
                    
                        
                elif car_positionX == 210 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 375
                    if tirosy == car_positionY:
                        tirosx = 350
                elif car_positionX == 375 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 540
                    if tirosy == car_positionY:
                        tirosx=560
                elif car_positionX == 540 and tecla.key == pygame.K_LEFT:
                    car_positionX = 375
                    if tirosy == car_positionY:
                        tirosx = 350

        fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)    
        posição_inicial_fundo_y += velocidade_fundo
        func_cubos(cubosx, cubosy)
        cubosy += cubos_speed
        desvio(Score)

        if car_positionX > 637 - carX or car_positionX < 157:
            bater()
                            
        if car_positionY > altura_da_tela - carY or car_positionY < 0:
            bater()
                
        if posição_inicial_fundo_y == 0:
            posição_inicial_fundo_y = -600
        
        if posição_lourencoY > altura_da_tela:
            posição_lourencoY = 0 - random.randrange(3500,4000)
            posição_lourencoX = random.choice([210,375,540])
            Score += 1
            
        if posição_mirandaY > altura_da_tela:
            posição_mirandaY = 0 - random.randrange(100,3000)
            posição_mirandaX = random.choice([210,375,540])
            Score += 1
        
        if posição_orfaliY > altura_da_tela:
            posição_orfaliY = 0 - random.randrange(6000,7000)
            posição_orfaliX = random.choice([210,375,540])
            Score += 1
            
        if posição_fredY > altura_da_tela:
            posição_fredY = 0 - random.randrange(100,2500)
            posição_fredX = random.choice([210,375,540])
            Score += 1
        
        if posição_haddadY > altura_da_tela:
            posição_haddadY = 0 - random.randrange(5000,10000)
            posição_haddadX = random.choice([210,375,540])
            Score += 1
            
        if posição_viniciusY > altura_da_tela:
            posição_viniciusY = 0 - random.randrange(2000,5000)
            posição_viniciusX = random.choice([210,375,540])
            Score += 1
        
        if posição_heloisaY > altura_da_tela:
            posição_heloisaY = 0 - random.randrange(100,2500)
            posição_heloisaX = random.choice([210,375,540])
            Score += 1
        if car_positionY < cubosy + cubos_compr:
            if car_positionX > cubosx and car_positionX < cubosx + cubos_larg or car_positionX+carX > cubosx and car_positionX + carX < cubosx + cubos_larg:
            
                cubosy = (altura_da_tela-3000)
                cubosx = choice([270,360,540])
                contador+=1
                
            else:
                if cubosy > 800:
                    cubosy = (altura_da_tela-3000)
                    cubosx = choice([230,360,540])
                    
        imagem_carro(car_positionX,car_positionY)
        cubos_contador(contador)
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

        #moeda(moedaX,moedaY)
        moedaY += velocidade_moeda
        
        imagem_carro(car_positionX,car_positionY)

        
        
        
                
        
        if car_positionY < posição_lourencoY + prof_altura and car_positionY + carY >= posição_lourencoY + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_lourencoX and car_positionX < posição_lourencoX + prof_largura or car_positionX+carX > posição_lourencoX and car_positionX + carX < posição_lourencoX+prof_largura:
                  bater()
            
        if car_positionY  < posição_mirandaY + prof_altura and car_positionY + carY >= posição_mirandaY + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_mirandaX and car_positionX < posição_mirandaX + prof_largura or car_positionX+carX > posição_mirandaX and car_positionX + carX < posição_mirandaX+prof_largura:
                  bater()

        if car_positionY  < posição_orfaliY + prof_altura and car_positionY + carY >= posição_orfaliY + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_orfaliX and car_positionX < posição_orfaliX + prof_largura or car_positionX+carX > posição_orfaliX and car_positionX + carX < posição_orfaliX+prof_largura:
                  bater()
                  
        if car_positionY  < posição_fredY + prof_altura and car_positionY + carY >= posição_fredY + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_fredX and car_positionX < posição_fredX + prof_largura or car_positionX+carX > posição_fredX and car_positionX + carX < posição_fredX+prof_largura:
                  bater()

        if car_positionY  < posição_haddadY + prof_altura: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_haddadX and car_positionX < posição_haddadX + prof_largura or car_positionX+carX > posição_haddadX and car_positionX + carX < posição_haddadX+prof_largura:
                  Score += 10
                  posição_haddadY = -1500
                  posição_haddadX = random.choice([210,375,540])
                  
        if car_positionY < posição_viniciusY + prof_altura: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_viniciusX and car_positionX < posição_viniciusX + prof_largura or car_positionX+carX > posição_viniciusX and car_positionX + carX < posição_viniciusX+prof_largura:
                  Score += 5
                  posição_viniciusY = -1500
                  posição_viniciusX = random.choice([210,375,540])

        if car_positionY < posição_heloisaY + prof_altura and car_positionY + carY >= posição_heloisaY + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
              if car_positionX > posição_heloisaX and car_positionX < posição_heloisaX + prof_largura or car_positionX+carX > posição_heloisaX and car_positionX + carX < posição_heloisaX+prof_largura:
                  bater()     
        
        
        
        if contador > 0:    
            if tecla.type == pygame.QUIT:
                pygame.quit()
                quit()        
            
            if tecla.type == pygame.KEYDOWN:
                if tecla.key == pygame.K_SPACE:
                    pass
                    
                    #tiros(tirosx,tirosy)

            if tecla.type == pygame.KEYUP:
                if tecla.key == pygame.K_SPACE:
                    tiros(tirosx,tirosy)
                    tiros_speed = 10
                    tirosx = car_positionX
                    
                        
#                    for i in range(1,600):
#                        tiros_speed+=0.000002
                    
                    tirosy -= tiros_speed
                    
                    if tirosy<0:
                        if contador>0:
                            tirosy=car_positionY
                            contador-=1
                            
                                        
        if tirosy  < posição_mirandaY + prof_altura and tirosy + tiros_width >= posição_mirandaY: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
            if tirosx > posição_mirandaX and tirosx < posição_mirandaX + prof_largura or tirosx+tiros_width > posição_mirandaX and tirosx + tiros_width < posição_mirandaX+prof_largura:
                posição_mirandaY = -1000
                posição_mirandaX = random.choice([210,375,540])
        
        if tirosy  < posição_lourencoY + prof_altura and tirosy + tiros_width >= posição_lourencoY: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
            if tirosx > posição_lourencoX and tirosx < posição_lourencoX + prof_largura or tirosx+tiros_width > posição_lourencoX and tirosx + tiros_width < posição_lourencoX+prof_largura:
                posição_lourencoY = -1000
                posição_lourencoX = random.choice([210,375,540])
                
        if tirosy  < posição_orfaliY + prof_altura and tirosy + tiros_width >= posição_orfaliY: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
            if tirosx > posição_orfaliX and tirosx < posição_orfaliX + prof_largura or tirosx+tiros_width > posição_orfaliX and tirosx + tiros_width < posição_orfaliX+prof_largura:
                posição_orfaliY = -1000
                posição_orfaliX = random.choice([210,375,540])
                
        if tirosy  < posição_fredY + prof_altura and tirosy + tiros_width >= posição_fredY: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
            if tirosx > posição_fredX and tirosx < posição_fredX + prof_largura or tirosx+tiros_width > posição_fredX and tirosx + tiros_width < posição_fredX+prof_largura:
                posição_fredY = -1000
                posição_fredX = random.choice([210,375,540])
                
                
                
        if tirosy  < posição_heloisaY + prof_altura and tirosy + tiros_width >= posição_heloisaY: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
            if tirosx > posição_heloisaX and tirosx < posição_heloisaX + prof_largura or tirosx+tiros_width > posição_heloisaX and tirosx + tiros_width < posição_heloisaX+prof_largura:
                posição_heloisaY = -1000
                posição_heloisaX = random.choice([210,375,540])
        
        #pygame.mixer.Sound.stop(faustao)
        pygame.display.update()
        framespersecond.tick(fps)
def intinicial():
    
    interface = pygame.image.load('Fundo1.png')    
    interface = pygame.transform.scale(interface,(largura_da_tela,altura_da_tela))
    gameDisplay.blit(interface,(0,0))
    
                
    def button(msg,msg1,msg2,x,y,w,h,ic,ac):
        while True:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
    #            print(mouse)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()
            
            if x+w > mouse[0] > x and y + h > mouse[1] > y:   #310,400,180,40 (x,y,w,h)
                pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
                if click[0] == 1:
                    loop_jogo()
                    
            else:
                pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
                
            if x+w > mouse[0] > x and y+60+h > mouse[1] > y+60:
                pygame.draw.rect(gameDisplay, ac, (x,y+60,w,h))
            else:
                pygame.draw.rect(gameDisplay, ic, (x,y+60,w,h))
                
            if x + w > mouse[0] > x and y+120+h > mouse[1] > y+120:
                pygame.draw.rect(gameDisplay, ac, (x,y+120,w,h))
                if click[0] == 1:
                    pygame.quit()
                    quit()
                    
            else:
                pygame.draw.rect(gameDisplay, ic, (x,y+120,w,h))
                
                            
            font = pygame.font.SysFont(None, 40)
            text = font.render(msg,True,white)
            gameDisplay.blit(text,(363,410))
        
            font = pygame.font.SysFont(None, 40)
            text = font.render(msg1,True,white)
            gameDisplay.blit(text,(333,470))
        
            font = pygame.font.SysFont(None, 40)
            text = font.render(msg2,True,white)
            gameDisplay.blit(text,(363,530))
            
            
    button('PLAY','RANKING','QUIT',310,400,180,40,black,blackb)                        
intinicial()

loop_jogo()
pygame.quit()

quit()

