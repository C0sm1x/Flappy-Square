import pygame
import random
import time

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
        self.YELLOW = (255, 255, 0) 
        self.GREEN = (0, 0, 255)

    def eventHandleing(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False
            if self.event.type == pygame.KEYDOWN: 
                if self.event.key == pygame.K_SPACE: 
                    player.playerYVel = -10
            
        if pipe.pipesX < 0 + pipe.pipeWidth:
            pipe.pipesX = self.WIDTH + 10
            pipe.pipeHeight = random.randint(100, 200)
            pipe.pipe2Height = random.randint(100, 200) * -1
            
    def collision(self):
        if player.playerX < pipe.pipesX + pipe.pipeWidth and player.playerX + player.playerWidth > pipe.pipesX and player.playerY < pipe.pipesY + pipe.pipeHeight and player.playerHeight + player.playerY > pipe.pipesY:             
            time.sleep(2)

        if player.playerX < pipe.pipesX + pipe.pipeWidth and player.playerX + player.playerWidth > pipe.pipesX and player.playerY > pipe.pipes2Y + pipe.pipe2Height and player.playerHeight + player.playerY < pipe.pipes2Y:             
            time.sleep(2)
class Player:
    def __init__(self):
        self.playerX = game.WIDTH/3
        self.playerY = 300
        self.playerYVel = 0
        self.playerXVel = 0
        self.playerWidth = 20
        self.playerHeight = 20
        self.playerYAcc = 0.5
        

    def draw(self):
        pygame.draw.rect(game.screen, game.YELLOW, (self.playerX, self.playerY, self.playerWidth, self.playerHeight))

    def movement(self):
        # Motion
        self.playerYVel += self.playerYAcc 

        self.playerY += self.playerYVel + self.playerYAcc/2

 
class Pipes:
    def __init__(self):
        self.pipeWidth = 10
        self.pipeHeight = random.randint(100, 200)
        self.pipesX = game.WIDTH + 10
        self.pipesY = 0

        self.pipes2Y = game.HEIGHT
        self.pipe2Height = self.pipeHeight * -1 + player.playerHeight
    
    def drawtoppipe(self):
        pygame.draw.rect(game.screen, game.GREEN, (self.pipesX, self.pipesY, self.pipeWidth, self.pipeHeight))

    def drawbottompipe(self):
        pygame.draw.rect(game.screen, game.GREEN, (self.pipesX, pipe.pipes2Y, self.pipeWidth, self.pipe2Height))

    def movement(self):
        self.pipesX -= 3
    
    

game = Game()
player = Player()
pipe = Pipes()

while game.running:
    game.eventHandleing()
    game.collision()

    player.draw() 
    player.movement()

    pipe.drawtoppipe()
    pipe.drawbottompipe()
    pipe.movement()

    pygame.display.update()
    game.screen.fill(game.BLACK)
    game.clock.tick(game.FPS)
pygame.quit()
quit()
