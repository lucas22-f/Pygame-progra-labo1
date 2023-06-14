import pygame
import random
from Asteroide import Asteroide
from Nave import Nave
from Fondo import Fondo
from Disparo import Disparo
from Enemy import Enemy
def render_font_interfaz_main(font,mensaje,screen,x,y):
    text_surface = font.render(f"{mensaje}", True, "White")
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode([1280,720])
    pygame.display.set_caption("My game","jueguito")

    #TIMER
    tick = pygame.USEREVENT + 0 
    pygame.time.set_timer(tick,400)
    
    RELOJ = pygame.time.Clock()
    
    #ASTEROIDES
    lista_ast = Asteroide.crear_lista_ast(8)
    #colisiones asteroide - nave
    lista_colisionados = Asteroide.crear_lista_colisionados(lista_ast)
    #Particulas
    lista_particulas = Fondo.crear_lista_particulas(100)

    #NAVE
    nave = Nave()
    #Texto Vida nave
    font = pygame.font.Font("SPACESUI.TTF", 30)
    barra_vida = pygame.Surface((nave.nave_vida,30))
    ventana = True
    contador = 0


    #Enemigo
    enemy = Enemy()
    while(ventana):
        
        RELOJ.tick(60)
        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_UP]:
            Nave.actualizar_movimientoY(nave,-7)
        if lista_teclas[pygame.K_DOWN]:
            Nave.actualizar_movimientoY(nave,7)
        if lista_teclas[pygame.K_LEFT]:
            Nave.actualizar_movimientoX(nave,-7)
        if lista_teclas[pygame.K_RIGHT]:
            Nave.actualizar_movimientoX(nave,7)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                ventana = False
            if event.type == pygame.USEREVENT:
                if event.type == tick:
                    enemy.disparar_enemy()          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Nave.disparar(nave)


        screen.fill("Black")

        
        Asteroide.actualizar(lista_ast)
        Fondo.actualizar_particulas(lista_particulas)
        barra_vida = nave.actualizar_vida()
        Fondo.dibujar_particulas(lista_particulas,screen)
        Nave.actualizar(nave,screen)
        Nave.verificar_colision_bala(nave,lista_ast)
        Enemy.actualizar_enemy(enemy,screen)
        if nave.nave_vida > 0:
            Asteroide.verificar_colision(lista_ast,lista_colisionados,nave)
            Asteroide.actualizar_pantalla(lista_ast,screen)
            render_font_interfaz_main(font,"Vida",screen,1130,62)
            render_font_interfaz_main(font,f"score  {nave.score}",screen,200,62)
            contador+=1/60
            screen.blit(barra_vida,(972,8))
            render_font_interfaz_main(font,f"{int(contador)}",screen,600,62)
                


        pygame.display.flip()
    pygame.quit()
main()