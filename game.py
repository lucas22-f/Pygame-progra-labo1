import pygame
import random
from Asteroide import Asteroide
from Nave import Nave
from Fondo import Fondo
def main():
    pygame.init()
    screen = pygame.display.set_mode([1280,720])
    pygame.display.set_caption("My game","jueguito")

    #TIMER
    tick = pygame.USEREVENT + 0 
    pygame.time.set_timer(tick,30)
    
    #ASTEROIDES
    lista_ast = Asteroide.crear_lista_ast(15)
    #colisiones asteroide - nave
    lista_colisionados = Asteroide.crear_lista_colisionados(lista_ast)

    
    #Particulas
    lista_particulas = Fondo.crear_lista_particulas(100)

    #NAVE
    nave = Nave()

    ventana = True

    while(ventana):
        


        lista_teclas = pygame.key.get_pressed()

        if lista_teclas[pygame.K_UP]:
            Nave.actualizar_movimientoY(nave,-1)
        if lista_teclas[pygame.K_DOWN]:
            Nave.actualizar_movimientoY(nave,1)
        if lista_teclas[pygame.K_LEFT]:
            Nave.actualizar_movimientoX(nave,-1)
        if lista_teclas[pygame.K_RIGHT]:
            Nave.actualizar_movimientoX(nave,1)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                ventana = False
            if event.type == pygame.USEREVENT:
                if event.type == tick:
                    Asteroide.actualizar(lista_ast)
                    Fondo.actualizar_particulas(lista_particulas)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Nave.disparar(nave)

         
       
        screen.fill((13,7,34)) 
        Fondo.dibujar_particulas(lista_particulas,screen)
        Nave.actualizar(nave,screen)
        Asteroide.verificar_colision(lista_ast,lista_colisionados,nave)
        Asteroide.actualizar_pantalla(lista_ast,nave,screen)
       

        pygame.display.flip()
    pygame.quit()
main()