import pygame
from animaciones import get_animaciones_vida

class Barra_vida(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple):
        super().__init__()

        self.animaciones = get_animaciones_vida()
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

        self.vida = 75
        self.flag_colision = False

        self.flag_muerto = False


    def update(self):
        if self.vida == 75:
            self.indice = 0
        elif self.vida == 50:
            self.indice = 1
        elif self.vida == 25:
            self.indice = 2
        else:
            self.indice = 3
            self.flag_muerto = True

        self.image = self.animaciones[self.indice]