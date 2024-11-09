import pygame
from codes.hud import CoinHud

screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
running = True


bitcoinImg = pygame.image.load(r'sprites/bitcoin.png')
coinHud = CoinHud(screen, bitcoinImg)

pygame.init()
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    totalAmount, upgradeCost, earnPerClick = coinHud.updateVariables()
    
    coinHud.showHud(totalAmount, upgradeCost, earnPerClick)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()