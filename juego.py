import random
import pygame
from pygame.locals import *
import sys
import time
import random



WIDTH = 1048
HEIGHT = 480
pygame.init()
class jugador:
    def __init__(self,n):
        self.nombre=n
        self.vida=30
        self.at=0
        self.df=0
        
    def ataque (self):
        a=random.randint(1,7)
        atc=0
        if a>=1 and a<=2:
            atc=1
            print("1 de daño")
        if a>=3 and a<=4:
            atc=5
            print("5 de daño")
        if a>=5 and a<=6:
            atc=10
            print("10 de daño")
        if a==7:
            atc=15
            print("15 de daño")

        return atc



    def defenza(self,ataq):
        d=random.randint(1,7)
        df=0
        if d>=1 and d<=2:
            df=ataq
            print("todo el daño ",df)
        if d>=3 and d<=4:
            df=ataq/2
            print("mitad de daño",df)
        if d>=5 and d<=6:
            df=ataq*0.25
            print("un cuarto de daño ",df)
        if d==7:
            df=0
            print("nada de daño ",df)

        self.vida=self.vida-df
   
        
    
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego")
    pygame.mixer.music.load("musica.mp3")
    fondo=pygame.image.load("fondo.jpg")
    reloj = pygame.time.Clock()
    pygame.mixer.music.play(1)
    sonido = pygame.mixer.Sound("golpe.wav")
    victoriar = pygame.mixer.Sound("vic.wav")
    
 
    parado=pygame.image.load("a-1.png").convert_alpha()
    escudo=pygame.image.load("a-2.png").convert_alpha()
    golpe=pygame.image.load("a-3.png").convert_alpha()
    critico=pygame.image.load("a-4.png").convert_alpha()
    muerto=pygame.image.load("a-5.png").convert_alpha()
    victoria=pygame.image.load("a-6.png").convert_alpha()


    parado2=pygame.image.load("a-1.png").convert_alpha()
    escudo2=pygame.image.load("a-2.png").convert_alpha()
    golpe2=pygame.image.load("a-3.png").convert_alpha()
    critico2=pygame.image.load("a-4.png").convert_alpha()
    muerto2=pygame.image.load("a-5.png").convert_alpha()
    victoria2=pygame.image.load("a-6.png").convert_alpha()
    golpe2=pygame.transform.flip(golpe2, True, False)
    parado2=pygame.transform.flip(parado2, True, False)
    escudo2=pygame.transform.flip(escudo2, True, False)
    critico2=pygame.transform.flip(critico2, True, False)
    muerto2=pygame.transform.flip(muerto2, True, False)
    victoria2=pygame.transform.flip(victoria2, True, False)
  

    j1=jugador("pablo")
    j2=jugador("pedro")

    screen.blit(fondo,(0,0))
    screen.blit(parado,(320,220))
    screen.blit(parado2,(450,220))
    
    pygame.display.flip()
    time.sleep(1.95)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        reloj.tick(5)
        while j1.vida>0 and j2.vida>0:
            at1=j1.ataque()
            at2=j2.ataque()
            screen.blit(fondo,(0,0))
            pygame.display.flip()
            
            
                
            j2.defenza(at1)
            if at1>10:
                screen.blit(critico2,(450,220))
                pygame.display.flip()
            
            screen.blit(golpe,(320,220))
            screen.blit(escudo2,(450,220))
            sonido.play()
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(fondo,(0,0))
            j1.defenza(at2)
            if at2>10:
                screen.blit(critico,(320,220))
                pygame.display.flip()

            
            screen.blit(golpe2,(450,220))
            screen.blit(escudo,(320,220))
            sonido.play()
            pygame.display.flip()
            time.sleep(0.5)

    
            pygame.display.update()
            pygame.display.flip()
            screen.blit(fondo,(0,0))

            
            print (j1.vida)
            print (j2.vida)

        pygame.display.update()
        pygame.display.flip()
        screen.blit(fondo,(0,0))
        if j1.vida>j2.vida:
            pygame.mixer.music.stop()
            
            screen.blit(victoria,(320,220))
            screen.blit(muerto2,(450,250))
            victoriar.play()
            time.sleep(0.5)
            victoriar.stop()
        else:
            pygame.mixer.music.stop()
            
            screen.blit(victoria2,(450,250))
            screen.blit(muerto,(320,220))
            victoriar.play()
            time.sleep(0.5)
            victoriar.stop()
        
    return 0
    


if __name__ == '__main__':
	pygame.init()
	main()
