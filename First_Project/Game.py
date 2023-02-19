import pygame, sys

#------------colours-------------------------------#

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

#-------------first-vars----------------------#

pygame.init()
size=(800, 500)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()

#-----------logic-----------------------------#

while True:

	for event in pygame.event.get():

		if event.type==pygame.QUIT:

			sys.exit()



#----------drawing-zone---------------------#

	screen.fill(WHITE)		

#-----------end-of-drawing-zone-----------------#
	
	pygame.display.flip()
	clock.tick(60)