import pygame
import random

pygame.mixer.pre_init()
pygame.mixer.init()

class Click():

    def __init__(self, screen):
        self.totalAmount = 0

        self.earnPerClick = 1

        self.screen = screen

        self.bitcoinHitbox = pygame.draw.circle(self.screen, "white", (100,80), 35)

        self.clickAudio = pygame.mixer.Channel(0).play(pygame.mixer.Sound('sfx/clicking_sound.mp3'))

        self.upgradeHitbox = {
            'upgrade1': pygame.draw.rect(self.screen, "black", (800,100,150,30)),
            'upgrade2': pygame.draw.rect(self.screen, "black", (800,300,150,30))
            } 
        
        self.upgradeCosts = {
            'upgrade1': 20,
            'upgrade2': 300
        }


    def getMousePosition(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        return mouseX, mouseY


    def checkClickingOnBitcoin(self, btcImage):
        mouseX, mouseY = Click(self.screen).getMousePosition()
        self.mouseRect = pygame.Rect(mouseX,mouseY, 3, 3)
        
        isClicking = (pygame.mouse.get_pressed(num_buttons=3)[0])
        isColliding = self.bitcoinHitbox.colliderect(self.mouseRect)

        pygame.draw.rect(self.screen, "white", self.mouseRect)

        btcTransform = btcImage

        if isClicking and isColliding:
            self.totalAmount += self.earnPerClick

            btcTransform = pygame.transform.rotozoom(btcImage, random.randint(3, 360), random.uniform(0.8, 1.2))

            self.clickAudio

            pygame.time.wait(200)

        return self.totalAmount, btcTransform, self.earnPerClick
    
    def checkClickingOnUpgrade(self):

        isClicking = (pygame.mouse.get_pressed(num_buttons=3)[0])

        for upgradeId in self.upgradeHitbox.keys():
            isColliding = self.upgradeHitbox[upgradeId].colliderect(self.mouseRect)
            upgradeCost = self.upgradeCosts[upgradeId]

            if (isClicking and isColliding) and self.totalAmount >= upgradeCost:
                self.totalAmount -= upgradeCost

                pygame.time.wait(200)
                
                match upgradeId:
                    case "upgrade1":
                        self.upgradeCosts[upgradeId] = round(self.upgradeCosts[upgradeId] * 1.15, 2)
                
                        self.earnPerClick = round(self.earnPerClick * 1.1, 2)

                    case "upgrade2":
                        self.upgradeCosts[upgradeId] =  round(self.upgradeCosts[upgradeId] * 1.3, 2)

                        self.earnPerClick = round((self.earnPerClick * 1.25), 2)

        
        return self.upgradeCosts