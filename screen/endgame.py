import pygame
from constantes import *


from screen.startgame import Game


class Endgame:
    def __init__(self, screen):
        self.gameover = False
        self.blocrouge = 0
        self.blocrouge_bg = pygame.image.load('assets/play.png')

    def update(self, win):
        if self.gameover:
            speed = 0

            if self.blocrouge > 20:
                win.blit(self.blocrouge, (0,0))

