import pygame
import random
from Asteroide import Asteroide
from Nave import Nave
from Fondo import Fondo
from Disparo import Disparo


def main():
    pygame.init()
    screen = pygame.display.set_mode([1280,720])
    pygame.display.set_caption("My game","jueguito")

    #TIMER
    tick = pygame.USEREVENT + 0 
    pygame.time.set_timer(tick,40)

    RELOJ = pygame.time.Clock()
    
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
        
        RELOJ.tick(60)

        lista_teclas = pygame.key.get_pressed()

        if lista_teclas[pygame.K_UP]:
            Nave.actualizar_movimientoY(nave,-12)
        if lista_teclas[pygame.K_DOWN]:
            Nave.actualizar_movimientoY(nave,12)
        if lista_teclas[pygame.K_LEFT]:
            Nave.actualizar_movimientoX(nave,-12)
        if lista_teclas[pygame.K_RIGHT]:
            Nave.actualizar_movimientoX(nave,12)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                ventana = False
            if event.type == pygame.USEREVENT:
                if event.type == tick:
                    Asteroide.actualizar(lista_ast)
                    Fondo.actualizar_particulas(lista_particulas)
                    barra_vida = nave.actualizar_vida(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Nave.disparar(nave)
       
        screen.fill("Black") 
        Fondo.dibujar_particulas(lista_particulas,screen)
        Nave.actualizar(nave,screen)
        Nave.verificar_colision_bala(nave,lista_ast)
        if nave.nave_vida > 0:
            Asteroide.verificar_colision(lista_ast,lista_colisionados,nave)
            Asteroide.actualizar_pantalla(lista_ast,screen)
            text_surface = barra_vida[1].render("Vida nave jugador 1", True, "White")
            text_rect = text_surface.get_rect()
            text_rect.center = (1130,50)
            screen.blit(text_surface, text_rect)
            screen.blit(barra_vida[0],(972,1))

        pygame.display.flip()
    pygame.quit()
main()