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
fred5 = pygame.image.load('fred1.png')
haddad = pygame.image.load('had1.png')
heloisa = pygame.image.load('helo2.png')
vinicius = pygame.image.load('vinicius1.png')
bala = pygame.image.load("bala.png")
cubo = pygame.image.load("caixinha.png")

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

def desvio(contar):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(contar),True,green)
    DisplayDoJogo.blit(text,(0,0))
    
def text_objects(text, font): #Não entendi muito bem essa função
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect() 

def mensagem(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((largura_da_tela/2),(altura_da_tela/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    loop_jogo()

def bater():
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(faustao)
    mensagem('ERROOOOU!!!')
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
    DisplayDoJogo.blit(fred5,(r,s))
    
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

    prof_largura = 60
    prof_altura = 60
    
    car_positionY = 475
    car_positionX = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165
    carX = 57
    carY = 106

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
    
    class Jogador:
        Score = 0
    
    class personagens:
        def __init__(self,titulo1,titulo2):
            self.titulo1 = titulo1
            self.titulo2 = titulo2
            
            
        def posiniper(self,random1,random2):
            self.titulo1 = random.choice([210,375,540])
            self.titulo2 = random.randrange(random1,random2)

        def posper2(self,random3,random4):
            if self.titulo2 > altura_da_tela:
                self.titulo2 = 0 - random.randrange(random3,random4)
                self.titulo1 = random.choice([210,375,540])
                
                Jogador.Score += 1
            
        def crash(self):
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    bater()

        def crash2 (self,value):
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    
                    Jogador.Score += value

    lor = personagens('posição_lourençoX','posição_lourençoY')
    mir = personagens('posição_mirandaX','posição_mirandaY')
    orf = personagens('posição_orfaliX','posição_orfaliY')
    fred = personagens('posição_fredX','posição_fredY')
    had = personagens('posição_haddadX','posição_haddadY')
    vin = personagens('posição_viniciusX','posição_viniciusY')
    hel = personagens('posição_heloisaX','posição_heloisaY')

    lor.posiniper(-2000,0)
    mir.posiniper(-3000,0)
    orf.posiniper(-2000,0)
    fred.posiniper(-2500,0)
    had.posiniper(-10000,0)
    vin.posiniper(-5000,0)
    hel.posiniper(-2500,0)
    
    Não_Rodar_Jogo = False

    while not Não_Rodar_Jogo:
        
        for tecla in pygame.event.get():
            
            if tecla.type == pygame.QUIT:
                Não_Rodar_Jogo = True
            
            if tecla.type == pygame.KEYDOWN:

                
                if car_positionX == 375 and tecla.key == pygame.K_LEFT:
                    car_positionX = 210
                    if tirosy == car_positionY:                    
                        tirosx = 210
                    
                elif car_positionX == 210 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 375
                    if tirosy == car_positionY:
                        tirosx = 375
                    
                elif car_positionX == 375 and tecla.key == pygame.K_RIGHT:
                    car_positionX = 540
                    if tirosy == car_positionY:
                        tirosx=540
                    
                elif car_positionX == 540 and tecla.key == pygame.K_LEFT:
                    car_positionX = 375
                    if tirosy == car_positionY:
                        tirosx = 375
            
                if tecla.key == pygame.K_SPACE:
                    pass
                
                if contador > 0:    
                    
                    if tecla.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            if tecla.type == pygame.KEYUP:
                if tecla.key == pygame.K_SPACE:
                    tiros(tirosx,tirosy)
                    tiros_speed = 10
                    tirosx = car_positionX

                    tirosy -= tiros_speed
                        
                    if tirosy<0:
                        if contador>0:
                            tirosy=car_positionY
                            contador-=1

                if tirosy  < mir.titulo2 + prof_altura and tirosy + tiros_width >= mir.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if tirosx > mir.titulo1 and tirosx < mir.titulo1 + prof_largura or tirosx+tiros_width > mir.titulo1 and tirosx + tiros_width < mir.titulo1+prof_largura:
                        mir.titulo2 = -1000
                        mir.titulo1 = random.choice([210,375,540])
            
                if tirosy  < lor.titulo2 + prof_altura and tirosy + tiros_width >= lor.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if tirosx > lor.titulo1 and tirosx < lor.titulo1 + prof_largura or tirosx+tiros_width > lor.titulo1 and tirosx + tiros_width < lor.titulo1+prof_largura:
                        lor.titulo2 = -1000
                        lor.titulo1 = random.choice([210,375,540])
                    
                if tirosy  < orf.titulo2 + prof_altura and tirosy + tiros_width >= orf.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if tirosx > orf.titulo1 and tirosx < orf.titulo1 + prof_largura or tirosx+tiros_width > orf.titulo1 and tirosx + tiros_width < orf.titulo1+prof_largura:
                        orf.titulo2 = -1000
                        orf.titulo1 = random.choice([210,375,540])
                    
                if tirosy  < fred.titulo2 + prof_altura and tirosy + tiros_width >= fred.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if tirosx > fred.titulo1 and tirosx < fred.titulo1 + prof_largura or tirosx+tiros_width > fred.titulo1 and tirosx + tiros_width < fred.titulo1+prof_largura:
                        fred.titulo2 = -1000
                        fred.titulo1 = random.choice([210,375,540])

                if tirosy  < hel.titulo2 + prof_altura and tirosy + tiros_width >= hel.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if tirosx > hel.titulo1 and tirosx < hel.titulo1 + prof_largura or tirosx+tiros_width > hel.titulo1 and tirosx + tiros_width < hel.titulo1+prof_largura:
                        hel.titulo2 = -1000
                        hel.titulo1 = random.choice([210,375,540])


        fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)    
        posição_inicial_fundo_y += velocidade_fundo
        

        func_cubos(cubosx, cubosy)
        cubosy += cubos_speed


        desvio(Jogador.Score)

        if car_positionX > 637 - carX or car_positionX < 157:
            bater()
                            
        if car_positionY > altura_da_tela - carY or car_positionY < 0:
            bater()
                
        if posição_inicial_fundo_y == 0:
            posição_inicial_fundo_y = -600

        lor.posper2(3500,4000)
        mir.posper2(100,3000)
        orf.posper2(6000,7000)
        fred.posper2(100,2500)
        had.posper2(5000,10000)
        vin.posper2(2000,5000)
        hel.posper2(100,2500)

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
        lourenco1(lor .titulo1,lor.titulo2)
        miranda1(mir.titulo1,mir.titulo2)
        orfali1(orf.titulo1,orf.titulo2)
        fred1(fred.titulo1,fred.titulo2)
        haddad1(had.titulo1,had.titulo2)
        vinicius1(vin.titulo1,vin.titulo2)
        heloisa1(hel.titulo1,hel.titulo2)
        
        
        lor.titulo2 += velocidade_fundo        
        mir.titulo2 += velocidade_fundo
        orf.titulo2 += velocidade_fundo
        fred.titulo2 += velocidade_fundo           
        had.titulo2 += velocidade_fundo   
        vin.titulo2 += velocidade_fundo
        hel.titulo2 += velocidade_fundo
        

        imagem_carro(car_positionX,car_positionY)

        lor.crash()
        mir.crash()
        orf.crash()
        fred.crash()
        hel.crash()

        vin.crash2(1)
        #vin.titulo2 = -1500
        #vin.titulo1 = random.choice([210,375,540])

        
        had.crash2(2)
        #had.titulo2 = -1500
        #had.titulo1 = random.choice([210,375,540])

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