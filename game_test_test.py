# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 720
Y = 720
 
# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
# create a surface object, image is drawn on it.
cards = [r"C:\Users\ethan\Desktop\Projects\Python\blackjack\one_card.png", r"C:\Users\ethan\Desktop\Projects\Python\blackjack\two_card.png", r"C:\Users\ethan\Desktop\Projects\Python\blackjack\three_card.png"]

screen.fill((255, 255, 255))

card_queue = []
# Using blit to copy content from one surface to other
for card in cards:
	card_queue.append(pygame.image.load(card).convert())

for length in range(len(cards)):
	#card algorithm is [(screen_width / 2) - ((num_cards / 2) * card_width) + (card_index * card_width)]
	screen.blit(card_queue[length], ((360-((len(cards)/2)*100)+(length * 75)), 300))
 
# paint screen one time
pygame.display.flip()
running = True
while running:
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for ev in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if ev.type == pygame.QUIT:
            running = False
 
# deactivates the pygame library
pygame.quit()