import pygame
from codes.click_mechanism import Click

pygame.font.init()

class CoinHUD():
    def __init__(self, screen, bitcoinImg):

        self.screen = screen
        self.bitcoinImg = bitcoinImg

        self.ClickMechanism = Click(self.screen)

    def showHud(self, totalAmount, upgradeCost, earnPerClick):
        hudFont = pygame.font.SysFont('Arial', 40, bold=True)

        hudCounter = hudFont.render(f'{totalAmount} satoshis', False, (0,0,0))
        hudUpgrade1 = hudFont.render(f'cost:{upgradeCost["upgrade1"]} satoshis', False, (0,0,0))
        hudUpgrade2 = hudFont.render(f'cost:{upgradeCost["upgrade2"]} satoshis', False, (0,0,0))
        hudEarnPerClick = hudFont.render(f'{earnPerClick} satoshis p/click', False, (255,0,0))

        self.screen.blit(hudCounter, (200,0))
        self.screen.blit(hudUpgrade1, (400,200))
        self.screen.blit(hudUpgrade2, (400,300))
        self.screen.blit(hudEarnPerClick, (0,200))

        self.screen.blit(self.btcTransform,(50,30))
    
    def updateVariables(self):
        totalAmount, self.btcTransform, earnPerClick = self.ClickMechanism.checkClickingOnBitcoin(self.bitcoinImg)

        upgradeCost = self.ClickMechanism.checkClickingOnUpgrade()

        return round(totalAmount,2), upgradeCost, earnPerClick

class SaveHUD():

    def __init__(self):
        pass

    def showSaveHUD():
        pass

    def showOpenSaveHUD():
        pass

    def showLoadHUD():
        pass