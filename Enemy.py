import random
import pygame
from Disparo import Disparo


class Enemy:
    def __init__(self) -> None:
        self.nave_imagen = pygame.image.load("enemy.png")
        self.nave_rect = self.nave_imagen.get_rect()
        self.nave_rect.x = 100
        self.nave_rect.y = 300
        self.col_rect =pygame.Rect(self.nave_rect.x, self.nave_rect.y+40,300,60)
        self.colision = False
        self.nave_visible = True
        self.nave_vivo = True
        self.nave_vida = 500
        self.direccion = "abajo"
        self.balas = []
        

    def actualizar_enemy(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.col_rect)
        screen.blit(self.nave_imagen,self.nave_rect)
        self.mover_enemy()
        for e in self.balas:
            e.mover()
            screen.blit(e.e_imagen,e.disparo_rect)

    def disparar_enemy(self,screen):
        bala = Disparo(self.nave_rect.centerx,self.nave_rect.centery,True)
        self.balas.append(bala)  

    def mover_enemy(self):
        if self.direccion == "abajo":
            if self.nave_rect.y < 600:
                self.nave_rect.y+=1
                self.col_rect.y+=1
            else:
                self.direccion = "arriba"
        elif  self.direccion == "arriba":
            if self.nave_rect.y > 0:
                self.nave_rect.y-=1
                self.col_rect.y-=1
            else:
                self.direccion = "abajo"

