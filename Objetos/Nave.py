import random
import pygame
from Objetos.Disparo import Disparo
from Objetos.Asteroide import Asteroide
pygame.mixer.init()

rock= pygame.mixer.Sound("./sounds/rock_coll.mp3")
rock.set_volume(0.1)
rock.play()
rock.stop()


sound = pygame.mixer.Sound("./sounds/disp.mp3")
sound.set_volume(0.8)
sound.play()
sound.stop()

golpe_bala = pygame.mixer.Sound("./sounds/golpe_bala.mp3")
golpe_bala.set_volume(0.1)
golpe_bala.play()
golpe_bala.stop()

class Nave:
    def __init__(self) -> None:
        self.nave_imagen = pygame.image.load("./images/nave.png")
        self.nave_imagen = pygame.transform.scale(self.nave_imagen,(120,70))
        self.nave_rect = self.nave_imagen.get_rect()
        self.nave_rect.x = 1100
        self.nave_rect.y = 300
        self.col_rect =pygame.Rect(1050+60,300+20,100,40)
        self.colision = False
        self.nave_visible = True
        self.nave_vivo = True
        self.nave_vida = 300
        self.balas = []
        self.score = 0
        self.contador = 0
       

    def actualizar(self,screen,enemigo):
            
            if self.nave_visible:
                screen.blit(self.nave_imagen,self.nave_rect)
            for i,balas in enumerate(self.balas):
                balas.mover()
                #pygame.draw.rect(screen,"White",balas.disparo_rect)
                screen.blit(balas.imagen, balas.disparo_rect)
                
                if self.verificar_colision_nave_enemigo(balas,enemigo):
                    golpe_bala.play()
                    enemigo.nave_vida-=30
                 
                    balas.disparo_rect.x = 1400
                    if enemigo.nave_vida <=0:
                         self.score+=300
                    
                    #print("colisiono")
                    #print(enemigo.nave_vida)
                    
                
                if balas.disparo_rect.x < -10 or balas.disparo_rect.x > 1330:
                    self.balas.pop(i)
                    
    def disparar(self):
       
        if self.nave_vivo:
            
            bala = Disparo(self.nave_rect.centerx,self.nave_rect.centery,False)
            sound.play()
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
                    rock.play()
                    asteroide.asteroide_rect.x = 1300
                    asteroide.asteroide_rect.y = random.randrange(0,700,70)
                    asteroide.velocidad+=random.randrange(0,5,1)
                    bala.disparo_rect.x = 1400
                    self.actualizar_score()

    def verificar_colision_nave_enemigo(self,bala,enemigo):
        if enemigo.col_rect.colliderect(bala.disparo_rect):
            return True
        return False
       
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


               