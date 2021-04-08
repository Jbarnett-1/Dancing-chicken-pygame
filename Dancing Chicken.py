#import and running PyGame application
import pygame

pygame.init()

display_width = 1200
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dancing Chicken')

#define colors RGB
black = (0,0,0)
white = (255,255,255)

#game clock to time (FPS)
clock = pygame.time.Clock()
crashed = False
chickenImg = pygame.image.load('bird.png')

def chicken(x,y):
    gameDisplay.blit(chickenImg, (x,y)) #reference the variable in front
    
x = (display_width * 0.25)
y = (display_height * 0.60)
x_change = 0
chicken_speed = 0

#game loop 
while not crashed:
    for event in pygame.event.get(): #detects mouse, slicking, and keys
        if event.type == pygame.QUIT: #how to quit
            crashed = True     #break out of loop
   
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0   #so doesn't move continuously 
    
    x += x_change
    
    gameDisplay.fill(white) #color of the background
    chicken(x,y) #chicken over the background
        
    pygame.display.update() #can put parameter inside and make it easy to update
    clock.tick(60) #number is frames per second
    
pygame.quit() #stop pygame from running
quit()