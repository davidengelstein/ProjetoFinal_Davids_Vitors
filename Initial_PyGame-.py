# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:21:27 2015

@author: vitor_000
"""
#pymunk

import pygame

pygame.init() #essencial para funcionar o pygame
gameDisplay = pygame.display.set_mode((800,600)) #tamanhododisplay
pygame.display.set_caption('Race Game') #Título da janela
clock = pygame.time.Clock()

crashed = False #Caso o carro colidir com os objetos na pista - Estamos contando que ele não colidiu

while not crashed:
      for event in pygame.event.get(): #Basicamente cria uma lista dos eventos que acontecem (pressionar teclas, etc...)
          if event.type == pygame.QUIT: #Pressionar o x da janela e fechar o jogo. Pode incrementar e criar janelas para isso
             crashed = True
             
          print(event) #Nos mostra os eventos que estão acontecendo
      pygame.display.update() #Update em toda a janela ... ou #pygame.display.flip()
      clock.tick(60) #Relacionado a velocidade do update - Valor pode ser alterado
pygame.quit()