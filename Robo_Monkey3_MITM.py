#Name: Robo_Monkey3_MITM (Monkey In The Middle)
#Author:Rex
#Date:3/27/24


#Use the down arrow to bounce to the beat :)

#Import libraries
import pygame
import sys
import time

#---------------------Background stuff--------------------------

#load background img
bg = pygame.image.load("img/background.jpg")

#Add music
theme = 'audio/wii_theme.mp3'
pygame.mixer.init()
pygame.mixer.music.load(theme)
pygame.mixer.music.play()
#-----------------------------------------------


#-----------------------Class for the background monkeys-----------------
class Monkeys(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        #import sprites to empty list for background monkeys
        self.sprites = []
        self.sprites.append(pygame.image.load('img/sprite_1.png'))
        self.sprites.append(pygame.image.load('img/sprite_2.png'))

        #Set sprite location for background monkeys
        self.current_sprite = 0
        self.counter = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    #Updates which frame/image the sprite is on
    def update(self):
            
            #counter for what sprite to display
            #Don't ask me how these numbers work, it was just a lot of trail and error
            self.counter += 1.2335

            #Depending on what the counter is on, either make the monkeys go up or down
            if self.counter >= 30 and self.counter < 60:
                self.current_sprite = 1
            elif self.counter >= 60:

                self.counter = 0
                self.current_sprite = 0


            #Set the image to the current image in the list
            self.image = self.sprites[self.current_sprite]

    #Calculate time that has passed
    #elapsed_time = pygame.time.get_ticks()
    #Add background monkeys
    #if elapsed_time > 100:
#-----------------------------------------------------
            

#------------Different class for the player sprite-------------------------   
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()


        #Import sprites for playable monkey
        self.playable_sprites = []
        self.playable_sprites.append(pygame.image.load('img/sprite_2.png'))
        self.playable_sprites.append(pygame.image.load('img/sprite_0.png'))

        #Set sprite location for playable monkey
        self.player_current_sprite = 0
        self.image = self.playable_sprites[self.player_current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    #Updates which frame/image the sprite is on
    def update(self,bounce):
        #Set the image to b o u n c e (0 or 1) depending on player input
        self.image = self.playable_sprites[bounce]
#-------------------------------------------------------------------------
        
#general setup
pygame.init()
clock = pygame.time.Clock()


#Declare B O U N C E
bounce = 0

#Game screen
screen_width = 400
screen_height = 238
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("R O B O  M O N K E Y S")

#Create the background monkey sprites and locations
moving_sprites = pygame.sprite.Group()
monkey2 = Monkeys(200,50)
monkey3 = Monkeys(0,50)

#Player sprite and location
player_sprite = pygame.sprite.Group()
player = Player(100,50)

#Add these sprites to their respective groups
moving_sprites.add(monkey2)
moving_sprites.add(monkey3)
player_sprite.add(player)

#play whole thing
while True:

    #If player wants to leave
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Detect player input
        #if the down arrow is pressed, bounce
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bounce = 1
                elapsed_time = pygame.time.get_ticks()
                print(elapsed_time)
                player_sprite.update(bounce)
                player_sprite.draw(screen)

        #If there's no player input, then don't bounce and reset the image back to standard
        else:
            bounce = 0
            player_sprite.update(bounce)
            player_sprite.draw(screen)

    #Drawing screen and sprites
    screen.blit(bg, (0,0)) 
    moving_sprites.draw(screen)
    player_sprite.draw(screen)
    moving_sprites.update()
    pygame.display.flip()







    clock.tick(60)





        



