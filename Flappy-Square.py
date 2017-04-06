import pygame
import random
import os

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 640
        self.HEIGHT = 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Flappy Square")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.score = 0

        self.running = True
        self.isOnGameOverScreen = False
        self.isOnStartScreen = True

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0) 
        self.GREEN = (0, 205, 0)

        self.fontSize = 45
        self.gameFont = pygame.font.SysFont("monospace", self.fontSize)
        self.gameInstructionsFont = pygame.font.SysFont("monospace", self.fontSize - 20)
        self.gameScoreFont = pygame.font.SysFont("monospace", self.fontSize -10)
    
    def eventHandleing(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False
            if self.event.type == pygame.KEYDOWN: 
                if self.event.key == pygame.K_SPACE: 
                    player.playerYVel = -10    

                if self.event.key == pygame.K_RETURN and self.isOnStartScreen == True:
                    self.isOnStartScreen = False
                    player.playerYAcc = 0.5
                    pipe.pipeVel = -10

                if self.event.key == pygame.K_RETURN and self.isOnGameOverScreen == True:
                    self.isOnGameOverScreen = False
                    self.isOnStartScreen = True


        if pipe.pipesX < 0 + pipe.pipeWidth:
            pipe.pipesX = self.WIDTH + 10
            pipe.pipeHeight = random.randint(100, 200)
            pipe.pipe2Height = random.randint(100, 200) * -1


        if player.playerY > pipe.pipeHeight and player.playerY < pipe.pipe2Height + pipe.pipes2Y and player.playerX == pipe.pipesX:
            self.score +=1
        

    def collision(self):
        if player.playerX < pipe.pipesX + pipe.pipeWidth and player.playerX + player.playerWidth > pipe.pipesX and player.playerY < pipe.pipesY + pipe.pipeHeight and player.playerHeight + player.playerY > pipe.pipesY:             
            self.isOnGameOverScreen = True


        if player.playerX < pipe.pipesX + pipe.pipeWidth and player.playerX + player.playerWidth > pipe.pipesX and player.playerY > pipe.pipes2Y + pipe.pipe2Height and player.playerHeight + player.playerY < pipe.pipes2Y:             
            self.isOnGameOverScreen = True

    def newGame(self):
        if self.isOnStartScreen == False:
            self.isOnStartScreen == True

        if self.isOnGameOverScreen == True:
            player.playerX = 120
            self.score = 0
            player.playerY = 300
            pipe.pipesX =  self.WIDTH + 10
            player.playerYVel = 0

    def gameOver(self):
        gameOverText = self.gameFont.render("Game Over", True, self.WHITE)
        continueText = self.gameInstructionsFont.render("Press enter to continue", True,  self.WHITE)

        if self.isOnGameOverScreen == True and self.isOnStartScreen == False:
            while self.isOnGameOverScreen:
                self.screen.fill(self.BLACK)
                self.screen.blit(gameOverText, (self.WIDTH/3, self.HEIGHT/3))
                self.screen.blit(continueText, (self.WIDTH/4,self.HEIGHT/2.2))
                break

    def startScreen(self):
        self.startScreenText = self.gameFont.render("Flappy Square", True, self.WHITE)    
        self.pressSpaceKeyToJumpText = self.gameInstructionsFont.render("Press the space key to jump", True, self.WHITE)
        if self.isOnStartScreen == True and self.isOnGameOverScreen == False:
            while self.isOnStartScreen:
                player.playerYVel = 0
                player.playerYAcc = 0
                pipe.pipeVel = 0
                self.screen.fill(self.BLACK)
                self.screen.blit(self.startScreenText, (self.WIDTH/4, self.HEIGHT/3))
                self.screen.blit(self.pressSpaceKeyToJumpText, (self.WIDTH/5, self.HEIGHT/2.2))
                break

    def gamescore(self):
        self.gameScoreText = self.gameScoreFont.render(str(self.score), True, self.WHITE)
        self.screen.blit(self.gameScoreText, (self.WIDTH/2, self.HEIGHT * 0))

class Player:
    def __init__(self):
        self.playerX = 120
        self.playerY = 300
        self.playerYVel = 0
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
        self.pipe2Height = self.pipeHeight * -1 

        self.pipeVel = -10
    
    def drawtoppipe(self):
        pygame.draw.rect(game.screen, game.GREEN, (self.pipesX, self.pipesY, self.pipeWidth, self.pipeHeight))

    def drawbottompipe(self):
        pygame.draw.rect(game.screen, game.GREEN, (self.pipesX, pipe.pipes2Y, self.pipeWidth, self.pipe2Height))

    def movement(self):
        self.pipesX += self.pipeVel
    
    

game = Game()
player = Player()
pipe = Pipes()

while game.running:
    game.eventHandleing()
    game.collision()

    player.draw() 

    pipe.drawtoppipe()
    pipe.drawbottompipe()
    pipe.movement()

    game.startScreen()

    game.gameOver()

    player.movement()

    game.gamescore()
    game.newGame()
    print(str(pipe.pipesX) + " " + str(player.playerX))

    pygame.display.update()
    game.screen.fill(game.BLACK)
    game.clock.tick(game.FPS)

pygame.quit()
quit()
