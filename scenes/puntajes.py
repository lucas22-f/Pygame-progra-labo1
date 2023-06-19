import pygame
from pygame.locals import *
from globals import *
from funciones import *

def puntaje(lista_particulas,player):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)
    title = pygame.font.Font("./fonts/SPACESUI.TTF", 50)
    text_player = pygame.font.Font("./fonts/Square Game.otf", 30)
    interface = pygame.font.Font("./fonts/Square Game.otf", 20)

    #Data player
    print(player.retornar_dic())


    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        render_font_interfaz_main(title,"--Puntajes--",screen,screen.get_rect().centerx,screen.get_rect().centery-290)
        render_font_interfaz_main(text_player,"--- player --- puntaje --- tiempo ---",screen,screen.get_rect().centerx,screen.get_rect().centery-190)
        render_font_interfaz_main(interface,"BACKSPACE   <--- Volver al menu",screen,screen.get_rect().centerx,screen.get_rect().centery+320)
        for event in pygame.event.get():
            
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    OPCION2 = 0
                    return OPCION2
                    
        # Renderizar el texto en el rectángulo de texto
       

        pygame.display.flip()
  
    pygame.quit()
