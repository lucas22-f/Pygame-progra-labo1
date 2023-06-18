import pygame
from pygame.locals import *
from constantes import * 
from funciones import *
def menu(lista_particulas):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Ingresar un String")

    # Configuración de la fuente
    font = pygame.font.Font(None, 32)
    text_color = (0, 255, 0)
    input_string = ""

    # Obtener las dimensiones del rectángulo de texto
    text_rect = pygame.Rect(0, 0, 200, 50)
    text_rect.center = screen.get_rect().center

    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)

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
                else:
                    # Agregar el carácter ingresado al string
                    input_string += event.unicode

       

        # Renderizar el texto en el rectángulo de texto
        rendered_text = font.render(input_string, True, text_color)
        text_surface = pygame.Surface((text_rect.width, text_rect.height))
        text_surface.fill((255, 255, 255))
        text_surface.blit(rendered_text, (10, 10))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
  
    pygame.quit()
