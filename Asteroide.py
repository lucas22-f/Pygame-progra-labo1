import pygame
import random
class Asteroide:
    def __init__(self,x,y) -> None:
        #Asteroide
        self.asteroide_imagen = pygame.image.load("roca.png")
        self.asteroide_rect = self.asteroide_imagen.get_rect()
        self.asteroide_rect.x = x
        self.asteroide_rect.y = y
        self.visible = True
        self.velocidad = random.randrange(1,50,2)

    def crear_lista_ast(cant):
        lista_ast = []
        for i in range(cant):
            rand_y = random.randrange(0,600,70)
            rand_x = random.randrange(-1000,0,70)
            lista_ast.append(Asteroide(rand_x,rand_y))
        return lista_ast

    def actualizar(lista_ast):
        for ast in lista_ast:   
            rect_ast = ast.asteroide_rect
            rect_ast.x = rect_ast.x + ast.velocidad
            
    
    def actualizar_pantalla(lista_ast,nave,screen):
        for ast in lista_ast:   
            if nave.nave_rect.colliderect(ast.asteroide_rect):
                nave.nave_visible = False
            pygame.draw.rect(screen,(250,0,0),ast.asteroide_rect)
            screen.blit(ast.asteroide_imagen,ast.asteroide_rect)

    