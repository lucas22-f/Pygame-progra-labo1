import random

import pygame
from Disparo import Disparo


class Enemy:
    def __init__(self) -> None:
        self.nave_imagen = pygame.image.load("./imagenes/enemy.png")
        self.nave_rect = self.nave_imagen.get_rect()
        self.nave_rect.x = 100
        self.nave_rect.y = 300
        self.col_rect =pygame.Rect(self.nave_rect.x+50, self.nave_rect.y+40,200,60)
        self.colision = False
        self.nave_visible = True
        self.nave_vivo = True
        self.nave_vida = 500
        self.direccion = "abajo"
        self.balas = []
        self.velocidad = 1
    
        

    def actualizar_enemy(self,screen,nave):
        if self.nave_vida > 0:
            barra_vida = pygame.Surface((self.nave_vida,10))
            barra_vida.fill("Red")
            #pygame.draw.rect(screen,(255,0,0),self.col_rect)
            screen.blit(barra_vida,self.nave_rect)
            screen.blit(self.nave_imagen,self.nave_rect)
        else:
            self.nave_rect.y = 900
            self.col_rect.y = 900
            if nave.score > 2000 and nave.score <3000:
                self.nave_vida = 500
                self.nave_rect.y = 300
                self.col_rect.y = 350
                self.velocidad = 3 
            elif nave.score > 4700 and nave.score <5500:
                self.nave_vida = 700
                self.nave_rect.y = 300
                self.col_rect.y = 350
                self.velocidad = 5
            elif nave.score > 7000:
                self.nave_vida = 1000
                self.nave_rect.y = 300
                self.col_rect.y = 350
                self.velocidad = 7
        self.mover_enemy()
  
        for i,e in enumerate(self.balas):
            e.mover()
            screen.blit(e.e_imagen,e.disparo_rect)
            #pygame.draw.rect(screen,"Green",nave.col_rect)
            #pygame.draw.rect(screen,"White",e.disparo_e_rect)
            
            if self.verificar_colision_bala_enemigo(nave,e):
                nave.nave_vida-=20
                if nave.nave_vida <=0:
                    nave.nave_visible = False
                    nave.nave_vivo = False
                    nave.nave_vida = 0
                    nave.col_rect.x = 1400
                self.balas.pop(i)
            if e.disparo_rect.x > 1339  or e.disparo_rect.x < -10:
                    self.balas.pop(i)
                    #print(len(self.balas))

    def imprimir_enemigo(self,enemigos,screen,nave):
        for enemigo in enemigos:
            enemigo.actualizar_enemy(screen, nave)

       


    def verificar_colision_bala_enemigo(self,nave,bala):
        if nave.col_rect.colliderect(bala.disparo_e_rect):
            return True
        return False

    def disparar_enemy(self):
        bala = Disparo(self.nave_rect.centerx,self.nave_rect.centery,True)
        self.balas.append(bala)  

    def mover_enemy(self):
        if self.direccion == "abajo":
            if self.nave_rect.y < 600:
                self.nave_rect.y+=self.velocidad
                self.col_rect.y+=self.velocidad
            else:
                self.direccion = "arriba"
        elif  self.direccion == "arriba":
            if self.nave_rect.y > 0:
                self.nave_rect.y-=self.velocidad
                self.col_rect.y-=self.velocidad
            else:
                self.direccion = "abajo"

