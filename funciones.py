import pygame
from Asteroide import Asteroide
from Nave import Nave
from Fondo import Fondo
from Enemy import Enemy
from constantes import *

def set_game_run(lista_ast,nave,lista_particulas,screen,enemy):

    set_up_fondo(lista_particulas,screen)
    Asteroide.actualizar(lista_ast)
    Nave.verificar_colision_bala(nave, lista_ast)
    Nave.actualizar(nave, screen, enemy)
    Enemy.actualizar_enemy(enemy, screen, nave)

def set_game_interface(lista_ast,lista_colisionados,nave,screen,font,contador,barra_vida):


    Asteroide.verificar_colision(lista_ast, lista_colisionados, nave)
    Asteroide.actualizar_pantalla(lista_ast, screen)
    render_font_interfaz_main(font, "Vida", screen, 1130, 62)
    render_font_interfaz_main(font, f"score  {nave.score}", screen, 200, 62)
    contador += 1/60
    screen.blit(barra_vida, (972, 8))
    render_font_interfaz_main(font, f"{int(contador)}", screen, 600, 62)

def set_up_screen():
    screen = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("My game", "jueguito")
    return screen
def set_up_fondo(lista_particulas,screen):
    Fondo.actualizar_particulas(lista_particulas)
    Fondo.dibujar_particulas(lista_particulas, screen)

def set_timers():
    tick = pygame.USEREVENT + 0
    pygame.time.set_timer(tick, 400)
    return tick


def render_font_interfaz_main(font, mensaje, screen, x, y):
    text_surface = font.render(f"{mensaje}", True, "White")
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def setup_main_sounds():
    pygame.mixer.init()
    sonido = pygame.mixer.Sound("./sounds/fondo.mp3")
    sonido.set_volume(0.15)
    sonido2 = pygame.mixer.Sound("./sounds/music.mp3")
    sonido2.set_volume(0.055)
    if OPCION == 0:
        sonido2.play(1)
    elif OPCION == 1:
        sonido2.stop()
        sonido2.play(1)
        sonido.play(1)