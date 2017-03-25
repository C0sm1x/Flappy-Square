import pygame, random;

pygame.init();

SCREENWIDTH = 640;
SCREENHEIGHT = 480;
gameDisplay = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT));

pygame.display.set_caption("Flappy Square");

fps = pygame.time.Clock();

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

                  
class player:
    def __init__(self, playerX, playerY, playerXVelocity, playerYVelocity, playerWidth, playerHeight, WHITE):
        self.playerX = playerX
        self.playerY = playerY
        self.playerXVelocity = playerXVelocity
        self.playerYVelocity = playerYVelocity
        self.playerWidth = playerWidth
        self.playerHeight = playerHeight
        self.playerColor = WHITE


    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.playerColor, (self.playerX, self.playerY, self.playerWidth, self.playerHeight) )
    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.playerYVelocity = -8
                self.playerY += self.playerYVelocity
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.playerYVelocity = 0


def gameLoop():
    running = True;
    playerX = 200
    playerY = 200
    playerXVelocity = 0
    playerYVelocity = 0
    playerWidth = 10
    playerHeight = 10

    player1 = player(playerX, playerY, playerXVelocity, playerYVelocity, playerWidth, playerHeight, WHITE)
    while running == True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            player1.movement(event)

        player1.draw(gameDisplay)

        #Updating the screen
        pygame.display.update();
        gameDisplay.fill(BLACK)
        fps.tick(60);

gameLoop();
pygame.quit();
quit();
