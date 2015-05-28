# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:53 2015
@author: vitor_000,vitor_kitahara
"""

import pygame
import random
import time

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




moedass = pygame.image.load('moeda.png')

musica = pygame.mixer.music.load('uptown8bits.wav')
#faustao = pygame.mixer.Sound('faustao.wav')


Imagem_Fundo = pygame.image.load('8bitsRoad.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))


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
    Score = 0
    
    
    class personagens:
        def __init__(self,titulo1,titulo2):
            self.titulo1 = titulo1
            self.titulo2 = titulo2
            self.Score = 0
            
        def posiniper(self,random1,random2):
            self.titulo1 = random.choice([210,375,540])
            self.titulo2 = random.randrange(random1,random2)

        def posper2(self,random3,random4):
            if self.titulo2 > altura_da_tela:
                self.titulo2 = 0 - random.randrange(random3,random4)
                self.titulo1 = random.choice([210,375,540])
                self.Score += 1
            
        def crash(self):
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    bater()

        def crash2 (self,value):
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 60: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    self.Score += value

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

        lor.posper2(3500,4000)
        mir.posper2(100,3000)
        orf.posper2(6000,7000)
        fred.posper2(100,2500)
        had.posper2(5000,10000)
        vin.posper2(2000,5000)
        hel.posper2(100,2500)
        
            
        imagem_carro(car_positionX,car_positionY)
        
        lourenco1(lor.titulo1,lor.titulo2)
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
        had.crash2(2)


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