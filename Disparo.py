import pygame
import random
class Disparo:

    def __init__(self,x,y) -> None:
        self.superficie_bala = pygame.Surface((10,5))
        self.superficie_bala.fill("White")
        self.imagen = pygame.image.load("misil.png")
        self.imagen = pygame.transform.scale(self.imagen,(55,25))
        self.disparo_rect = self.imagen.get_rect()
        self.disparo_rect.y = y
        self.disparo_rect.x = x
        self.disparo_daño = 25

    def mover(self):
        self.disparo_rect.x -= 10

    def verificar_colision_asteroide(self, asteroide):
        if self.disparo_rect.colliderect(asteroide.asteroide_rect):
            return True
        return False

    
                
               
 
        

       
            
    
        
            