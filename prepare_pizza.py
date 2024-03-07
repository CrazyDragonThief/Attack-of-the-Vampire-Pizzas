#Set up game

#Import libraries
import pygame
from pygame import*

#Initialize pygame
pygame.init()

#-------------------------------------------
#Define constant variables

#Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#-------------------------------------------
#Load assets

#Create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

#Set up the enemy image
pizza_img = image.load('vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))

#Add a giant pepperoni
draw.circle(GAME_WINDOW, (255, 0, 0), (925, 425), 25, 0)

#Draw a green rectangle
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 395, 110, 110), 5)
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 295, 110, 110), 0)

#-------------------------------------------
#Game loop

game_running = True
while game_running:

#-------------------------------------------
#Check for events
    #Checking for and handling events
    for event in pygame.event.get():

        #Exit loop on quit
        if event.type == QUIT:
            game_running = False

#------------------------------------------- 
#Update display.
    display.update()

#Close main game loop
#-------------------------------------------

#Clean up game
pygame.quit()

