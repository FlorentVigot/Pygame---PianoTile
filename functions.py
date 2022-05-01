import pygame
from constantes import *


def get_speed(score):
    return 200 + 5 * score


# Le chemin pour jouer les notes
def play_notes(notePath):
	pygame.mixer.Sound(notePath).play()