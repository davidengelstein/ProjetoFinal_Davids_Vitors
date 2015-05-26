# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:46:03 2015

@author: david
"""

import pygame
import time
import random
from random import choice

pygame.init()

display_width = 1000
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 80

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("corrida")

clock = pygame.time.Clock()

carrinho = pygame.image.load("carro.png")
arqPista = pygame.image.load("pista.png")
arqvidas = pygame.image.load("vida.png")

dardo2 = pygame.image.load("tiro2.png")
cubo = pygame.image.load("caixinha.png")

def tiros(tirosx,tirosy):
    gameDisplay.blit(dardo2,(tirosx,tirosy))

    

def cubos_contador(cont):
    font = pygame.font.SysFont(None, 25)
    text = font.render("tiros: "+str(cont), True, black)
    gameDisplay.blit(text,(0,20)) 

def coisas_dodged(contador):
    font = pygame.font.SysFont(None, 25)
    text = font.render("pontos: "+str(contador), True, black)
    gameDisplay.blit(text,(0,0))

def pista(pista_startx,pista_starty):
    gameDisplay.blit(arqPista,(pista_startx,pista_starty))
    
def func_cubos(cubosx,cubosy):
    gameDisplay.blit(cubo,(cubosx,cubosy))        
    
def objetos(coisax,coisay, coisaw, coisah, cor):
    pygame.draw.rect(gameDisplay, cor, [coisax, coisay, coisaw, coisah])

def car(x,y):
    gameDisplay.blit(carrinho,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
    
def crash():
    message_display("voce bateu")

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.65)
    

    x_change = 0 
    
    coisa_startx = random.randrange(0, display_width)
    coisa_starty = -600
    coisa_speed = 5
    coisa_width = 100
    coisa_height = 80
    
    pista_startx = 0
    pista_starty = -1000
    pista_speed = coisa_speed
    
    cubosx = random.randrange(0, display_width)
    cubosy = 0
    cubos_speed = coisa_speed
    cubos_compr=100
    cubos_larg=120
    
    tirosx = x
    tirosy = y
    tiros_speed=1
    tiros_change = 0
    tiros_width = 5
    tiros_compr = 100
    
    dodged = 0
    
    gameExit = False
    cores = [black, red]
    c = choice(cores)
    contador=0
    
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                    tiros_change = x_change 
                if event.key == pygame.K_RIGHT:
                    x_change = 15
                    tiros_change = x_change
            
            
                        
                
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
                    

        x += x_change
        tirosx += tiros_change
        tirosx = x*1.1
        
        gameDisplay.fill(white)
        
        pista(pista_startx, pista_starty)
        #objetos(coisax,coisay, coisaw, coisah, cor)
        
        
        func_cubos(cubosx, cubosy)
        objetos(coisa_startx, coisa_starty, coisa_width, coisa_height, c)
        
        coisa_starty += coisa_speed
        cubosy += cubos_speed

        
        
                
        
        pista_starty += pista_speed
        while pista_starty >= (display_height - 1001):
            pista_starty = -1000
#        while viday > (display_height + 500):
#            viday = 0
#            vidax = random.randrange(0, display_width) 
        

        
                
        car(x,y)    
        coisas_dodged(dodged)
        cubos_contador(contador)
        
        
                    
                    
        if x > display_width - car_width  or x < 0:
            crash()
        
        if coisa_starty > display_height:
            coisa_starty = 0 - coisa_height
            coisa_startx = random.randrange(0, display_width)
            dodged +=1
        if y < coisa_starty + coisa_height:
            
            if x > coisa_startx and x < coisa_startx + coisa_width or x+car_width > coisa_startx and x + car_width < coisa_startx + coisa_width:
                if contador > 0:
                    contador = (contador-1)
            
                elif contador == 0:
                        crash()
                    

            else:
                coisa_speed+=0.005
                pista_speed+=0.005
                cubos_speed+=0.005
        if y < cubosy + cubos_compr:
            if x > cubosx and x < cubosx + cubos_larg or x+car_width > cubosx and x + car_width < cubosx + cubos_larg:
            
                cubosy = (display_height-3000)
                cubosx = random.randrange(0, display_width)
                contador+=1
                
            else:
                if cubosy > 700:
                    cubosy = (display_height-3000)
        #if tirosy+tiros_compr < coisa_starty + coisa_height:
            #if tirosx > coisa_startx and tirosx < coisa_startx + coisa_width or tirosx+tiros_width > coisa_startx and tirosx + tiros_width < coisa_startx + tiros_width:  
                #coisa_starty = display_height - 1500
        
        
        
        if contador > 0:    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
            
                    
                    tiros(tirosx,tirosy)
                    tiros_speed = 10
            
                    
                        
                    for i in range(1,600):
                        tiros_speed+=0.000002
                    
                    tirosy -= tiros_speed
    
                    if tirosy<-100:
                        if contador>0:
                            tirosy=y
                            contador-=1
                            
                            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    tiros(tirosx,tirosy)
                    tiros_speed = 10
                    
                    for i in range(1,600):
                        tiros_speed+=0.000002
                    
                    tirosy -= tiros_speed
                    if tirosy<-100:
                        if contador>0:
                            tirosy=y
                            contador-=1
                            
                    
                    
                    
                            
                            
                
                    

                    
                
            
                
        pygame.display.update()
        clock.tick(60)
        
        
game_loop()
pygame.quit()
quit ()
            