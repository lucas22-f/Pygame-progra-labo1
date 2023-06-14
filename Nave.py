import random
import pygame
from Disparo import Disparo
from Asteroide import Asteroide

class Nave:
    def __init__(self) -> None:
        self.nave_imagen = pygame.image.load("./imagenes/nave.png")
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
        self.score = 0

    def actualizar(self,screen):
            if self.nave_visible:
                screen.blit(self.nave_imagen,self.nave_rect)
            for i,balas in enumerate(self.balas):
                balas.mover()
                screen.blit(balas.imagen, balas.disparo_rect)
                if balas.disparo_rect.x < -10 or balas.disparo_rect.x > 1330:
                    self.balas.pop(i)
                    
    def disparar(self):
        if self.nave_vivo:
            bala = Disparo(self.nave_rect.centerx,self.nave_rect.centery,False)
            self.balas.append(bala)
    
    def actualizar_vida(self):
        barra_vida = pygame.Surface((self.nave_vida,30))
        barra_vida.fill("Green")
        return barra_vida
    
    def actualizar_score(self):
         self.score+= 50
    
    def verificar_colision_bala(self, lista_ast):
        for bala in self.balas:
            for asteroide in lista_ast:
                if  bala.verificar_colision_asteroide(asteroide):
                    asteroide.asteroide_rect.x = 1300
                    asteroide.asteroide_rect.y = random.randrange(0,700,70)
                    asteroide.velocidad+=random.randrange(0,5,1)
                    bala.disparo_rect.x = 1400
                    self.actualizar_score()
           
    def actualizar_movimientoY(self,mov_y):
         new_y = self.col_rect.y+ mov_y
         if new_y > 90 and new_y < 650:
               self.col_rect.y+= mov_y
               self.nave_rect.y+= mov_y

    def actualizar_movimientoX(self,mov_x):
         new_x = self.col_rect.x+ mov_x
         if new_x > 1100 and new_x < 1160:
               self.col_rect.x+= mov_x
               self.nave_rect.x+= mov_x


               