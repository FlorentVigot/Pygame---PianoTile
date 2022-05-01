import pygame
from constantes import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,win):
        super(Tile, self). __init__()

        self.win = win
        self.x, self.y = x,y 
        self.color = BLUE
        self.color_border = PURPLE
        # creer nouvelle image sur une autre image avec transparence
        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
        # rectangle
        self.rect = self.surface.get_rect()
        # position rectangle
        self.rect.x = x
        self.rect.y = y
        # Touche active
        self.active = True

    def update(self, speed):
        self.rect.y += speed
        # Si position de la touche est plus grande ou égal à la taille de l'écran 
        if self.rect.y >= HEIGHT:
            # le restangle est tué/effacé
            self.kill()

        if self.active:
            # Dessin de la touche noir
            pygame.draw.rect(self.surface, self.color,(0,0,TILE_WIDTH, TILE_HEIGHT))
            # Dessin de la bordure de la touche
            pygame.draw.rect(self.surface, self.color_border,(0,0,TILE_WIDTH, TILE_HEIGHT), 2)
        else:
            # Dessin transparent
            pygame.draw.rect(self.surface, (0,0,0,90), (0,0,TILE_WIDTH, TILE_HEIGHT))
        # dessin au dessus de l'autre
        self.win.blit(self.surface, self.rect)