import pygame, random;

pygame.init();

screenWidth = 640;
screenHeight = 480;
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight));

pygame.display.set_caption("Flappy Square");

fps = pygame.time.Clock();

def gameLoop():
    running = True;
    while running == True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;

        #Updating the screen
        pygame.display.update();
        fps.tick(60);

gameLoop();
pygame.quit();
quit();
