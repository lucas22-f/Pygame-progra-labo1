import pygame
import random
from Asteroide import Asteroide
from Nave import Nave
from Disparo import Disparo

def main():
    pygame.init()
    screen = pygame.display.set_mode([1280,720])
    pygame.display.set_caption("My game","jueguito")

    #TIMER
    tick = pygame.USEREVENT + 0 
    pygame.time.set_timer(tick,60)
    
    #ASTEROIDES
    lista_ast = Asteroide.crear_lista_ast(10)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Nave.disparar(nave)

         
       
        screen.fill((13,7,34)) 
        Nave.actualizar(nave,screen)
        Asteroide.actualizar_pantalla(lista_ast,nave,screen)

        pygame.display.flip()
    pygame.quit()
main()