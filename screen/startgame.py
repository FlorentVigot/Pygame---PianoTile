import pygame
from constantes import *


class Startgame:
    def __init__(self, screen):
        # Image de fond menu
        self.fond_menu = pygame.image.load("assets/bg_menu.png")
        # On redimensionne à la nouvelle résolution
        self.fond_menu = pygame.transform.scale(self.fond_menu, (WIDTH, HEIGHT))
        self.home_page = True
        self.ecran = pygame.display.set_mode((WIDTH, HEIGHT ))

        self.win = self.ecran

    def menu_display(self):
            if self.home_page:
                self.win.blit(self.fond_menu, (WIDTH//8, HEIGHT//8))