import pygame

class Nave:
    def __init__(self) -> None:
        
        self.nave_imagen = pygame.image.load("nave.png")
        self.nave_imagen = pygame.transform.scale(self.nave_imagen,(120,70))
        self.nave_rect = self.nave_imagen.get_rect()
        self.nave_rect.x = 1100
        self.nave_rect.y = 300
        self.nave_visible = True

    def actualizar(self,screen):
            if self.nave_visible:
                pygame.draw.rect(screen,(0,250,0),self.nave_rect)
                screen.blit(self.nave_imagen,self.nave_rect)

    def actualizar_movimientoY(self,mov_y):
         new_y = self.nave_rect.y+ mov_y
         if new_y > 0 and new_y < 650:
               self.nave_rect.y+= mov_y

    def actualizar_movimientoX(self,mov_x):
         new_x = self.nave_rect.x+ mov_x
         if new_x > 0 and new_x < 1160:
               self.nave_rect.x+= mov_x