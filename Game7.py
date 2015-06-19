
# -*- coding: utf-8 -*-

import pygame
import random
import time
from random import choice
from firebase import firebase
from tkinter import *
import sys
import tkinter as tk


FIREBASE_URL = "https://car-game.firebaseio.com/"

global result

if __name__ == '__main__':
    # Cria uma referência para a aplicação Firebase
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Lê o dado da base de dados
    result = fb.get('/', "Scores")



#nome = input("Insira o seu nome: ")

escolha_Carro = 1 # 1  for Ferrari 2 for Mini

produto = result

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
grey = (69,69,69)



largura_da_tela = 800 #eixox
altura_da_tela = 600


smallfont = pygame.font.SysFont("comicsansms", 30)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 110)

gameDisplay = pygame.display.set_mode((largura_da_tela,altura_da_tela))

fps = 1000



img_mini = pygame.image.load('car8bits2.png')
img_ferrari = pygame.image.load('ferraricar.png')
img_delorean = pygame.image.load('delorean.png')
img_speed = pygame.image.load('speedracer.png')
imgcarro = img_mini
lourenco = pygame.image.load('lor.png')
miranda = pygame.image.load('mir.png')
orfali = pygame.image.load('orf.png')
fred5 = pygame.image.load('fred1.png')
haddad = pygame.image.load('had.png')
heloisa = pygame.image.load('helo2.png')
vinicius = pygame.image.load('vinicius1.png')
bala = pygame.image.load("bala.png")
cubo = pygame.image.load("ItemBox.png")
Mini2 = pygame.image.load('mini.png')
Mini = pygame.image.load('mini2.png')
Ferrari2 = pygame.image.load('Ferrari.png')
Ferrari = pygame.image.load('Ferrari2.png')
fundo = pygame.image.load('Fundo1.png')
space = pygame.image.load('space.png')
arrow = pygame.image.load('arrow.png')
Delorean = pygame.image.load('deloreann.png')
Delorean2 = pygame.image.load('deloreannpb.png')
Speed = pygame.image.load('speedracerr.png')
Speed2 = pygame.image.load('speedracerrpb.png')
helopeq = pygame.image.load('helopeq.png')
orfpeq = pygame.image.load('orfpeq.png')
fredpeq = pygame.image.load('fredpeq.png')
mirpeq = pygame.image.load('mirpeq.png')
lorpeq = pygame.image.load('lorpeq.png')
bruno = pygame.image.load('bruno.png')
bruno2 = pygame.image.load('bruno2.png')
calvin = pygame.image.load('calvin.png')
calvin2 = pygame.image.load('calvin2.png')
brinquedo = pygame.image.load('brinquedo.png')
brinquedo2 = pygame.image.load('brinquedo2.png')
garrix = pygame.image.load('garrix.png')
garrix2 = pygame.image.load('garrix2.png')
katy = pygame.image.load('katy.png')
katy2 = pygame.image.load('katy2.png')
acdc = pygame.image.load('acdc.png')
acdc2 = pygame.image.load('acdc2.png')
deserto = pygame.image.load('deserto.png')


virus = pygame.mixer.Sound('virus.wav')
firework = pygame.mixer.Sound('katy.wav')
thunder = pygame.mixer.Sound('thunderstruck.wav')
uptown = pygame.mixer.Sound('uptown8bits.wav')
bottle = pygame.mixer.Sound('DrinkingFromTheBottle.wav')
faustao = pygame.mixer.Sound('faustao.wav')
som = bruno


Imagem_Fundo = pygame.image.load('8bitsRoad.png')
Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))

fundointro = pygame.transform.scale(fundo,(largura_da_tela,altura_da_tela))
scorefinal = pygame.transform.scale(deserto,(largura_da_tela,altura_da_tela))



def cubos_contador(cont):
    font = pygame.font.SysFont(None, 40)
    text = font.render("tiros: "+str(cont), True, black)
    DisplayDoJogo.blit(text,(0,28))

def func_cubos(cubosx,cubosy):
    gameDisplay.blit(cubo,(cubosx,cubosy))

def desvio(contar):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(contar),True,green)
    DisplayDoJogo.blit(text,(0,0))

def text_objects(text,cor,size):
    if size == 'small':
        textSurface = smallfont.render(text,True,cor)
    elif size == 'medium':
        textSurface = medfont.render(text,True,cor)
    elif size == 'large':
        textSurface = largefont.render(text,True,cor)
    return textSurface,textSurface.get_rect()

def mensagem (msg,cor,y_displace=0,x_displace = 0,size='small'):
    textSurf, textRect = text_objects(msg,cor,size)    
    textRect.center = (largura_da_tela/2) + x_displace,(altura_da_tela/2) + y_displace
    DisplayDoJogo.blit(textSurf,textRect)
    
def botao(x,y,w,h,ic,ac,acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DisplayDoJogo, ac, (x,y,w,h))
        if click[0] == 1:
            if acao == 'play':
                rostos()
            if acao == 'quit':
                pygame.quit()
                quit()
            if acao == 'ranking':
                rank()          
            if acao == 'sim':
                music_select()
            if acao == 'nao':
                intro()
            if acao == 'mini':
                loop_jogo()
            if acao == 'ferrari':
                loop_jogo()
            if acao == 'delorean':
                loop_jogo()
            if acao == 'speed':
                loop_jogo()
            if acao == 'controles':
                controle()
            if acao == 'back':
                intro()
            if acao == 'playy':
                music_select()
            if acao == 'calvin':
                car_select()
            if acao == 'bruno':
                car_select()
            #if acao == 'brinquedo':
            if acao == 'garrix':
                car_select()
            if acao == 'katy':
                car_select()
            if acao == 'acdc':
                car_select()
            if acao == 'forward':
                restart()
            
    else:
        pygame.draw.rect(DisplayDoJogo, ic,(x,y,w,h))
        

def intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        
        
        DisplayDoJogo.blit(fundointro, (0,0))
        #pygame.draw.rect(DisplayDoJogo,white,[0,230,100,200])

                
        botao(310,370,190,40,black,green,acao = 'play')
        botao(310,430,190,40,black,red,acao = 'ranking')
        botao(310,490,190,40,black,blue,acao = 'controles')
        botao(310,550,190,40,black,yellow,acao = 'quit')
        

        font = pygame.font.SysFont(None, 40)
        text = font.render('PLAY',True,white)
        gameDisplay.blit(text,(366,380))
        
        font = pygame.font.SysFont(None, 40)
        text = font.render('RANKING',True,white)
        gameDisplay.blit(text,(336,440))

        font = pygame.font.SysFont(None, 40)
        text = font.render('CONTROLS',True,white)
        gameDisplay.blit(text,(325,500))
        
        font = pygame.font.SysFont(None, 40)
        text = font.render('QUIT',True,white)
        gameDisplay.blit(text,(369,560))
        
        pygame.display.update()

def gamb():
    intro()
    #pag_inicial.root.destroy()

abc = ""

def tkinter():
    global nome

    pag_inicial = Tk()
    pag_inicial.geometry('250x100+500+300')
    pag_inicial.title('Nome')

    nome = StringVar()

    shin_doidao = Label(pag_inicial,text = "Insira o seu nome:").pack()

    inserir_shin_doidao = Entry(pag_inicial,textvariable = nome).pack()

    shin_chapadao = Button(pag_inicial,text = "OK", command = gamb, fg = 'black', bg = 'white').pack()

    pag_inicial.mainloop()

    

def restart():

    restart = True

    while restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DisplayDoJogo.blit(fundointro, (0,0))
        mensagem('Play again?',red,80,0,'medium')
        #mensagem(Jogador.Score,green,0,0,'medium')

        botao(355,440,80,40,black,green,acao='sim')
        botao(355,515,80,40,black,red,acao='nao')

        font = pygame.font.SysFont(None, 40)
        text = font.render('YES',True,white)
        gameDisplay.blit(text,(370,450))

        font = pygame.font.SysFont(None, 40)
        text = font.render('NO',True,white)
        gameDisplay.blit(text,(375,525))

        pygame.mixer.Sound.stop(faustao)

        pygame.display.update()


def rank():
     rank = True
     while rank:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         gameDisplay.blit(deserto,(0,0))
         mensagem("RANKING",black,-265,0,'medium')
         mensagem("RANKING",red,-268,3,'medium')
         
         botao(690,550,100,40,black,yellow,acao='back')
         font = pygame.font.SysFont(None, 40)
         text = font.render('BACK',True,white)
         gameDisplay.blit(text,(700,560))         
         
         texto = ordena_ranking(produto).split("\n")
         ct = 0
         for linha in texto:
             mensagem(linha,black,-220 + ct*50,0,'small')
             mensagem(linha,yellow,-223 + ct*50,3,'small')
             
             ct +=1
         pygame.display.update()
         
def controle():

    controle = True

    while controle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DisplayDoJogo.fill(white)
        
        mensagem('Controls',red,-250,0,'medium')
        mensagem('Press the space button to shoot',blue,-60,0,'small')
        mensagem('Use the directionals to control the car',blue,190,0,'small')

        botao(690,550,100,40,black,yellow,acao='back')

        font = pygame.font.SysFont(None, 40)
        text = font.render('BACK',True,white)
        gameDisplay.blit(text,(700,560))

        gameDisplay.blit(space,(225,150))
        gameDisplay.blit(arrow,(280,300))
        
        pygame.display.update()    

def rostos():

    rostos = True

    while rostos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DisplayDoJogo.fill(grey)

        mensagem('Take these faces to get points',green,-150,90,'small')
        mensagem('Take this block to get ammo',yellow,220,90,'small')
        mensagem('Bypass these faces',red,60,90,'small')

        botao(690,550,100,40,black,green,acao='playy')

        font = pygame.font.SysFont(None, 40)
        text = font.render('PLAY',True,white)
        gameDisplay.blit(text,(705,560))

        gameDisplay.blit(haddad,(80,40))
        gameDisplay.blit(vinicius,(100,160))
        gameDisplay.blit(cubo,(100,490))
        gameDisplay.blit(helopeq,(80,300))
        gameDisplay.blit(mirpeq,(80,380))
        gameDisplay.blit(lorpeq,(150,300))
        gameDisplay.blit(fredpeq,(150,380))
        gameDisplay.blit(orfpeq,(210,340))
        
        

        pygame.display.update()

#def Score_Final():
    #Score_Final = True

    #while Score_Final:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #quit()

        #DisplayDoJogo.blit(scorefinal,(0,0))
        
        #botao(690,550,100,40,black,green,acao='forward')
        #font = pygame.font.SysFont(None, 40)
        #text = font.render('PLAY',True,white)
        #gameDisplay.blit(text,(705,560))

        #font = pygame.font.SysFont(None, 40)
        #text = font.render(Jogador.Score,True,black)
        #gameDisplay.blit(text,(200,200))        
        
        #pygame.display.update()
    

    #font = pygame.font.SysFont(None, 40)
    #text = font.render("Pinto",True,green)
    #DisplayDoJogo.blit(text,(200,200))
        
#def bater(Jogador):

    #print(Jogador.Score)
    #pygame.mixer.Sound.stop(som)
    #pygame.mixer.Sound.set_volume(faustao,1.0)
    #pygame.mixer.Sound.play(faustao)
    #mensagem('ERROOOOU!!!',red,0,0,'large')
    #pygame.display.update()
    #Ranking(Jogador.Score)
    #print(produto)
    #time.sleep(2)
    #loop_jogo()
    #Score_Final() 
    #restart()
    
class car_botao():
    carro = 'mini'
    def __init__(self,img,img2,x,y,w,h,acao=None):
        self.img = img
        self.img2 = img2
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.acao = acao

    def show_car(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            gameDisplay.blit(self.img2,(self.x,self.y))
            if click[0] == 1:
                if self.x == 58 and self.y == 140:
                    car_botao.carro = 'ferrari'
                    loop_jogo()            
                if self.x == 442 and self.y == 140:
                    car_botao.carro = 'mini'
                    loop_jogo()
                if self.x == 58 and self.y == 360:
                    car_botao.carro = 'delorean'
                    loop_jogo()
                if self.x == 442 and self.y == 360:
                    car_botao.carro = 'speed'
                    loop_jogo()
                
        else:
            gameDisplay.blit(self.img,(self.x,self.y))
                           
def car_select():

     sel = True

     while sel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(grey)

        Mini_object.show_car()
        Ferrari_object.show_car()
        Delorean_object.show_car()
        Speed_object.show_car()

        mensagem('Choose your car',red,-250,0,'medium')
        pygame.display.update()

Mini_object = car_botao(Mini,Mini2,442,140,300,188)
Ferrari_object = car_botao(Ferrari,Ferrari2,58,140,300,188)
Delorean_object = car_botao(Delorean2,Delorean,58,360,300,188)
Speed_object = car_botao(Speed2,Speed,442,360,300,188)

class music_botao():
    musica = 'uptown'

    def __init__(self,img,img2,x,y,w,h,acao=None):
        self.img = img
        self.img2 = img2
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.acao = acao

    def show_music(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            gameDisplay.blit(self.img2,(self.x,self.y))
            if click[0] == 1:
                if self.x == 65 and self.y == 80:
                    music_botao.musica = 'bruno'
                    car_select()
                if self.x == 555 and self.y == 80:
                    music_botao.musica = 'calvin'
                    car_select()
                #if self.x == 310 and self.y == 80:
                    #music_botao.musica = 'brinquedo'
                    #pass
                if self.x == 65 and self.y == 340:
                    music_botao.musica = 'garrix'
                    car_select()
                if self.x == 310 and self.y == 340:
                    music_botao.musica = 'katy'
                    car_select()
                if self.x == 555 and self.y == 340:
                    music_botao.musica = 'acdc'
                    car_select()
                
                
        else:
            gameDisplay.blit(self.img,(self.x,self.y))

def music_select():

    mus = True

    while mus:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(grey)

        calvin_object.show_music()
        bruno_object.show_music()
        brinquedo_object.show_music()
        garrix_object.show_music()
        katy_object.show_music()
        acdc_object.show_music()

        mensagem('Choose the artist',red,-270,0,'medium')
        pygame.display.update()

calvin_object = music_botao(calvin2,calvin,555,80,180,244)
bruno_object = music_botao(bruno2,bruno,65,80,180,244)
brinquedo_object = music_botao(brinquedo2,brinquedo,310,80,180,244)
garrix_object = music_botao(garrix2,garrix,65,340,180,244)
katy_object = music_botao(katy2,katy,310,340,180,244)
acdc_object = music_botao(acdc2,acdc,555,340,180,244)


        
        

def Ranking(Score):
    global nometext
    nometext = nome.get()
    ranking = {}
    ranking[nometext] = Score   
    produto.append(ranking)
    # Troque esta URL pela de seu próprio App Firebase
    FIREBASE_URL = "https://car-game.firebaseio.com/"
    # Main
    if __name__ == '__main__':
        fb = firebase.FirebaseApplication(FIREBASE_URL, None)
        # Escreve dados no Firebase
        fb.put('/', "Scores", produto)


def ordena(dici):
    if dici == None:
        return 0
    for k in dici:
        return dici[k]   

def ordena_ranking(produto):  
    ranking = ""
    ordem = list(reversed(sorted(produto, key=ordena)))[:10]    
    for cada in ordem:
        if cada == None:
            continue
        for i,j in cada.items():
            #print(i, " : ", j)
            ranking = ranking +  (str(i) + " : " + str(j) + "\n")
    print(ranking)
    return ranking
#gameDisplay.fill(black)

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
    #Imagem_Fundo = pygame.image.load('8bitsRoad.png')   
    #Imagem_Fundo = pygame.transform.scale(Imagem_Fundo,(largura_da_tela,1200))
    
    def fundo(x,y):
        DisplayDoJogo.blit(Imagem_Fundo,(x,y))

    global imgcarro
    global som
    
    if car_botao.carro == 'ferrari':
        imgcarro = img_ferrari
    elif car_botao.carro == 'mini':
        imgcarro = img_mini
    elif car_botao.carro == 'delorean':
        imgcarro = img_delorean
    elif car_botao.carro == 'speed':
        imgcarro = img_speed

    if music_botao.musica == 'bruno':
        som = uptown
    elif music_botao.musica == 'calvin':
        som = bottle
    #elif music_botao.musica == 'brinquedo':
        #pass
    elif music_botao.musica == 'garrix':
        som = virus
    elif music_botao.musica == 'katy':
        som = firework
    elif music_botao.musica == 'acdc':
        som = thunder

    
 
    pygame.mixer.Sound.play(som)
    
    velocidade_fundo = 10
    posição_inicial_fundo_y = -600
    posição_inicial_fundo_x = 0

    prof_largura = 60
    prof_altura = 60
    
    car_positionY = 475
    car_positionX = 375 #esquerda = 210 , meio = 375, direita = 540 - Variando de 165
    carX = 57
    carY = 106

    cubosx = choice([210,375,540])
    cubosy = 0
    cubos_speed = velocidade_fundo
    cubos_compr=60
    cubos_larg=66



    contador = 0
    lista_tiros = []

    etapas = {}
    etapas[5] = [1,False]
    #etapas[10] = [1,False]
    
    
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
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 50: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    bater(Jogador)
                    
                       

        def crash2 (self,value):
            if car_positionY < self.titulo2 + prof_altura and car_positionY + carY >= self.titulo2 + 20: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                if car_positionX > self.titulo1 and car_positionX < self.titulo1 + prof_largura or car_positionX + carX > self.titulo1 and car_positionX + carX < self.titulo1 + prof_largura:
                    
                    Jogador.Score += value
                    self.titulo2 = -1500
                    self.titulo1 = random.choice([210,375,540])
        
                

    class tiros:
        altura = 40
        largura = 10
        def __init__(self,imagem, display, posX,posY, vX = 0, vY = 0):
            self.imagem = imagem
            self.posX = posX
            self.posY = posY
            self.vX = vX
            self.vY = vY
            self.display = display
            
        def desenhar(self):
            self.display.blit(self.imagem, (self.posX, self.posY))
            
        def atualizar(self):
            self.posX += self.vX
            self.posY -= self.vY
            
        def add_obstaculos(self, obst):
            self.obstaculos = obst
            
        def add_lista(self, lista_tiros):
            self.lista_tiros = lista_tiros

        def crash3(self):
            for p in obstaculos:
                if self.posY < p.titulo2 + prof_altura and self.posY + tiros.altura >= p.titulo2: #Este e o próximo if realizam todas as possíveis opções de colisão com o bloco. São expressões matemáticas               
                    if self.posX > p.titulo1 and self.posX < p.titulo1 + prof_largura or self.posX + tiros.largura > p.titulo1 and self.posX + tiros.largura < p.titulo1 + prof_largura:
                        
                        p.titulo2 = -1500
                        p.titulo1 = random.choice([210,375,540])
                        lista_tiros.remove(self)
                        Jogador.Score += 3

    def Score_Final():
        Score_Final = True

        while Score_Final:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.mixer.Sound.stop(faustao)
            DisplayDoJogo.blit(scorefinal,(0,0))
            
            botao(690,550,100,40,black,green,acao='forward')
            font = pygame.font.SysFont(None, 40)
            text = font.render('SKIP',True,white)
            gameDisplay.blit(text,(705,560))

            font = pygame.font.SysFont(None, 60)
            text = font.render("Score: " + str(Jogador.Score),True,black)
            gameDisplay.blit(text,(330,200))

            #font = pygame.font.SysFont(None, 40)
            #text = font.render(str(Jogador.Score),True,black)
            #gameDisplay.blit(text,(387,250))        
            
            pygame.display.update()
    

    #font = pygame.font.SysFont(None, 40)
    #text = font.render("Pinto",True,green)
    #DisplayDoJogo.blit(text,(200,200))
        
    def bater(Jogador):

        print(Jogador.Score)
        pygame.mixer.Sound.stop(som)
        pygame.mixer.Sound.set_volume(faustao,1.0)
        pygame.mixer.Sound.play(faustao)
        mensagem('ERROOOOU!!!',red,0,0,'large')
        pygame.display.update()
        Ranking(Jogador.Score)
        #print(produto)
        time.sleep(2)
        #loop_jogo()
        Score_Final() 
        restart()
                        
                

    lor = personagens('posição_lourençoX','posição_lourençoY')
    mir = personagens('posição_mirandaX','posição_mirandaY')
    orf = personagens('posição_orfaliX','posição_orfaliY')
    fred = personagens('posição_fredX','posição_fredY')
    had = personagens('posição_haddadX','posição_haddadY')
    vin = personagens('posição_viniciusX','posição_viniciusY')
    hel = personagens('posição_heloisaX','posição_heloisaY')
    
    obstaculos = [lor, mir, orf, fred, hel]


    lor.posiniper(-2000,0)
    mir.posiniper(-3000,0)
    orf.posiniper(-2000,0)
    fred.posiniper(-2500,0)
    had.posiniper(-10000,0)
    vin.posiniper(-5000,0)
    hel.posiniper(-2500,0)
    

    print(velocidade_fundo)
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
                    
                
                if tecla.key == pygame.K_SPACE:
                    if contador > 0:
                        t = tiros(bala, DisplayDoJogo, car_positionX, car_positionY, 0, 10)
                        t.add_obstaculos(obstaculos)
                        lista_tiros.append(t)
                        t.add_lista(lista_tiros)
                        contador -= 1

        fundo(posição_inicial_fundo_x,posição_inicial_fundo_y)
        cubos_contador(contador)       
        func_cubos(cubosx, cubosy)

        lourenco1(lor .titulo1,lor.titulo2)
        miranda1(mir.titulo1,mir.titulo2)
        orfali1(orf.titulo1,orf.titulo2)
        fred1(fred.titulo1,fred.titulo2)
        haddad1(had.titulo1,had.titulo2)
        vinicius1(vin.titulo1,vin.titulo2)
        heloisa1(hel.titulo1,hel.titulo2)

        lor.posper2(1000,5000)
        mir.posper2(1000,5000)
        orf.posper2(1000,5000)
        fred.posper2(1000,5000)
        had.posper2(10000,20000)
        vin.posper2(10000,20000)
        hel.posper2(1000,5000)

        imagem_carro(car_positionX,car_positionY)

        lor.crash()
        mir.crash()
        orf.crash()
        fred.crash()
        hel.crash()

        vin.crash2(10)
        had.crash2(20)

        desvio(Jogador.Score)

        posição_inicial_fundo_y += velocidade_fundo

        cubosy += cubos_speed
                
        lor.titulo2 += velocidade_fundo        
        mir.titulo2 += velocidade_fundo
        orf.titulo2 += velocidade_fundo
        fred.titulo2 += velocidade_fundo           
        had.titulo2 += velocidade_fundo   
        vin.titulo2 += velocidade_fundo
        hel.titulo2 += velocidade_fundo

        if car_positionX > 637 - carX or car_positionX < 157:
            bater(Jogador)
                            
        if car_positionY > altura_da_tela - carY or car_positionY < 0:
            bater(Jogador)
                
        if posição_inicial_fundo_y == 0:
            posição_inicial_fundo_y = -600


        if car_positionY < cubosy + cubos_compr:
            if car_positionX > cubosx and car_positionX < cubosx + cubos_larg or car_positionX+carX > cubosx and car_positionX + carX < cubosx + cubos_larg:
            
                cubosy = (altura_da_tela-3000)
                cubosx = choice([230,360,540])
                contador+=1
                
                
            else:
                if cubosy > 800:
                    cubosy = (altura_da_tela-3000)
                    cubosx = choice([230,360,540])

        for t in lista_tiros:
            t.atualizar()
            t.desenhar()
            t.crash3()


        #if Jogador.Score in etapas:
            #if etapas[Jogador.Score][1] == False:
                #velocidade_fundo += etapas[Jogador.Score][0]
                #etapas[Jogador.Score][1] = True
                #print('Score: %d  Velocidade: %d '%(Jogador.Score, velocidade_fundo))

        
        #pygame.mixer.Sound.stop(faustao)

        pygame.display.update()
        framespersecond.tick(fps)


tkinter()
intro() 
controle()
rostos()
music_select()
car_select()
Score_Final()
restart()        
loop_jogo()
pygame.quit()
quit()
