import pygame
import random
class Asteroide:
    def __init__(self,x,y) -> None:
        #Asteroide
        self.asteroide_imagen = pygame.image.load("roca.png")
        self.asteroide_rect = self.asteroide_imagen.get_rect()
        self.asteroide_rect.x = x
        self.asteroide_rect.y = y
        self.velocidad = random.randrange(1,2,2)
        self.vida = 100
        self.daño = 20

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
                rect_ast.y = random.randrange(0,700,82)
            
    def actualizar_pantalla(lista_ast,screen):
        for ast in lista_ast:
            pygame.draw.rect(screen,(250,0,0),ast.asteroide_rect) 
            screen.blit(ast.asteroide_imagen,ast.asteroide_rect)

    def crear_lista_colisionados(lista_ast):
        lista_colisionados = []
        for e in range(len(lista_ast)):
            lista_colisionados.append(False)
        return lista_colisionados

    def verificar_colision(lista_ast,lista_colisionados,nave):
        for i,ast in enumerate(lista_ast):
            if not lista_colisionados[i] and nave.nave_rect.colliderect(ast.asteroide_rect):#verifica en mi lista de colisionados si no fue colisionado 
                #anteriormente para que al ejecutarse la colision se ejecute este bloque de codigo 1 vez
                lista_colisionados[i] = True
                nave.nave_vida-=ast.daño
                if nave.nave_vida <=0:
                    nave.nave_visible = False
                print(f"vida nave : {nave.nave_vida}")
                print(f"colision con el asteroide: {i+1} ") 
            if ast.asteroide_rect.right < 0 or ast.asteroide_rect.left > 1230 or ast.asteroide_rect.bottom < 0 or ast.asteroide_rect.top > 700:
                lista_colisionados[i] = False

               
                   
                    
                    
            
            
        

    