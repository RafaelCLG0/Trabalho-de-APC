





#------------Meu Projeto em Python-------------------------#
#Nome: Rafael Ferreira Leandro
#Matrícula: 211041286


import pygame
from random import randint

#inicializa todos os módulos pygame importados
pygame.init()

#Tamanho da Janela
janela = pygame.display.set_mode ((840,650))

#Define o nome da Janela
pygame.display.set_caption("Jogo de Corrida em Python")


#Localização do Meu carro
x= 380                                                          #Meu carro  Max= 630 Min= 140
y= 300                                                          #Meu carro Max=0 Min=470

#Local aonde o Carro Roxo vai aparecer

carro_x_r = 200                                                     #Carro Roxo
carro_y_r = randint(800,1000)                                       #Carro Roxo
        #Condição para aparecer aleatoriamente dentre do limite

#Local aonde o carro da Policia vai aparecer
carro_x_p = 300                                                   #Policia
carro_y_p = randint(1300,3000)                                    #Policia
        #Condição para aparecer aleatoriamente dentre do limite
#Local aonde o Taxi vai aparecer

carro_x_t = 450                                                   #Taxi
carro_y_t = randint(-1000,-200)                                   #Taxi
        #Condição para aparecer aleatoriamente dentre do limite

#Local aonde o Carro Branco vai aparecer
carro_x_b = 575                                                   #Carro Branco
carro_y_b = randint(-2000,-300)                                   #Carro Branco
        #Condição para aparecer aleatoriamente dentre do limite


#Variavel de indicação do estado do Menu
menu = 1
#Variavel de indicação do estado do Game Over
gamer_over = 0
#Variavel de indicação do estado do tempo
timer = 0
#Variavel de indicação do estado do tempo em segundos
tempo_segundo = 0

#Velocidade aleatoria dentro do limite dos outros carros(Carro Roxo, Carro Branco, Policia e Taxi)
velocidade_outros = randint(10,100)

#Velocidade do Meu carro
velocidade = 20



#Função para importar as imagem para o jogo

fundo = pygame.image.load('assets/pista.png')
meu_carro = pygame.image.load('assets/Meu carro.png')
carro_roxo = pygame.image.load('assets/Carro_Comum2.png')
taxi = pygame.image.load('assets/Taxi.png')
carro_branco = pygame.image.load('assets/Carro_Comum.png')
police = pygame.image.load('assets/Police.png')


#Definição da Função para Exibir os textos na tela
def exibe_textos(msg, tamanho, cor):

    fonte = pygame.font.SysFont('comicsansms',tamanho, True, False)
    mensagem = f'{msg}'
    texto_format = fonte.render(mensagem, True, cor)
    return texto_format

#Incrementa o Score do jogo
Tempo = exibe_textos('Score:'+str(tempo_segundo), 40, (0,0,0))

#Variavel que chama e toca a música no jogo
musica_de_fundo = pygame.mixer.music.load('assets/Intro.wav')
pygame.mixer.music.play(-1)



#Variavel booleana
janela_aberta = True
#Loop de condição para executar dentro do While
while janela_aberta:
    #Executar o Menu do jogo
    if menu == 1:

        #Condição para quando disparar algum evento ele atualizar ou fechar a janela
        for event in pygame.event.get():
            #Evento para fechar a Janela
            if event.type == pygame.QUIT:
                #Vai sair do Loop do While e fechar a janela
                janela_aberta = False

        #Imagem do Menu
        menu_tela = pygame.image.load('assets/Menu1.png')
        #Imagem das Teclas
        tecla = pygame.image.load('assets/Teclas.png')

        #Função para aparecer a Imagem na Tela (Menu e Teclas)
        janela.blit(menu_tela, (0,0))
        janela.blit(tecla, (400,50))

        #Variavel para aparecer a mensagem indicada formatada
        Menu = exibe_textos('Pressione Espaço para iniciar', 40, (0,0,0))
        controles = exibe_textos('Controles:', 40, (0,0,0))

        janela.blit(Menu, (150,10))
        janela.blit(controles, (200,120))

        #Variavel de comandos
        comandos = pygame.key.get_pressed()
        #Condição para Inicializar o jogo e sair do Menu
        if comandos[pygame.K_SPACE]:
            menu = 0
            #Função de para a música do Menu
            pygame.mixer.music.stop()

            #Função de Retornar a música
            pygame.mixer.music.rewind()
            #Chamar outra música
            musica_de_fundo = pygame.mixer.music.load('assets/Playingame.wav')
            pygame.mixer.music.play(-1)

        #Função de atualizar o codigo por um período de tempo
        pygame.time.delay(50)
        #Função de atualizar partes da tela
        pygame.display.update()

    #Quando Sair do Menu
    else:
        #Condição para rodar o jogo   
        if gamer_over == 0:

            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False


            #Variavel para executar os comandos do player
            comandos = pygame.key.get_pressed()
            #Comandos de movimentos
            if comandos[pygame.K_UP] and y >= 1:
                y -= velocidade
            if comandos[pygame.K_DOWN] and  y <= 460:
                y += velocidade
            if comandos[pygame.K_RIGHT] and x <= 620:
                x += velocidade
            if comandos[pygame.K_LEFT] and x >= 150:
                x -= velocidade
            if comandos[pygame.K_w] and y >= 1:
                y -= velocidade
            if comandos[pygame.K_s] and  y <= 460:
                y += velocidade
            if comandos[pygame.K_d] and x <= 620:
                x += velocidade
            if comandos[pygame.K_a] and x >= 150:
                x -= velocidade




            #Comandos que fazem os carro andarem
            if (carro_y_r <= -300):
                carro_y_r = randint(800,1000)
            if (carro_y_p <= -300):
                carro_y_p = randint(1300,3000)  
            if (carro_y_t >= 650):
                carro_y_t = randint(-1000,-200)
            if (carro_y_b >= 650):
                carro_y_b = randint(-2000,-300)
            
            #Condição do Tempo
            if (timer < 20):
                timer += 1
            #Aplica a condição do Tempo
            else:
                tempo_segundo += 1
                Tempo = exibe_textos('Score:'+str(tempo_segundo), 40, (0,0,0))
                timer = 0


            #Aplica a Velocidade dos outros carros
            carro_y_r -= velocidade_outros
            carro_y_t += velocidade_outros
            carro_y_b += velocidade_outros 
            carro_y_p -= velocidade_outros

            #Adiciona a imagem da pista,tempo e carros
            janela.blit(fundo,(0,0))
            Meu_carro1 = janela.blit(meu_carro, (x,y))
            CarroRoxo = janela.blit(carro_roxo, (carro_x_r,carro_y_r))
            Taxi = janela.blit(taxi, (carro_x_t,carro_y_t))
            CarroBranco = janela.blit(carro_branco, (carro_x_b,carro_y_b))
            Policia = janela.blit(police, (carro_x_p,carro_y_p))
            janela.blit(Tempo, (10,60))

            #Condição de colisão
            if Meu_carro1.colliderect(CarroRoxo):
                gamer_over = 1
            if Meu_carro1.colliderect(Taxi):
                gamer_over = 1
            if Meu_carro1.colliderect(CarroBranco): 
                gamer_over = 1
            if Meu_carro1.colliderect(Policia): 
                gamer_over = 1

            pygame.display.update()





        #Reniciar o Jogo
        else:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False


            pygame.mixer.music.stop()

            #Aparece a função reniciar com Game Over, Reniciar e Score
            gameover = exibe_textos('Game Over', 80, (255,255,255))
            janela.blit(gameover, (200,150))
            restart = exibe_textos('Pressione r para reiniciar', 40, (255,255,0))
            janela.blit(restart, (180,250))
            Score = exibe_textos('Score:'+str(tempo_segundo), 40, (255,255,255))
            janela.blit(Score, (320,320))


            pygame.display.update()

            #Incrementa a função "Reniciar"
            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_r]:

                pygame.mixer.music.rewind()
                musica_de_fundo2 = pygame.mixer.music.load('assets/Playingame.wav')
                pygame.mixer.music.play(-1)


                x= 380                              #Meu carro
                y= 300                              #Meu carro
                carro_x_r = 200                     #Carro Roxo
                carro_y_r = randint(800,1000)       #Carro Roxo
                carro_x_p = 300                     #Policia
                carro_y_p = randint(1300,3000)      #Policia
                carro_x_t = 450                     #taxi
                carro_y_t = randint(-1000,-200)     #taxi
                carro_x_b = 575                     #Carro Branco
                carro_y_b = randint(-2000,-300)     #Carro Branco


                timer = 0
                tempo_segundo = -1

                velocidade_outros = randint(20,30)
                velocidade = 20
                gamer_over = 0







#Desinicializar todos os módulos pygame
pygame.quit()    


#--------------------------------------Link Utilizados-------------------------------------------------#

#Imagem da Tela do Menu 

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fbr.ign.com%2Fhorizon-chase-turbo%2F59942%2Ffeature%2Fhorizon-chase-turbo-mudamos-tudo-para-adaptar-o-game-para-o-ps4&psig=AOvVaw0GfNRAE4uX-I71JH94v5Vu&ust=1636221072044000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjsr9LkgfQCFQAAAAAdAAAAABAD 

#Imagem dos Controles 

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Fbr%2Ficone-gratis%2Fteclado_854120&psig=AOvVaw1MHxE8u-LWEFRv-VG1ID5N&ust=1636221116949000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLiw0ufkgfQCFQAAAAAdAAAAABAJ 

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Ffr%2Fvectoriel%2Fclavier-de-joueur-dordinateur-touches-wasd-illustration-de-vecteur-touches-wasd-gm1193231012-339319726&psig=AOvVaw1MHxE8u-LWEFRv-VG1ID5N&ust=1636221116949000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLiw0ufkgfQCFQAAAAAdAAAAABAY 

#Imagens Carros 

#https://br.freepik.com/vetores-gratis/conjunto-de-vista-superior-do-vetor-carros-picape-conversivel-de-automovel-e-jipe-taxi-e-policia_11060845.htm?query=carros%20vista%20de%20cima 

#https://br.freepik.com/vetores-gratis/carro-de-policia-e-taxi-carro-esporte-e-sedan-sinal-de-transporte-automovel-direcao-e-simbolo_10700715.htm?query=carros%20vista%20de%20cima 

#Músicas 

#https://youtu.be/tA7a_EEgwrw 

#https://youtu.be/oqL8i8kEMWA?list=PLD677B4A66D9CD31F 

#Link da Playlist 
 
#https://youtu.be/ddgppBdhVn8?list=PLwsAoT89dh3qNpl9MpvMan-zLWb4gQKAb

#Site de Suporte

#https://www.pygame.org/docs/ref/pygame.html 
