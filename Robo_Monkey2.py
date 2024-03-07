

#Import libraries
import pygame
import sys
import time
#load background img
bg = pygame.image.load("img/background.jpg")

#Add music
theme = 'audio/wii_theme.mp3'
pygame.mixer.init()
pygame.mixer.music.load(theme)
pygame.mixer.music.play()




class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        #import sprites to empty list
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load('img/sprite_0.png'))
        self.sprites.append(pygame.image.load('img/sprite_1.png'))
        self.sprites.append(pygame.image.load('img/sprite_2.png'))
        self.sprites.append(pygame.image.load('img/sprite_3.png'))
        self.sprites.append(pygame.image.load('img/sprite_4.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    #Updates which frame/image the sprite is on
    def update(self):
        #If the down button is pressed
        if self.is_animating == True:
            #Go to the next image in the list
            self.current_sprite += 1

            #Unless we are at the end of the list, in which case
            #go back to the start
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            #Set the image to the current image in the list
            self.image = self.sprites[self.current_sprite]

    #Toggle whether or not the sprite is moving
    #def animate(self):
        #self.is_animating = True






#general setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_width = 400
screen_height = 238
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("R O B O  M O N K E Y S")

#Create the sprites and groups
moving_sprites = pygame.sprite.Group()
monkey1 = Player(100,50)
monkey2 = Player(200,50)
monkey3 = Player(0,50)









  



#play whole thing
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #If the down arrow is pressed, run animation
        #if event.type == pygame.KEYDOWN:
            #player.animate()
    

    #Drawing
    screen.blit(bg, (0,0)) 
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()


    #Calculate time that has passed
    elapsed_time = pygame.time.get_ticks()

    #Add monkeys for when an amount of time has passed
    if elapsed_time >= 7000:
        moving_sprites.add(monkey1)
 
    if elapsed_time >= 10500:
        moving_sprites.add(monkey2)
    
    if elapsed_time >= 13700:
        moving_sprites.add(monkey3)
        


    clock.tick(6.2)
