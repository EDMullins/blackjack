#CS 225
#Ethan Mullins
#Top-Down version of Blackjack

'''1 2 3 4 5 6 7 8 9 10 Jack Queen King Ace'''

'''
    1. get random card for user and dealer
    2. ask user, stand or call (repeat until hand is over 21 or user stands)
    3. repeat steps for dealers hand
    4. compare user and dealers hand to decide winner
'''
import pygame
import random

def main():
    pygame.init()
    
    pygame.display.set_mode((400,500))
    card_id = random.randint(1, 14)
    
    running = True
    #Game Loop
    while True:
        screen.fill((30,180,20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    
        #events() #will have 2 buttons for hit and stand, and maybe a quit button
        #loop() #will have 14 images of cards to render in and display at different parts of the screen
        #render() #prints out screen graphics
    
    

main()