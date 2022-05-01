import pygame
from constantes import *
from sound import Sound
from tiles import Tile
import random
import json
from pickle import TRUE
from tkinter import Button, font
from numpy import True_
from pygame import locals as const
from tiles import Tile
import random
from functions import get_speed
from functions import play_notes
from threading import Thread

class Game:
    def __init__(self, screen):
        self.ecran = pygame.display.set_mode((WIDTH, HEIGHT ))# Initialise taille écran
        self.fond = pygame.image.load("assets/bg.png") # Image de fond
        self.fond = pygame.transform.scale(self.fond, (WIDTH, HEIGHT)) # On redimensionne à la nouvelle résolution
        self.win = self.ecran
        Sound.music_bg(self.win)
        self.continuer = True
        self.tile = Tile(0,0, self.win)
        self.clock = pygame.time.Clock()
        self.continuer = True
        self.homepage = True
        self.gamepage = False
        self.tile_group =pygame.sprite.Group()
        # on génère un nombre entre 0 et 3
        self.x = random.randint(0,3)
        # on créer la touche noir
        self.tile = Tile(self.x * TILE_WIDTH, TILE_HEIGHT, self.win )
        # on l'ajoute au groupe
        self.tile_group.add(self.tile)
        self.scrolling = 0
        self.num_tile = 1
        self.score = 0
        self.speed = 1
        self.pos = None
        self.notes_count = 0
        # on ouvre le fichier contenant les notes 
        with open ('notes.json') as file:
            notes_dict = json.load(file)
        self.notes_list = notes_dict['1']
        pygame.mixer.set_num_channels(len(self.notes_list))
        # liste des notes du morceau sélectionné
    def run(self):
        while self.continuer:
            pos = None
            self.win.blit(self.fond, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continuer = False
                    # de manière à pouvoir quitter le menu avec echap ou la croix
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE or \
                        event.key == pygame.K_q:
                        self.continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
            # Pour chaque touche noir du groupe
            for tile in self.tile_group:
                # on augmente la vitesse 
                tile.update(self.speed)
                if pos:
                    if tile.rect.collidepoint(pos):
                        tile.active = False
                        self.score +=1
                        pos = None
                        self.note = self.notes_list[self.notes_count]
                        thread = Thread(target=play_notes, args=(f'music/{self.note}.ogg', ))
                        thread.start()
                        thread.join()
                        # on joue les notes suivantes 
                        self.notes_count = (self.notes_count + 1) % len(self.notes_list)
                # le jeu est fermé lorsque la touche, touche le bas de l'écran
                if tile.rect.bottom >= HEIGHT and tile.active:
                    self.continuer = False
                    # Sound.music_endgame(self.win)
            if len(self.tile_group) > 0:
            # on accède au dernier sprite
                tile = self.tile_group.sprites()[-1]
                if tile.rect.top + self.speed >= 0:
                    # on génère un nombre entre 0 et 3
                    x = random.randint(0,3)
                    y = -TILE_HEIGHT - (0 - tile.rect.top)
                    # on créer la touche noir
                    tile = Tile(x * TILE_WIDTH,y, self.win )
                    # on l'ajoute au groupe
                    self.tile_group.add(tile)
                    # on gernère une nouvelle touche
                    self.num_tile += 1
                    # le score augmente
                    self.score +=1
            self.speed = int(get_speed(self.score) * (FPS / 2000))
            self.clock.tick(FPS)
            pygame.display.update()