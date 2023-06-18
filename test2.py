import pygame
from pygame.locals import *

pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prompt de Escritura")

# Configuración del prompt
font = pygame.font.Font(None, 32)
text_color = (255, 255, 255)
input_string = ""

# Configuración de la línea del prompt
line_color = (255, 255, 255)
line_x = 20  # Posición horizontal de la línea del prompt
line_height = 40  # Altura de la línea del prompt
line_width = 2  # Ancho de la línea del prompt
line_blink_interval = 500  # Intervalo de parpadeo de la línea en milisegundos
line_visible = True
last_blink_time = 0

# Bucle principal
running = True
while running:
    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time >= line_blink_interval:
        last_blink_time = current_time
        line_visible = not line_visible

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                # Eliminar el último carácter del string
                input_string = input_string[:-1]
            else:
                # Agregar el carácter ingresado al string
                input_string += event.unicode

    screen.fill((0, 0, 0))

    # Renderizar el texto en pantalla
    rendered_text = font.render(input_string, True, text_color)
    text_rect = rendered_text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(rendered_text, text_rect)

    # Dibujar la línea del prompt si es visible
    if line_visible:
        pygame.draw.line(screen, line_color, (text_rect.left + line_x, text_rect.bottom), (text_rect.left + line_x, text_rect.bottom + line_height), line_width)

    pygame.display.update()

pygame.quit()
