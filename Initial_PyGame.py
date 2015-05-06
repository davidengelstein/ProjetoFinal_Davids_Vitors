# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:21:27 2015

@author: vitor_000
"""
#pymunk

import pygame

pygame.init() #essencial para funcionar o pygame

display_width = 800 #Tamanho do display
display_height = 600 # Tamanho do display

black = (0,0,0) #Nenhuma opção de cor - Elemento 1 cor vermelha, Elemento 2 cor verde, Elemento 3 cor azul (cores primarias)
white = (255,255,255) #Todas opções de cores
red = (255,0,0) #Somente vermelha
green = (0,255,0)
blue = (0,0,255) 
#De acordo com isso podemos ir misturando as cores no display

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Cria o display e o seu respectivo tamanho
pygame.display.set_caption('Race Game') #Título da janela
clock = pygame.time.Clock()

carImg = pygame.image.load('southpark2.jpg') #Comando para carregar imagens
  
def car(x,y):
    gameDisplay.blit(carImg,(x,y)) #Coloca a imagem do carro no display, de acordo com as posições x e y. Lembrando que 0,0 é a o canto de cima esquerdo da tela
    
x = (display_width * 0.3) 
y = (display_height * 0.2)


a = 200
b= 300

crashed = False #Caso o carro colidir com os objetos na pista - Estamos contando que ele não colidiu

while not crashed:
      for event in pygame.event.get(): #Basicamente cria uma lista dos eventos que acontecem (pressionar teclas, etc...)
          if event.type == pygame.QUIT: #Pressionar o x da janela e fechar o jogo. Pode incrementar e criar janelas para isso
             crashed = True
      
      gameDisplay.fill(black) #Define a cor de fundo do display. NECESSITA ESTAR ANTES DE CHAMAR A FUNÇÃO CARRO!
      car(x,y) #Chamando a função car para nos mostrar o carro na posição (x,y) 
      #print(event) #Nos mostra os eventos que estão acontecendo
      pygame.display.update() #Update em toda a janela ... ou #pygame.display.flip()
      clock.tick(60) #Relacionado a velocidade do update - Valor pode ser alterado
pygame.quit()