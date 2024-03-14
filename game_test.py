import pygame 
import sys
import random 

'''
To-Do
1. get images working and then I can show all the cards at once
2. Make sure only to show the second card that the dealer gets until player stands and only show the total of the one card shown
'''

#After the game loop I need to have another loop to display the Dealers turn which happens automatically but same logic and he always stops at 16
#Then I need to test users score to see if they won or not
def end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text):
	while True:
		#self explanatory 
		win_text = smallfont.render('You Win', True, white)
		push_text = smallfont.render('Push', True, white)
		lose_text = smallfont.render('You Lost', True, white)
		replay_text = smallfont.render('Replay', True, white)
		quit_text = smallfont.render('Quit', True, white)
		
		#Dealers turn logic after stand is hit
		if player_card_total <= 21:
			if dealer_card_total <= 16:
				if card_key < 11:
					dealer_card_total += card_key
				elif card_key == 11 or card_key == 12 or card_key == 13:
					dealer_card_total += 10
				elif card_key == 14:
					# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
					if player_card_total + 11 > 21:
						player_card_total += 1
					else:
						player_card_total += 11
					
				dealer_card_total_text = smallfont.render('Total: '+str(dealer_card_total), True, white)
				dealer_card_queue.append(smallfont.render(cards[card_key], True, white))
				card_key = random.randint(1, 14)
		
		#gets the events from the player
		for ev in pygame.event.get(): 
			mouse = pygame.mouse.get_pos() 
			if ev.type == pygame.QUIT:
				pygame.quit() 
			if ev.type == pygame.MOUSEBUTTONUP: 	
				#proccessing the mouse clicks the if statements are for each button
				if (width/2)-140 <= mouse[0] <= width/2 and (height/2)+40 <= mouse[1] <= (height/2)+80:
					main()
				if width/2 <= mouse[0] <= (width/2)+140 and (height/2)+40 <= mouse[1] <= (height/2)+80:
					pygame.quit()
		#Resests screen
		screen.fill((40,160,40))
		
		screen.blit(dealer_card_queue[-1], (width/2, height-650))
		screen.blit(dealer_card_total_text, (width-200, height-650))
		
		screen.blit(player_card_queue[-1], (width/2, height-225))
		screen.blit(player_card_total_text, (width-200, height-225))
		
		#Win or Lose logic
		if player_card_total > 21:
			screen.blit(lose_text, ((width/2)-60 ,height/2))
		elif player_card_total < dealer_card_total and dealer_card_total <= 21:
			screen.blit(lose_text, ((width/2)-60 ,height/2))
		elif player_card_total <= 21 and dealer_card_total > 21:
			screen.blit(win_text, ((width/2)-60 ,height/2))
		elif player_card_total <= 21 and player_card_total > dealer_card_total:
			screen.blit(win_text, ((width/2)-60 ,height/2))
		elif player_card_total == dealer_card_total:
			screen.blit(push_text, ((width/2)-60 ,height/2))
		
		#buttons for replay and quit
		if (width/2)-140 <= mouse[0] <= (width/2) and (height/2)+40 <= mouse[1] <= (height/2)+80: 
			pygame.draw.rect(screen,color_light,[(width/2)-140, (height/2)+40, 140,40]) 
		else: 
			pygame.draw.rect(screen,color_dark,[(width/2)-140, (height/2)+40 ,140,40])
		if (width/2) <= mouse[0] <= (width/2)+140 and (height/2)+40 <= mouse[1] <= (height/2)+80: 
			pygame.draw.rect(screen,color_light,[width/2, (height/2)+40, 140,40]) 
		else: 
			pygame.draw.rect(screen,color_dark,[width/2, (height/2)+40 ,140,40]) 
		screen.blit(replay_text, ((width/2)-120, (height/2)+40))
		screen.blit(quit_text, ((width/2)+35, (height/2)+40))
		
		pygame.display.update()

#Before my game loop starts I need to give the Player and the Dealer 2 cards and store those values in seperate totals
#Ok I know theres a better way to do this but I dont want to make tht complex of a loop for all 4 cards'''
		
#Game Logic	
def main():
	# initializing the constructor 
	pygame.init() 

	# screen resolution 
	res = (720,720) 

	# opens up a window 
	screen = pygame.display.set_mode(res) 

	# white color 
	white = (255,255,255) 

	# light shade of the buttons
	color_light = (170,170,170) 

	# dark shade of the buttons
	color_dark = (100,100,100) 

	# stores the width of the screen into a variable 
	width = screen.get_width() 

	# stores the height of the screen into a variable 
	height = screen.get_height() 

	# defining a font 
	smallfont = pygame.font.SysFont('Corbel',35) 

	# rendering my text for buttons
	hit_text = smallfont.render('Hit' , True , white) 
	stand_text = smallfont.render('Stand', True, white)

	# dict with all my cards that has the random card key as the key 
	cards = {1: '1', 2: '2', 3: '3',
			4: '4', 5: '5', 6: '6',
			7: '7', 8: '8', 9: '9',
			10: '10', 11: 'Jack', 12: 'Queen',
			13: 'King', 14: 'Ace'}
	card_key = random.randint(1, 14)

	#Players Card stuff
	player_card_queue = []
	player_card_total = 0
	player_card_total_text = smallfont.render('', True, white)

	#Dealers Card stuff
	dealer_card_queue = []
	dealer_card_total = 0
	dealer_card_total_text = smallfont.render('', True, white)
	
	running = True
	
	while running:
		#if the game just started then draw 2 cards for the dealer and player
		if player_card_total == 0:
			i = 0
			while i != 2:
				if card_key < 11:
					player_card_total += card_key
				elif card_key == 11 or card_key == 12 or card_key == 13:
					player_card_total += 10
				elif card_key == 14:
					# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
					if player_card_total + 11 > 21:
						player_card_total += 1
					else:
						player_card_total += 11
				player_card_total_text = smallfont.render('Total: ' + str(player_card_total), True, white)
				#adds the card to card_queue
				player_card_queue.append(smallfont.render(cards[card_key], True, white))
				card_key = random.randint(1, 14)
				i += 1
			i = 0
			while i != 2:
				if card_key < 11:
					dealer_card_total += card_key
				elif card_key == 11 or card_key == 12 or card_key == 13:
					dealer_card_total += 10
				elif card_key == 14:
					# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
					if player_card_total + 11 > 21:
						player_card_total += 1
					else:
						player_card_total += 11
						
				dealer_card_total_text = smallfont.render('Total: ' + str(dealer_card_total), True, white)
				#adds the card to card_queue
				dealer_card_queue.append(smallfont.render(cards[card_key], True, white))
				card_key = random.randint(1, 14)
				i += 1
		#gets the events
		for ev in pygame.event.get(): 
			mouse = pygame.mouse.get_pos() 
			if ev.type == pygame.QUIT:
				pygame.quit() 
			if ev.type == pygame.MOUSEBUTTONUP: 	
				#proccessing the mouse clicks the if statements are for each button
				if width-150 <= mouse[0] <= width-10 and height-50 <= mouse[1] <= height-10:
					#the stand button calls the end function which runs the dealers turn and the logic for the end screen
					pygame.display.update()
					end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text)
				if width-300 <= mouse[0] <= width-160 and height-50 <= mouse[1] <= height-10:
					#finds the value of the card and stores it in card_total
					if card_key < 11:
						player_card_total += card_key
					elif card_key == 11 or card_key == 12 or card_key == 13:
						player_card_total += 10
					elif card_key == 14:
						# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
						if player_card_total + 11 > 21:
							player_card_total += 1
						else:
							player_card_total += 11
							
					player_card_total_text = smallfont.render('Total: ' + str(player_card_total), True, white)
					#adds the card to card_queue
					player_card_queue.append(smallfont.render(cards[card_key], True, white))
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
		for card in player_card_queue:
			screen.blit(card, (width/2, height-225))
		#Displays the total values of all cards obtained
		screen.blit(player_card_total_text, (width-200, height-225))
		
		#Displaying Dealers card queue and Total value
		screen.blit(dealer_card_queue[-1], (width/2, height-650))
		screen.blit(dealer_card_total_text, (width-200, height-650))
		
		if player_card_total > 21:
			end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text) 
		# updates the frames of the game 
		pygame.display.update()

#startin the game
main()
