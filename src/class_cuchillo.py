import pygame

class Cuchillo(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, velocidad: int, salida: tuple, direccion: bool):
        super().__init__()

        self.image = pygame.image.load(path_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        
        self.speed_x = velocidad
        self.rect.center = salida

        self.flag_direccion = direccion


    def update(self):
        if self.flag_direccion == True:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x