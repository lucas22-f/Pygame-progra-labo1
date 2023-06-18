import pygame
from pygame.locals import *
from constantes import * 
from funciones import *
def menu(lista_particulas):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)

    title = pygame.font.Font("./fonts/SPACESUI.TTF", 50)
    sub_title = pygame.font.Font("./fonts/Square Game.otf", 30)
    puntaje = pygame.font.Font("./fonts/Starjout.ttf", 30)
    # Configuración de la fuente
    font = pygame.font.Font(None, 32)
    text_color = (255, 255, 255)
    input_string = ""

    # Obtener las dimensiones del rectángulo de texto
    text_rect = pygame.Rect(0, 0, 500, 50)
    
    rect_surface = pygame.Surface((503, 53), pygame.SRCALPHA)
    rect_surface.fill((0, 0, 0, 0))
    rect_surface.get_rect().center = screen.get_rect().center
    text_rect.center = screen.get_rect().center
    
   
    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        render_font_interfaz_main(title,"Space - Attack",screen,screen.get_rect().centerx,screen.get_rect().centery-150)
        render_font_interfaz_main(sub_title,"Ingresa tu nombre  luego ENTER para jugar",screen,screen.get_rect().centerx,screen.get_rect().centery-50)
        render_font_interfaz_main(puntaje,"Presiona P para ver los puntajes",screen,screen.get_rect().centerx,screen.get_rect().centery+100)

        pygame.draw.rect(rect_surface, (255, 255, 255), rect_surface.get_rect(), 3)
        screen.blit(rect_surface,(screen.get_rect().centerx-251,screen.get_rect().centery-27))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    # Eliminar el último carácter del string
                    input_string = input_string[:-1]
                elif event.key == K_RETURN:
                    # Realizar algo con el string ingresado (en este caso, solo imprimirlo)
                    print("String ingresado:", input_string)
                    input_string = ""
                    OPCION = 1
                    return OPCION 
                elif event.key == K_LCTRL:
                    print("PUNTAJES")
                else:
                    # Agregar el carácter ingresado al string
                    input_string += event.unicode

       

        # Renderizar el texto en el rectángulo de texto
        rendered_text = font.render(input_string, True, text_color)
        text_surface = pygame.Surface((text_rect.width, text_rect.height))
        text_surface.fill((0,0,0,0))
        text_surface.blit(rendered_text, (10, 10))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
  
    pygame.quit()
