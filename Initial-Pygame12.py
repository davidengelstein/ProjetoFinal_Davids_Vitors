# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:21:27 2015

@author: vitor_000
"""
#pymunk
import pygame
import time
import random

pygame.init() #essencial para funcionar o pygame

display_width = 800 #Tamanho do display
display_height = 600 # Tamanho do display
tkinput_1 = True

black = (0,0,0) #Nenhuma opção de cor - Elemento 1 cor vermelha, Elemento 2 cor verde, Elemento 3 cor azul (cores primarias)
white = (255,255,255) #Todas opções de cores
red = (255,0,0) #Somente vermelha
green = (0,255,0)
blue = (0,0,255)
block_color = (100, 230, 50)
car_width = 110
dodged = 0
#De acordo com isso podemos ir misturando as cores no display

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Cria o display e o seu respectivo tamanho
pygame.display.set_caption('Race Game') #Título da janela
clock = pygame.time.Clock()

carImg = pygame.image.load('ferrari-python.jpg') #Comando para carregar imagens

def things_dodged(count): #Função que define o score do player
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: '+str(count), True, red)
    gameDisplay.blit(text,(0,0)) #Sempre p/ colocar algo na tela necessita se usar o comando blit

def things(thingx, thingy, thingw, thingh, color): #Define as especificações dos "obstáculos" na pista
    pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh]) #Desenha nosso obstáculo retangulo com as respectivas características
  
def car(x,y):
    gameDisplay.blit(carImg,(x,y)) #Coloca a imagem do carro no display, de acordo com as posições x e y. Lembrando que 0,0 é a o canto de cima esquerdo da tela

def text_objects(text, font): #Não entendi muito bem essa função
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect() 

def message_display(text): #Função que define a mensagem no display
    largeText = pygame.font.Font('freesansbold.ttf', 115) #Comando que define a fonte e o tamanho da letra da mensagem no display
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2), (display_height/2) #Faz a janela aparecer no centro da tela
    gameDisplay.blit(TextSurf, TextRect) #Desenha os parâmetros da função, como o desenho do carro
    
    pygame.display.update()

    time.sleep(2) #Tempo em segundos para o jogo recomeçar após a mensagem aparecer na tela. Para funcionar nessecitar ser importado o time
    
    game_loop() #Recomeça todo o jogo após a mensagem no display

def crash(): #Função que roda caso o carro bater
    message_display('ERROOU!!')

def game_loop():
    
    x = (display_width * 0.45) 
    y = (display_height * 0.8)
    
    x_change = 0
    
    thing_startx = random.randrange(0,display_width) #Coloca no randon as posições x dos obstáculos
    thing_starty = -600 #Posição inicial no eixo y do obstáculo
    thing_speed = 7 #Velocidade com que o obstáculo se move no eixo Y
    thing_width = 100 #Essa e a próxima linha definem o tamanho do obstáculo
    thing_height = 100    
    
    gameExit = False #Caso o carro colidir com os objetos na pista - Estamos contando que ele não colidiu
    
    while not gameExit:
          for event in pygame.event.get(): #Basicamente cria uma lista dos eventos que acontecem (pressionar teclas, etc...)
              if event.type == pygame.QUIT: #Pressionar o x da janela e fechar o jogo. Pode incrementar e criar janelas para isso
                 pygame.quit()
                 quit()
              if event.type == pygame.KEYDOWN:   #Movimento para esquerda e direita enquanto apertamos a tecla baixo
                  if event.key == pygame.K_LEFT:
                      x_change = -5
                  elif event.key == pygame.K_RIGHT:
                      x_change = 5
              
              if event.type == pygame.KEYUP:    #Movimento para esquerda e direita enquanto apertamos a tecla cima
                  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                      x_change = 0
                      
          
          x += x_change          
          gameDisplay.fill(black) #Define a cor de fundo do display. NECESSITA ESTAR ANTES DE CHAMAR A FUNÇÃO CARRO!
          
          #things(thingx, thingy, thingw, thingh, color)
          things(thing_startx, thing_starty, thing_width, thing_height, block_color) #Chamando a função dos obstáculos de acordo com as variáveis
          thing_starty += thing_speed #Movimentando o objeto no eixo y de acordo com a velocidade pré-estabelecida
          car(x,y) #Chamando a função car para nos mostrar o carro na posição (x,y)
          things_dodged(dodged) #Chamando a função do score
          
          if x > (display_width - car_width) or x < 0: #Caso o carro bata nas fronteiras da tela o jogo acaba
              crash() #Chamando a função colisão
              
          if thing_starty > display_height: #Estas duas linhas definem que o bloco volte a aparecer como obstáculo
              thing_starty = 0 - thing_height #Bloco volta mais rápido
              thing_startx = random.randrange(0,display_width) #Volta em outra posição de acordo com a função random
                 
              global dodged   
              dodged += 1 #Aumenta um no score do player caso ele não colida com o bloco
              
              for i in range(1,100): #Sobe a dificuldade do game a cada 10 ups no score          
                  if dodged == 10*i:
                      thing_speed += 1*i
            
          if y < thing_starty+thing_height: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas 

              
              if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:

               crash()
          
          #print(event) #Nos mostra os eventos que estão acontecendo
          pygame.display.update() #Update em toda a janela ... ou #pygame.display.flip()
          clock.tick(100) #Relacionado a velocidade do update - Valor pode ser alterado

game_loop() #Chamando a função game_loop
pygame.quit()
quit()