import pygame
import random
class Disparo:

    def __init__(self,x,y,enemy="") -> None:
        self.superficie_bala = pygame.Surface((10,5))
        self.superficie_bala.fill("White")
        self.imagen = pygame.image.load("./images/bullet.png")
        self.imagen = pygame.transform.scale(self.imagen,(35,15))
        self.e_imagen = pygame.image.load("./images/e_bullet.png")
        self.e_imagen = pygame.transform.scale(self.e_imagen,(100,55))
        self.disparo_rect = self.imagen.get_rect()
        self.disparo_rect.y = y
        self.disparo_rect.x = x
        self.disparo_e_rect = pygame.Rect(x+50,y+25,20,10)
        self.disparo_daño = 25
        self.enemy = enemy
        self.direccion = "izquierda"

    def mover(self):
        if self.enemy:
            self.disparo_rect.x += 15
            self.disparo_e_rect.x += 15
        else:
             self.disparo_rect.x -= 15
             self.disparo_e_rect.x -= 15
     

    def verificar_colision_asteroide(self, asteroide):
        if self.disparo_rect.colliderect(asteroide.asteroide_rect):
            return True
        return False

    
                
               
 
        

       
            
    
        
            