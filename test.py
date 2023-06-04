import pygame
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colisión")

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Definir rectángulos de la nave y los asteroides
nave_rect = pygame.Rect(400, 300, 50, 50)

asteroides_rects = [
    pygame.Rect(200, 200, 30, 30),
    pygame.Rect(300, 400, 40, 40),
    pygame.Rect(500, 250, 35, 35)
]
RELOJ = pygame.time.Clock()
# Lista de colisiones por asteroide
colisiones_detectadas = [False] * len(asteroides_rects)
print(colisiones_detectadas)
# Función para comprobar colisiones
def colision(objeto1, objeto2):
    return objeto1.colliderect(objeto2)

# Bucle principal del juego
while True:
    RELOJ.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la nave
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        nave_rect.x -= 1
    if keys[K_RIGHT]:
        nave_rect.x += 1
    if keys[K_UP]:
        nave_rect.y -= 1
    if keys[K_DOWN]:
        nave_rect.y += 1

    pantalla.fill(BLANCO)  # Limpiar la pantalla

    # Dibujar la nave
    pygame.draw.rect(pantalla, ROJO, nave_rect)

    # Dibujar los asteroides
    for i, asteroide_rect in enumerate(asteroides_rects):
        pygame.draw.rect(pantalla, ROJO, asteroide_rect)
        asteroide_rect.x+=1
        # Verificar colisiones con cada asteroide
        if not colisiones_detectadas[i] and colision(nave_rect, asteroide_rect):
            colisiones_detectadas[i] = True
            print(f"¡Colisión con asteroide {i + 1}!")

    pygame.display.flip()

