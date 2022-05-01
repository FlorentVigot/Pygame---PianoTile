import pygame


class Sound:
    def music_bg(self):
        # music by Flujino ( it's me ! )
        pygame.mixer.music.load('music/bar.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
    def music_endgame(self):
        pygame.mixer.music.load('music/FailPage.mp3')
        pygame.mixer.music.play()

        # # Titre du jeu
        # pygame.display.set_caption('Piano Bar')

        # # initialise la musique
        # pygame.mixer.init()


        # # musique répétitive 
        # pygame.mixer.music.play(-1)