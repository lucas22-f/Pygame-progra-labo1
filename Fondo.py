import pygame
import random

class Fondo:
    def __init__(self,x,y) -> None:
        self.superficie_particula = pygame.Surface((1,1))
        self.superficie_particula.fill("White")
        self.particula_rect = self.superficie_particula.get_rect()
        self.particula_rect.x = x
        self.particula_rect.y = y
        self.particula_velocidad = random.randrange(10,20,2)
        
    
    def crear_lista_particulas(cant):
        lista_particulas = []
        for e in range(cant):
            rand_y = random.randrange(0,700,70)
            rand_x = random.randrange(-1000,1000,70)
            particula = Fondo(rand_x,rand_y)
            lista_particulas.append(particula)
        return lista_particulas
    
    def actualizar_particulas(lista_particulas):
        for elemento in lista_particulas:
             elemento.particula_rect.x += elemento.particula_velocidad
             if elemento.particula_rect.x > 1250:
                elemento.particula_rect.x = random.randrange(-1000,0,70)
                elemento.particula_rect.y = random.randrange(30,700,70)

    def dibujar_particulas(lista_particulas,screen):
        for elemento in lista_particulas:
            pygame.draw.rect(screen,(250,0,0),elemento.particula_rect)
            screen.blit(elemento.superficie_particula,elemento.particula_rect)
           
