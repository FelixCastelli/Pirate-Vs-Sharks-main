import pygame
from config import SIZE_PERSONAJE, SIZE_PERSONAJE2, SIZE_ENEMIGO, SIZE_VIDA, SIZE_DIAMANTE, SIZE_ORO, SIZE_PLATA, SIZE_HEAL

def get_animaciones_personaje():
    animaciones = [
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/1_quieto.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/2_quieto.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/3_quieto.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/4_quieto.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/5_quieto.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/1.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/2.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/3.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/4.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/quieto/5.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/1_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/2_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/3_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/4_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/5_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/6_corriendo.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/1.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/2.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/3.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/4.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/5.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/caminar/6.png").convert_alpha(), (SIZE_PERSONAJE2)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/1_saltando.png").convert_alpha(), (SIZE_PERSONAJE)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/2_saltando.png").convert_alpha(), (SIZE_PERSONAJE)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/3_saltando.png").convert_alpha(), (SIZE_PERSONAJE)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/1.png").convert_alpha(), (SIZE_PERSONAJE)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/2.png").convert_alpha(), (SIZE_PERSONAJE)),
        pygame.transform.scale(pygame.image.load("./src/assets/personaje/saltar/3.png").convert_alpha(), (SIZE_PERSONAJE))
        ]

    return animaciones


def get_animaciones_enemigos():
    animaciones_enemigos = [
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/1_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/2_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/3_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/4_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/5_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/6_enemigo.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/1.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/2.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/3.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/4.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/5.png").convert_alpha(), (SIZE_ENEMIGO)),
        pygame.transform.scale(pygame.image.load("./src/assets/enemigos/6.png").convert_alpha(), (SIZE_ENEMIGO))
        ]
    
    return animaciones_enemigos


def get_animaciones_vida():
    animaciones_vida = [
        pygame.transform.scale(pygame.image.load("./src/assets/vida/health_bar0.png").convert_alpha(), (SIZE_VIDA)),
        pygame.transform.scale(pygame.image.load("./src/assets/vida/health_bar1.png").convert_alpha(), (SIZE_VIDA)),
        pygame.transform.scale(pygame.image.load("./src/assets/vida/health_bar2.png").convert_alpha(), (SIZE_VIDA)),
        pygame.transform.scale(pygame.image.load("./src/assets/vida/health_bar3.png").convert_alpha(), (SIZE_VIDA))
        ]

    return animaciones_vida


def get_animaciones_diamante():
    animaciones_diamante = [
        pygame.transform.scale(pygame.image.load("./src/assets/items/diamante/0.png").convert_alpha(), (SIZE_DIAMANTE)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/diamante/1.png").convert_alpha(), (SIZE_DIAMANTE)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/diamante/2.png").convert_alpha(), (SIZE_DIAMANTE)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/diamante/3.png").convert_alpha(), (SIZE_DIAMANTE)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/diamante/0.png").convert_alpha(), (SIZE_DIAMANTE))  
    ]

    return animaciones_diamante


def get_animaciones_oro():
    animaciones_moneda_oro = [
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/0_gold.png").convert_alpha(), (SIZE_ORO)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/1_gold.png").convert_alpha(), (SIZE_ORO)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/2_gold.png").convert_alpha(), (SIZE_ORO)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/3_gold.png").convert_alpha(), (SIZE_ORO)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/0_gold.png").convert_alpha(), (SIZE_ORO))    
    ]

    return animaciones_moneda_oro


def get_animaciones_plata():
    animaciones_moneda_plata = [
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/0_silver.png").convert_alpha(), (SIZE_PLATA)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/1_silver.png").convert_alpha(), (SIZE_PLATA)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/2_silver.png").convert_alpha(), (SIZE_PLATA)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/3_silver.png").convert_alpha(), (SIZE_PLATA)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/monedas/0_silver.png").convert_alpha(), (SIZE_PLATA))    
    ]

    return animaciones_moneda_plata

def get_animaciones_heal():
    animaciones_heal = [
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export1.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export2.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export3.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export4.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export5.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export6.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export7.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export8.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export9.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export10.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export11.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export12.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export13.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export14.png").convert_alpha(), (SIZE_HEAL)),
        pygame.transform.scale(pygame.image.load("./src/assets/items/heal/Botella-export15.png").convert_alpha(), (SIZE_HEAL))
    ]

    return animaciones_heal