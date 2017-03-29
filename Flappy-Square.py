import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 640
        self.HEIGHT = 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Flappy Square")
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.running = True

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)


    def eventHandleing(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False

            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_UP:
                    player.playerYAcc = -0.5
                if self.event.key == pygame.K_DOWN:
                    player.playerYAcc = 0.5
            if self.event.type == pygame.KEYUP:
                if self.event.key == pygame.K_UP or self.event.key == pygame.K_DOWN:
                    player.playerYAcc = 0

                    
class Player:
    def __init__(self):
        self.playerX = game.WIDTH/3
        self.playerY = 300
        self.playerYVel = 0
        self.playerWidth = 20
        self.playerHeight = 20
        self.playerYAcc = 0
        #self.playerFriction = -0.13
        

    def draw(self):
        pygame.draw.rect(game.screen, game.WHITE, (self.playerX, self.playerY, self.playerWidth, self.playerHeight))

    def movement(self):
        # Motion
        #self.playerYAcc += self.playerYVel * self.playerFriction

        self.playerYVel += self.playerYAcc 

        self.playerY += self.playerYVel + self.playerYAcc/2
 
        
game = Game()
player = Player()

while game.running:
    game.eventHandleing()

    player.draw() 

    player.movement()
    print("Acc " + str(player.playerYAcc))
    print("Vel " + str(player.playerYVel))

    pygame.display.update()
    game.screen.fill(game.BLACK)
    game.clock.tick(game.FPS)
pygame.quit()
quit()
