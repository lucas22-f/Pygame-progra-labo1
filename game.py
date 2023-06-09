import pygame
from Objetos.Asteroide import Asteroide
from Objetos.Nave import Nave
from Objetos.Fondo import Fondo
from Objetos.Enemy import Enemy
from Objetos.Player import Player

from funciones import *
from scenes.main import menu
from scenes.retry import reintentar
import globals
pygame.init()

#--------- INICIALIZAR VARIABLES ------------

# Screen
screen = set_up_screen()
# Timers
tick = set_timers()
# ASTEROIDES
lista_ast = Asteroide.crear_lista_ast(8)
# colisiones asteroide - nave
lista_colisionados = Asteroide.crear_lista_colisionados(lista_ast)
# Particulas
lista_particulas = Fondo.crear_lista_particulas(100)
# NAVE
nave = Nave()
# Texto Vida nave
font = pygame.font.Font("./fonts/SPACESUI.TTF", 30)
# Vida Nave
barra_vida = pygame.Surface((nave.nave_vida, 30))
# Enemigo
enemy = Enemy()
# Sonidos
setup_main_sounds()



#----------Variables booleanas y contadores----------
ventana = True
nave.contador = 0

player = Player("",0,0)
#----------BUCLE PRINCIPAL_-----------------
while (ventana):

    #Aplicamos try except para interceptar cualquier error de ejecucion del juego
    try:
        #consultamos por la variable Global que controla la opcion del menu, 
        if OPCION == 0:
               
               #func menu actualiza el valor de la variable Opcion
            OPCION = menu(lista_particulas,player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ventana = False    


            #si OPCION = 1 entonces entramos al juego
        elif OPCION == 1:
        
            #set FPS
            RELOJ.tick(60)

            #Manejo Teclas Movimiento
            lista_teclas = pygame.key.get_pressed()
            if lista_teclas[pygame.K_UP]:
                Nave.actualizar_movimientoY(nave, -7)
            if lista_teclas[pygame.K_DOWN]:
                Nave.actualizar_movimientoY(nave, 7)
            if lista_teclas[pygame.K_LEFT]:
                    Nave.actualizar_movimientoX(nave, -7)
            if lista_teclas[pygame.K_RIGHT]:
                Nave.actualizar_movimientoX(nave, 7)


            #Manejo Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ventana = False
                if event.type == pygame.USEREVENT:
                    if event.type == tick:
                        enemy.disparar_enemy()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Nave.disparar(nave)

            #Color - Fondo
            screen.fill("Black")

            #Funcion que actualiza los elementos del juego:
            set_game_run(lista_ast,nave,lista_particulas,screen,enemy)
            barra_vida = nave.actualizar_vida()

            #Func que actualiza la interfas dependiendo la vida de la nave.
            if nave.nave_vida > 0:
                set_game_interface(lista_ast,lista_colisionados,nave,screen,font,barra_vida)
                nave.contador += 1/60
                render_font_interfaz_main(font, f"{int(nave.contador)}", screen, 600, 62,"White")
            else:
                #Si la nave murio entonces guardamos los datos del ultimo jugador y lanzamos la pantalla de reintento actualizando OPCION
                #nuevamente .
                player = Player(globals.PLAYER_NAME,nave.score,int(nave.contador))
                OPCION = reintentar(lista_particulas,nave,lista_ast)

        pygame.display.flip()
    except pygame.error as e:
        print("Fin del juego")
        ventana = False

pygame.quit()
