import sys, pygame
from pygame.locals import *
import random
import time 


WIDTH = 1048
HEIGHT = 480
class jugador(pygame.sprite.Sprite):
	def __init__(self):
                
		self.imagen1=pygame.image.load("a-1.png").convert_alpha()
		self.imagen2=pygame.image.load("a-2.png").convert_alpha()
		self.imagen3=pygame.image.load("a-3.png").convert_alpha()
		self.imagen4=pygame.image.load("a-4.png").convert_alpha()
		self.imagen5=pygame.image.load("a-5.png").convert_alpha()
		self.imagen6=pygame.image.load("a-6.png").convert_alpha()
		self.imagenes=[self.imagen1,self.imagen2,self.imagen3,self.imagen4,self.imagen5,self.imagen6]
		self.actual=0
		self.imagen=self.imagenes[0]
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=(250,100)
		#self.estamoviendo=False
		#self.orientacion=0
		
	def mover (self,x,y):
		self.rect.move_ip(x,y)
		self.imagen1=pygame.image.load("a-1.png").convert_alpha()
		self.imagen2=pygame.image.load("a-2.png").convert_alpha()
		self.imagen3=pygame.image.load("a-3.png").convert_alpha()
		self.imagen4=pygame.image.load("a-4.png").convert_alpha()
		self.imagen5=pygame.image.load("a-5.png").convert_alpha()
		self.imagen6=pygame.image.load("a-6.png").convert_alpha()

	def mostrar(self,screen,a,an,t,sonido):
		#print ("entro e.e")
		#if (x,y)==(0,0):
		#	self.estamoviendo=False
		#else:
		#	self.estamoviendo=True
		
		#if self.actual>(len(self.imagenes)-1):
		#	self.actual=0
		
		if t==1:
			self.siguiente(sonido)
		
		
		self.imagen=self.imagenes[self.actual]
		screen.blit(self.imagen,(a,an))
	def siguiente(self,sonido):
		sonido.play()
		
		self.actual+=1
		if self.actual>(len(self.imagenes)-1):
			self.actual=0
	def girar(self,pygame):
		print (pygame)
		pygame.transform.flip(self.imagen,False,True)
def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("juego")	
	#imagen=pygame.image.load("a-2.png")
	#sprite1 = pygame.sprite.Sprite()
	#sprite1.image = imagen
	fondo=pygame.image.load("fondo.jpg")
	fondo=pygame.transform.flip(fondo, True, False)
	#screen.blit(fondo,(0,0))
	#screen.blit(imagen,(30,30))

	reloj = pygame.time.Clock()
	t=0
	j1=jugador()
	j2=jugador()
	
	
	
	pygame.mixer.music.load("musica.mp3")
	sonido = pygame.mixer.Sound("golpe.wav")
	pygame.mixer.music.play(1)
	#sonido.play()
	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
		reloj.tick(5)
		t=t+1
		if t>1:
			t=0
			
			
		if event.type==pygame.KEYDOWN:
			if event.key in [pygame.K_UP,pygame.K_DOWN]:
				pygame.transform.flip(fondo, True, False)
			
		
		screen.fill((0,0,0))
		screen.blit(fondo,(0,0))
		#screen.blit(sprite1.image,(100,100))
		#x,y = pygame.mouse.get_pos()
		#print ("",x,"",y)
		#reloj.tick(25)
		
		j2.mostrar(screen,500,220,t,sonido)
		j1.mostrar(screen,329,220,t,sonido)
		#j2.girar("pygame")
		
		pygame.display.update()
		pygame.display.flip()
            
	return 0

        



if __name__ == '__main__':
	pygame.init()
	main()
