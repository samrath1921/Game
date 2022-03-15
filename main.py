import random
import sys
import pygame
from pygame.locals import *

FPS=32
SCREENWIDTH=1900
SCREENHEIGHT=1000

SCREEN= pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES={}    
GAME_SOUNDS={}
PLAYER='gallery/sprites/heli.png'
BACKGROUND='gallery/sprites/background.jpg'
PIPE='gallery/sprites/building.jpg'

def welcomeScreen():
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ =="__main__":
    pygame.init()
    FPSCLOCK= pygame.time.Clock()
    pygame.display.set_caption('HELI CRASH')
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.jfif').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SOUNDS['die']=pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('gallery/audio/Crash .mp3')
    GAME_SOUNDS['point']=pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('gallery/audio/Swoosh.mp3')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('gallery/audio/Helicopter By.mp3')

    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame()

