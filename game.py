import pygame
import random
def main():
    pygame.init()
    screen = pygame.display.set_mode([500,500])
    pygame.display.set_caption("My game","jueguito")

    ventana = True
    posX = random.randint(0,500)
    posY = random.randint(0,500)
    posZ = random.randint(0,500)
    posW = random.randint(0,500)

    while(ventana):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                ventana = False
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
        posX = posX + random.randint(-1,1)        
        posY = posY + random.randint(-1,1)
        posZ = posZ + random.randint(-1,1)
        posW = posW + random.randint(-1,1)

        if posX < 0 or posW < 0:
            posX = 0
            posW = 0
        elif posX > 500 or posZ > 500:
            posX = 500
            posZ = 500
        if posY < 0 or posW < 0:
            posY = 0
            posW = 0
        elif posY > 500 or posZ > 500:
            posY = 500
            posZ = 500


        screen.fill((124,252,0))
        pygame.draw.circle(screen,(255,0,0),(posX,posY),5)
        pygame.draw.circle(screen,(255,0,0),(posX,posY),5)
        pygame.draw.circle(screen,(255,0,0),(posZ,posW),5)
        pygame.draw.circle(screen,(255,0,0),(posZ,posW),5)
        pygame.draw.circle(screen,(0,0,255),mouse,10)
        pygame.display.flip()
    pygame.quit()

main()