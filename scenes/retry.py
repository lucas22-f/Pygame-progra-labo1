import pygame
from pygame.locals import *
import globals
from funciones import *

import random
def reset_nave(nave,lista_ast):
    nave.nave_vida = 300
    nave.nave_rect.y = 300
    nave.nave_rect.x = 1100
    nave.col_rect = pygame.Rect(1050+60,300+20,100,40)
    nave.nave_visible = True
    nave.nave_vivo = True
    nave.score = 0
    for e in lista_ast:
        e.velocidad = random.randrange(1,3,1)
    
def reintentar(lista_particulas,player,nave,lista_ast):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)
    title = pygame.font.Font("./fonts/Starjout.ttf", 50)
    sub_title = pygame.font.Font("./fonts/Square Game.otf", 30)

    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        render_font_interfaz_main(title,"Reintentar ? ",screen,screen.get_rect().centerx,screen.get_rect().centery-290,"White")
        render_font_interfaz_main(sub_title,"R -- Reintentar",screen,screen.get_rect().centerx,screen.get_rect().centery-100,"White")
        render_font_interfaz_main(sub_title,"M -- Menu Principal",screen,screen.get_rect().centerx,screen.get_rect().centery-50,"White")
        render_font_interfaz_main(sub_title,"ESC -- SALIR DEL JUEGO",screen,screen.get_rect().centerx,screen.get_rect().centery,"White")
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    reset_nave(nave,lista_ast)
                    OPCION = 1
                    return OPCION
                elif event.key == K_m:
                    reset_nave(nave,lista_ast)
                    OPCION = 0
                    return OPCION
                elif event.key == K_ESCAPE:
                    running = False
                    
        # Renderizar el texto en el rectángulo de texto
       

        pygame.display.flip()
  
    pygame.quit()
