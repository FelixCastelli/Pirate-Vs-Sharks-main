import pygame
from animaciones import get_animaciones_oro

class Oro(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple):
        super().__init__()

        self.animaciones = get_animaciones_oro()
        self.indice = 0
        self.contador_animaciones = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.center = posicion


    def update(self):
        self.contador_animaciones += 1
        if self.indice >= 4:
            self.indice = 0
        if self.contador_animaciones == 7:
            self.indice += 1
            self.contador_animaciones = 0

        self.image = self.animaciones[self.indice]