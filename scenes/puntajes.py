import pygame
from pygame.locals import *
from globals import *
from funciones import *
from database.db import *

def puntaje(lista_particulas,player):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)
    title = pygame.font.Font("./fonts/SPACESUI.TTF", 50)
    text_player = pygame.font.Font("./fonts/Square Game.otf", 30)
    interface = pygame.font.Font("./fonts/Square Game.otf", 30)
    
    #Data player
    jugador = player.retornar_dic()
    if jugador['puntaje'] > 0:
        insertar_dato_en_tabla(jugador)
    
    lista_jugadores = traer_tabla_ordenada()

    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        render_font_interfaz_main(title,"--Puntajes--",screen,screen.get_rect().centerx,screen.get_rect().centery-290,"White")
        render_font_interfaz_main(interface,"BACKSPACE   <--- Volver al menu",screen,screen.get_rect().centerx,screen.get_rect().centery+320,"Yellow")
        render_font_interfaz_main(text_player,"{:^15}-{:^15}-{:^15}".format("Jugador", "Puntaje", "Tiempo"),screen,ANCHO/2,150,"White")
        if len(lista_jugadores) > 0:
            y = screen.get_rect().centery - 150
            for jugadores in lista_jugadores:
                render_font_interfaz_main(interface,"{:^13}--{:^13}--{:^13}".format(jugadores[1], jugadores[2], jugadores[3]),screen,ANCHO/2,y,"Purple")
                y+=30

        
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
