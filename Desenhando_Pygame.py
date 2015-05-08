# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:32:20 2015

@author: vitor_000
"""

import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)


pixAr = pygame.PixelArray(gameDisplay) #Comando para transformar o fundo da tela em pixels
pixAr[10][20] = green #Este comando pinta o pixel localizado no x = 10 e y = 20 de verde

pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5) #Este comando desenha uma linha no gameDisplay, de azul, iniciando no ponto (100,200) e terminando no ponto (300, 450). A linha tem 5 pixels

pygame.draw.rect(gameDisplay, red, (400,400,50,25)) #Este comando desenha retângulos. 400 e 400 significa o ponto esquerdo alto de início e os outros dois a largura e a altura.

pygame.draw.circle(gameDisplay, white, (150,150), 76) #Este comando desenha circulos. 150 e 150 significa o centro do circulo e 76 o raio.

pygame.draw.polygon(gameDisplay, green, ((25,75), (76,125), (250,375))) #Desenha poligonos. Basta especificar os pontos.

#Estes comandos podem ser úteis para desenharmos nossa pista e algum cenário do lado dela 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()