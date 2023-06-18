import pygame
from pygame.locals import *
from constantes import *
from funciones import *
def menu(lista_particulas):
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(GAME_NAME)

    title = pygame.font.Font("./fonts/SPACESUI.TTF", 50)
    text_player = pygame.font.Font("./fonts/Square Game.otf", 30)
    puntaje = pygame.font.Font("./fonts/Starjout.ttf", 30)
    # Configuración de la fuente
    font = pygame.font.Font(None, 32)
    text_color = (255, 255, 255)
    input_string = ""

    # Obtener las dimensiones del rectángulo de texto
    text_rect = pygame.Rect(0, 0, 500, 50)
    text_rect.center = screen.get_rect().center
    
   
    # Bucle principal
    running = True
    while running:

        RELOJ.tick(60)
        screen.fill("Black")
        set_up_fondo(lista_particulas,screen)
        render_font_interfaz_main(title,"Puntajes:",screen,screen.get_rect().centerx,screen.get_rect().centery-550)
        render_font_interfaz_main(text_player,"player --- puntaje--- tiempo----",screen,screen.get_rect().centerx,screen.get_rect().centery-500)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                   menu()

       

        # Renderizar el texto en el rectángulo de texto
        rendered_text = font.render(input_string, True, text_color)
        text_surface = pygame.Surface((text_rect.width, text_rect.height))
        text_surface.fill((0,0,0,0))
        text_surface.blit(rendered_text, (10, 10))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
  
    pygame.quit()
