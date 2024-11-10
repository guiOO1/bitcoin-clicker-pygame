import pygame
from codes.hud import CoinHUD
from save.save import SaveMechanism

screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
running = True


bitcoinImg = pygame.image.load(r'sprites/bitcoin.png')
saveMechanism = SaveMechanism()

saveName, initialTotalAmount, initialUpgradeCosts, initialEarnPerClick, feedback = saveMechanism.load_game("new")

coinHUD = CoinHUD(screen, bitcoinImg, initialTotalAmount, initialUpgradeCosts, initialEarnPerClick)

pygame.init()
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")


    totalAmount, upgradeCosts, earnPerClick = coinHUD.updateVariables()
    
    coinHUD.showHUD(totalAmount, earnPerClick, upgradeCosts)
    

    pygame.display.flip()

    clock.tick(30)

pygame.quit()