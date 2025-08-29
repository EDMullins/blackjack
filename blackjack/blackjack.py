import pygame 
import sys
import random 

'''
To-Do
1. fix timing like 1 second before the dealer pulls his next card
1. Beautify, fix colors maybe new font and mess with spacing
2. Try to do classes
'''

#After the game loop I need to have another loop to display the Dealers turn which happens automatically but same logic and they always stops at 16
#Then I need to test users score to see if they won or not
def end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text, dealer_back_card):
	#flips the backwards card given to the dealer before the loop runs because I need to only run once
	dealer_card_queue[0] = pygame.image.load(cards[dealer_back_card]).convert()
	if dealer_back_card < 11:
		dealer_card_total += dealer_back_card
	elif dealer_back_card == 11 or dealer_back_card == 12 or dealer_back_card == 13:
		dealer_card_total += 10
	elif dealer_back_card == 14:
		# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
		if dealer_card_total + 11 > 21:
			dealer_card_total += 1
		else:
			dealer_card_total += 11
	
	#Updates the text for the card total
	dealer_card_total_text = smallfont.render('Total: '+str(dealer_card_total), True, white)
	while True:
		#self explanatory 
		win_text = smallfont.render('You Win', True, white)
		push_text = smallfont.render('Push', True, white)
		lose_text = smallfont.render('You Lost', True, white)
		replay_text = smallfont.render('Replay', True, white)
		quit_text = smallfont.render('Quit', True, white)
		
		#I want to wait a little bit before drawing each card
		pygame.time.wait(50)
		
		#Dealers turn logic after stand is hit
		if player_card_total <= 21:
			if dealer_card_total <= 16:
				if card_key < 11:
					dealer_card_total += card_key
				elif card_key == 11 or card_key == 12 or card_key == 13:
					dealer_card_total += 10
				elif card_key == 14:
					# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
					if dealer_card_total + 11 > 21:
						dealer_card_total += 1
					else:
						dealer_card_total += 11
					
				dealer_card_total_text = smallfont.render('Total: '+str(dealer_card_total), True, white)
				dealer_card_queue.append(pygame.image.load(cards[card_key]).convert())
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
		
		#displays dealers cards and total
		for card_index in range(len(dealer_card_queue)):
			screen.blit(dealer_card_queue[card_index], ((360-((len(dealer_card_queue)/2)*100)+(card_index * 75)), 50))
		screen.blit(dealer_card_total_text, (width-150, height-440))
		
		#displays players card and total
		for card_index in range(len(player_card_queue)):
			screen.blit(player_card_queue[card_index], ((360-((len(player_card_queue)/2)*100)+(card_index * 75)), 450))
		screen.blit(player_card_total_text, (width-150, height-320))
		
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
	cards = {1: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\one_card.png", 2: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\two_card.png",
			3: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\three_card.png", 4: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\four_card.png",
			5: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\five_card.png", 6: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\six_card.png",
			7: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\seven_card.png", 8: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\eight_card.png",
			9: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\nine_card.png", 10: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\ten_card.png",
			11: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\jack_card.png", 12: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\queen_card.png",
			13: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\king_card.png", 14: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\ace_card.png", 
			15: r"C:\Users\ethan\Desktop\Projects\blackjack\imgs\back_card.png"}
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
				player_card_queue.append(pygame.image.load(cards[card_key]).convert())
				card_key = random.randint(1, 14)
				i += 1
			i = 0
			#take the loop out and make the first card drawn still affect the total but make it backwards
			#get a temporary variable to hold the value of the card being turned around and when stand is hit I need to change the queue to the original card
			#then I need to update the total with the new value
			dealer_back_card = card_key
			dealer_card_queue.append(pygame.image.load(cards[15]).convert())
			card_key = random.randint(1, 14)
				
			if card_key < 11:
				dealer_card_total += card_key
			elif card_key == 11 or card_key == 12 or card_key == 13:
				dealer_card_total += 10
			elif card_key == 14:
				# Ace card logic for the different values I would do a button but I suck so maybe I'll come back to it
				if dealer_card_total + 11 > 21:
					dealer_card_total += 1
				else:
					dealer_card_total += 11
						
			dealer_card_total_text = smallfont.render('Total: ' + str(dealer_card_total), True, white)
			#adds the card to card_queue
			dealer_card_queue.append(pygame.image.load(cards[card_key]).convert())
			card_key = random.randint(1, 14)	
				
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
					end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text, dealer_back_card)
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
					player_card_queue.append(pygame.image.load(cards[card_key]).convert())
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
		
		#Displays the cards for player
		for card_index in range(len(player_card_queue)):
			screen.blit(player_card_queue[card_index], ((360-((len(player_card_queue)/2)*100)+(card_index * 75)), 450))
		#Displays the total values of all cards obtained
		screen.blit(player_card_total_text, (width-150, height-320))
		
		#Displays the cards for dealer
		for card_index in range(len(dealer_card_queue)):
			screen.blit(dealer_card_queue[card_index], ((360-((len(dealer_card_queue)/2)*100)+(card_index * 75)), 50))
		#Displays the total values of all cards obtained
		screen.blit(dealer_card_total_text, (width-150, height-440))
		
		if player_card_total > 21:
			end(screen, smallfont, white, color_light, color_dark, width, height, mouse, cards, card_key, player_card_queue, player_card_total, player_card_total_text, dealer_card_queue, dealer_card_total, dealer_card_total_text, dealer_back_card) 
		# updates the frames of the game 
		pygame.display.update()

#startin the game
main()