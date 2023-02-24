import pygame, sys, random

#------------colours-------------------------------#

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

#-------------first-vars----------------------#

pygame.init()
screen_width=800
screen_height=500
size=(screen_width, screen_height)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Game")

player=pygame.image.load("bro.png").convert()
player.set_colorkey(WHITE)

pygame.display.set_icon(player)
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)
coord_list=[]

player_x=150
player_y=298

cactus_x=700
cactus_y=330

player_speed=0
cactus_speed=10

allow_input=True

#-----------logic-----------------------------------------#

cactus=pygame.image.load("cactus.png").convert()
clouds=pygame.image.load("clouds.png").convert()
cactus.set_colorkey(WHITE)

for i in range(200):

	x=random.randint(0, 800)
	y=random.randint(410, 800)
	coord_list.append([x,y])

while True:

	for event in pygame.event.get():

		if event.type==pygame.QUIT:

			sys.exit()

		elif event.type==pygame.KEYDOWN:
	
			if event.key==pygame.K_SPACE:

				if allow_input:
					
					player_speed-=10
					allow_input=False
					pygame.time.set_timer(pygame.USEREVENT, 2000)

		elif event.type==pygame.USEREVENT:
		
			allow_input=True													

	player_y+=player_speed

	if player_y<=160:

		player_speed*=-1

	elif player_y==298:

		player_speed*=0
			
	cactus_x-=cactus_speed	

	if cactus_x==-10:

		cactus_x=800

#----------drawing-zone-------------------------------------#

	screen.fill(WHITE)	
	screen.blit(player, [player_x, player_y])
	screen.blit(cactus, [cactus_x, cactus_y])
	screen.blit(clouds, [40, 10])
	
	pygame.draw.line(screen, BLACK, [800,400], [0,400], 5)
	pygame.draw.circle(screen, BLACK, (600,90), 30)	

	for coord in coord_list:

		x=coord[0]
		y=coord[1]
		pygame.draw.circle(screen, BLACK, coord, 3)

#-----------end-of-drawing-and-logic-zone-----------------#
	
	pygame.display.flip()
	clock.tick(15)

pygame.quit()	