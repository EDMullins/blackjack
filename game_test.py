import pygame 
import sys
import random 


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (720,720) 

# opens up a window 
screen = pygame.display.set_mode(res) 

# white color 
white = (255,255,255) 

# light shade of the button 
color_light = (170,170,170) 

# dark shade of the button 
color_dark = (100,100,100) 

# stores the width of the screen into a variable 
width = screen.get_width() 

# stores the height of the screen into a variable 
height = screen.get_height() 

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

# rendering my text 
hit_text = smallfont.render('Hit' , True , white) 
stand_text = smallfont.render('Stand', True, white)

cards = {1: '1', 2: '2', 3: '3',
		4: '4', 5: '5', 6: '6',
		7: '7', 8: '8', 9: '9',
		10: '10', 11: 'Jack', 12: 'Queen',
		13: 'King', 14: 'Ace'}
card_key = random.randint(1, 14)
card_queue = []
card_total = 0
card_total_text = smallfont.render('', True, white)

running = True

while running:
	for ev in pygame.event.get(): 
		mouse = pygame.mouse.get_pos() 
		if ev.type == pygame.QUIT:
			pygame.quit() 
		if ev.type == pygame.MOUSEBUTTONUP: 	
			#proccessing the mouse clicks 
			if width-150 <= mouse[0] <= width-10 and height-50 <= mouse[1] <= height-10:
				stand_press = True
			if width-300 <= mouse[0] <= width-160 and height-50 <= mouse[1] <= height-10:
				#finds the value of the card and stores it in card_total
				if card_key < 11:
					card_total += card_key
				elif card_key == 11 or card_key == 12 or card_key == 13 or card_key == 14:
					card_total += 10
				card_total_text = smallfont.render(str(card_total), True, white)
				#adds the card to card_queue
				card_queue.append(smallfont.render(cards[card_key], True, white))
				card_key = random.randint(1, 14)
	
	
	#Everything below controls the visual aspect of my game
	screen.fill((40,160,40)) 
	
	# stores the (x,y) coordinates into 
	# the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
	# if mouse is hovered on a button it 
	# changes to lighter shade 
	if width-150 <= mouse[0] <= width-10 and height-50 <= mouse[1] <= height-10: 
		pygame.draw.rect(screen,color_light,[width-150, height-50, 140,40]) 
		
	else: 
		pygame.draw.rect(screen,color_dark,[width-150, height-50 ,140,40]) 
	if width-300 <= mouse[0] <= width-160 and height-50 <= mouse[1] <= height:
		pygame.draw.rect(screen, color_light,[width-300, height-50, 140, 40])
	else:
		pygame.draw.rect(screen, color_dark,[width-300, height-50, 140, 40])
	
	# superimposing the text onto our button 
	screen.blit(hit_text, (width-245, height-45))
	screen.blit(stand_text , (width-115, height-45))	
    
	#Displays the last card added to card queue (will eventually need to loop through my card_queue when I start displaying multiple cards at a time)
	if len(card_queue) != 0:
		screen.blit(card_queue[-1], (width/2, height/2))
    
	#Displays the total values of all cards obtained
	screen.blit(card_total_text, (width-40, height/2))
	# updates the frames of the game 
	pygame.display.update()  
