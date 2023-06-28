import pygame
from animaciones import get_animaciones_enemigos
from config import WIDTH

class Enemigos(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple, speed: int):
        super().__init__()

        self.animaciones = get_animaciones_enemigos()
        self.indice = 0
        self.image = self.animaciones[self.indice]
        self.contador_animaciones = 0

        self.rect = self.image.get_rect()
        self.rect.midbottom = posicion

        self.speed_x = speed
        self.left = False
        self.flag_direccion = False


    def update(self):
        if not self.flag_direccion:
            self.rect.x += self.speed_x
            self.left = True
            self.contador_animaciones += 1
            if self.indice >= 5:
                self.indice = 0
            if self.contador_animaciones == 11:
                self.indice += 1
                self.contador_animaciones = 0
            
            if self.rect.right >= WIDTH:
                self.flag_direccion = True
                self.rect.right = WIDTH

        elif self.flag_direccion:
            self.rect.x -= self.speed_x
            self.left = False
            self.contador_animaciones += 1
            if self.indice < 6:
                self.indice = 6    
            if self.indice >= 11:
                self.indice = 6
            if self.contador_animaciones == 11:
                    self.indice += 1
                    self.contador_animaciones = 0

            if self.rect.left <= 0:
                self.flag_direccion = False
                self.rect.left = 0

        self.image = self.animaciones[self.indice]