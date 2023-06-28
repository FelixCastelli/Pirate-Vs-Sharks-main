import pygame

from config import *

class Plataformas(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, posicion: tuple):
        super().__init__()

        self.image = pygame.image.load(path_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = posicion