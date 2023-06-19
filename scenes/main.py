import pygame
from pygame.locals import *
import globals
from funciones import *
from scenes.puntajes import puntaje
def menu(lista_particulas,player):

    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)

    title = pygame.font.Font("./fonts/SPACESUI.TTF", 50)
    sub_title = pygame.font.Font("./fonts/Square Game.otf", 30)
    puntajes = pygame.font.Font("./fonts/Starjout.ttf", 30)


    # Configuración de la fuente
    font = pygame.font.Font(None, 32)
    text_color = (255, 255, 255)
   

    # Obtener las dimensiones del rectángulo de texto
    text_rect = pygame.Rect(0, 0, 500, 50)
    
    rect_surface = pygame.Surface((503, 53), pygame.SRCALPHA)
    rect_surface.fill((0, 0, 0, 0))
    rect_surface.get_rect().center = screen.get_rect().center
    text_rect.center = screen.get_rect().center
    OPCION2 = 0
   
    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        if OPCION2 == 0:
            render_font_interfaz_main(title,"Space - Attack",screen,screen.get_rect().centerx,screen.get_rect().centery-150)
            render_font_interfaz_main(sub_title,"Ingresa tu nombre  luego        ENTER  <--|    para jugar",screen,screen.get_rect().centerx,screen.get_rect().centery-70)
            render_font_interfaz_main(puntajes,"Presiona Ctrl para ver los puntajes",screen,screen.get_rect().centerx,screen.get_rect().centery+100)

            pygame.draw.rect(rect_surface, (255, 255, 255), rect_surface.get_rect(), 3)
            screen.blit(rect_surface,(screen.get_rect().centerx-251,screen.get_rect().centery-27))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        # Eliminar el último carácter del string
                        globals.PLAYER_NAME = globals.PLAYER_NAME[:-1]
                    elif event.key == K_RETURN:
                        # Realizar algo con el string ingresado (en este caso, solo imprimirlo)
                        print(globals.PLAYER_NAME)
                        input_string = ""
                        OPCION = 1
                        print(OPCION)
                        return OPCION 
                    elif event.key == K_LCTRL:
                        OPCION2 = puntaje(lista_particulas,player)
                    else:
                        # Agregar el carácter ingresado al string
                        globals.PLAYER_NAME += event.unicode
        elif OPCION2 == 1:
            OPCION2 = puntaje(lista_particulas)
       

        # Renderizar el texto en el rectángulo de texto
        rendered_text = font.render(globals.PLAYER_NAME, True, text_color)
        text_surface = pygame.Surface((text_rect.width, text_rect.height))
        text_surface.fill((0,0,0,0))
        text_surface.blit(rendered_text, (10, 10))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
  
    pygame.quit()
