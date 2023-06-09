import random
import pygame
from Disparo import Disparo
from Asteroide import Asteroide

class Nave:
    def __init__(self) -> None:
        self.nave_imagen = pygame.image.load("nave.png")
        self.nave_imagen = pygame.transform.scale(self.nave_imagen,(120,70))
        self.nave_rect = self.nave_imagen.get_rect()
        self.nave_rect.x = 1100
        self.nave_rect.y = 300
        self.col_rect =pygame.Rect(1050+120/2,300+20,100,30)
        self.colision = False
        self.nave_visible = True
        self.nave_vivo = True
        self.nave_vida = 300
        self.balas = []

    def actualizar(self,screen):
            if self.nave_visible:
                pygame.draw.rect(screen,(0,250,0),self.col_rect)
                screen.blit(self.nave_imagen,self.nave_rect)
            for i,balas in enumerate(self.balas):
                pygame.draw.rect(screen,(255,255,255),balas.disparo_rect)
                balas.mover()
                screen.blit(balas.imagen, balas.disparo_rect)
                if balas.disparo_rect.left < -10 or balas.disparo_rect.right > 1230:
                    self.balas.pop(i)
                    
    def disparar(self):
        if self.nave_vivo:
            bala = Disparo(self.nave_rect.centerx,self.nave_rect.centery)
            self.balas.append(bala)
    
    def actualizar_vida(self,screen):
        
        barra_vida = pygame.Surface((self.nave_vida,30))
        barra_vida.fill("Green")
        return barra_vida
    
    def verificar_colision_bala(self, lista_ast):
        for bala in self.balas:
            for asteroide in lista_ast:
                if  bala.verificar_colision_asteroide(asteroide):
                    asteroide.asteroide_rect.x = 1300
                    asteroide.asteroide_rect.y = random.randrange(0,700,70)
                    asteroide.velocidad+=random.randrange(0,10,1)
                    bala.disparo_rect.x = 1300
           
    def actualizar_movimientoY(self,mov_y):
         new_y = self.col_rect.y+ mov_y
         if new_y > 0 and new_y < 650:
               self.col_rect.y+= mov_y
               self.nave_rect.y+= mov_y

    def actualizar_movimientoX(self,mov_x):
         new_x = self.col_rect.x+ mov_x
         if new_x > 1100 and new_x < 1160:
               self.col_rect.x+= mov_x
               self.nave_rect.x+= mov_x


               