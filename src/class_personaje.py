import pygame
from class_cuchillo import Cuchillo
from config import *
from animaciones import get_animaciones_personaje

class Personaje(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple):
        super().__init__()

        # Configuro la imagen del personaje y pongo la posicion donde va a iniciar
        self.animaciones = get_animaciones_personaje()
        self.indice = 0
        self.image = self.animaciones[self.indice]
        self.contador_animaciones = 0

        self.rect = self.image.get_rect()
        self.rect.center = posicion

        self.speed_x = 0 # Hago que la velocidad inicie en 0
        self.speed_y = 0
        self.left = False
        self.saltando = False
        self.flag_disparar_d = False
        self.flag_disparar_i = False


    def update(self):
        self.rect.x += self.speed_x # Para modificar donde se posiciona la coordenada en x
        # Animaciones
        if self.speed_x < 0: # Si está yendo a la izquierda
            self.left = True
            if self.saltando:
                self.contador_animaciones += 1
                if self.indice < 22:
                    self.indice = 22
                if self.indice >= 24:
                    self.indice = 22
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
            else:
                self.contador_animaciones += 1
                if self.indice < 10:
                    self.indice = 10                
                if self.indice >= 15:
                    self.indice = 10
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
        elif self.speed_x > 0:
            self.left = False
            if self.saltando:
                self.contador_animaciones += 1
                if self.indice < 25:
                    self.indice = 25    
                if self.indice >= 27:
                    self.indice = 25
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
            else:
                self.contador_animaciones += 1
                if self.indice < 16:
                    self.indice = 16    
                if self.indice >= 21:
                    self.indice = 16
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
        elif self.speed_x == 0 and not self.saltando:
            if self.left:
                self.contador_animaciones += 1
                if self.indice >= 4:
                    self.indice = 0
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
            else:
                self.contador_animaciones += 1
                if self.indice < 5:
                    self.indice = 5    
                if self.indice >= 9:
                    self.indice = 5
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0          
        else:
            if self.left:
                self.contador_animaciones += 1
                if self.indice < 22:
                    self.indice = 22
                if self.indice >= 24:
                    self.indice = 22
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
            else:
                self.contador_animaciones += 1
                if self.indice < 25:
                    self.indice = 25    
                if self.indice >= 27:
                    self.indice = 25
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0

        if self.flag_disparar_d or self.flag_disparar_i:
            if self.flag_disparar_d:
                self.contador_animaciones += 1
                if self.indice < 5:
                    self.indice = 5    
                if self.indice >= 9:
                    self.indice = 5
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0
            else:
                self.contador_animaciones += 1
                if self.indice >= 4:
                    self.indice = 0
                if self.contador_animaciones == 13:
                    self.indice += 1
                    self.contador_animaciones = 0      

        self.image = self.animaciones[self.indice]


    def atacar(self, sprites, cuchillos, direccion: bool):
        if direccion:
            self.cuchillo = Cuchillo("./src/assets/personaje/ataque/cuchillo.png", SIZE_CUCHILLO, SPEED_CUCHILLO, (self.rect.centerx + 10, self.rect.centery + 18), direccion)
        else:
            self.cuchillo = Cuchillo("./src/assets/personaje/ataque/cuchillo_izquierda.png", SIZE_CUCHILLO, SPEED_CUCHILLO, (self.rect.centerx - 10, self.rect.centery + 18), direccion)
        sprites.add(self.cuchillo)
        cuchillos.add(self.cuchillo)