import pygame
import random
class Disparo:

    def __init__(self,x,y) -> None:
        self.superficie_bala = pygame.Surface((10,5))
        self.superficie_bala.fill("White")
        self.disparo_rect = self.superficie_bala.get_rect()
        self.disparo_rect.y = y
        self.disparo_rect.x = x
       

    def mover(self):
        self.disparo_rect.x -= 5
       
    
        
            