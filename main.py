from typing_extensions import Self
import pygame
from pygame import locals as const
import constantes

from sound import Sound
from screen.startgame import Startgame
from screen.game import Game




# print("Appuyez sur n'importe quelle touche pour lancer la partie !")
pygame.init() 

# set title to windows
pygame.display.set_caption("Piano Tiles")

# create a game instance
game = Game(constantes.SCREEN)

# launch run function from game
game.run()

pygame.quit()
