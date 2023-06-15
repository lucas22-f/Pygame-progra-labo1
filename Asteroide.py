import pygame
import random
class Asteroide:
    def __init__(self,x,y) -> None:
        #Asteroide
        self.asteroide_imagen = pygame.image.load("./imagenes/roca.png")
        self.asteroide_rect = self.asteroide_imagen.get_rect()
        self.asteroide_rect.x = x
        self.asteroide_rect.y = y
        self.velocidad = random.randrange(1,10,2)
        self.daño = 50
        

    def crear_lista_ast(cant):
        lista_ast = []
        for i in range(cant):
            rand_y = random.randrange(0,700,70)
            rand_x = random.randrange(-1000,-20,70)
            lista_ast.append(Asteroide(rand_x,rand_y))
        return lista_ast

    def actualizar(lista_ast):
        for ast in lista_ast:   
            rect_ast = ast.asteroide_rect
            rect_ast.x = rect_ast.x + ast.velocidad
            rect_ast.y = rect_ast.y + random.randrange(-1,2,1)
            if rect_ast.x > 1230:
                rect_ast.x = random.randrange(-300,0,82)
                rect_ast.y = random.randrange(50,650,82)
            
    def actualizar_pantalla(lista_ast,screen):
        for ast in lista_ast:
            
            screen.blit(ast.asteroide_imagen,ast.asteroide_rect)

    def crear_lista_colisionados(lista_ast):
        
        lista_colisionados = []
        for e in range(len(lista_ast)):
            lista_colisionados.append(False)
        return lista_colisionados

    def verificar_colision(lista_ast,lista_colisionados,nave):
        for i,ast in enumerate(lista_ast):
            if not lista_colisionados[i] and nave.col_rect.colliderect(ast.asteroide_rect):#verifica en mi lista de colisionados si no fue colisionado 
                #anteriormente para que al ejecutarse la colision se ejecute este bloque de codigo 1 vez
                lista_colisionados[i] = True
                nave.nave_vida-=ast.daño
                ast.asteroide_rect.x = 1300
                if nave.nave_vida <=0:
                    nave.nave_visible = False
                    nave.nave_vivo = False
                    nave.nave_vida = 0
                    nave.col_rect.x = 1400
                    
                    
            if ast.asteroide_rect.x > 1230:
                lista_colisionados[i] = False

               
                   
                    
                    
            
            
        

    