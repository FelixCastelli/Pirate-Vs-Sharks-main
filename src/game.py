import pygame
import sys
import random
import json

from config import *
from class_personaje import Personaje
from class_plataforma import Plataformas
from class_enemigo import Enemigos
from class_barra_vida import Barra_vida
from class_diamante import Diamante
from class_plata import Plata
from class_oro import Oro
from class_heal import Heal

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pirate Vs Sharks")
        icono = pygame.image.load("./src/assets/imagenes/tiburon.png")
        icono = pygame.transform.scale(icono, SIZE_ICONO)
        pygame.display.set_icon(icono)
        self.screen = pygame.display.set_mode(DISPLAY)
        self.clock = pygame.time.Clock()

        self.jugando = False
        self.cooldown = 0
        self.score = 0
        self.high_score = 0
        self.lista_puntaje = []

        # self.musica_nivel = ("./src/assets/sonidos/level_music.mp3")
        # self.musica = pygame.mixer.Sound(self.musica_nivel)
        # self.musica.set_volume(0.05)

        # self.musica_general = ("./src/assets/sonidos/overworld_music.mp3")
        # self.musica_g = pygame.mixer.Sound(self.musica_general)
        # self.musica_g.set_volume(0.05)

        # self.s_salto = ("./src/assets/sonidos/jump.mp3")
        # self.sonido_saltar = pygame.mixer.Sound(self.s_salto)
        # self.sonido_saltar.set_volume(0.07)

        # self.s_ataque = ("./src/assets/sonidos/hit.mp3")
        # self.sonido_ataque = pygame.mixer.Sound(self.s_ataque)
        # self.sonido_ataque.set_volume(0.1)

        # self.s_kill = ("./src/assets/sonidos/stomp.mp3")
        # self.sonido_kill = pygame.mixer.Sound(self.s_kill)
        # self.sonido_kill.set_volume(0.1)

        # self.s_heal = ("./src/assets/sonidos/heal.mp3")
        # self.sonido_heal = pygame.mixer.Sound(self.s_heal)
        # self.sonido_heal.set_volume(1.5)

        # self.s_moneda = ("./src/assets/sonidos/coin.mp3")
        # self.sonido_moneda = pygame.mixer.Sound(self.s_moneda)
        # self.sonido_moneda.set_volume(0.3)

        # self.s_powerup = ("./src/assets/sonidos/power-up_explosion.mp3")
        # self.sonido_powerup = pygame.mixer.Sound(self.s_powerup)
        # self.sonido_powerup.set_volume(0.3)

        # self.s_damage = ("./src/assets/sonidos/damage.mp3")
        # self.sonido_damage = pygame.mixer.Sound(self.s_damage)
        # self.sonido_damage.set_volume(0.3)

        self.fuente = pygame.font.Font("./src/assets/fuentes/ARCADEPI.TTF", 30)
        self.fuente_final_score = pygame.font.Font("./src/assets/fuentes/ARCADEPI.TTF", 60)
        self.fuente_misc = pygame.font.Font("./src/assets/fuentes/ARCADEPI.TTF", 20)
        self.fuente_nombre = pygame.font.Font("./src/assets/fuentes/PIRATA.ttf", 100)

        self.fondo = pygame.image.load("./src/assets/imagenes/fondo.jpg")
        self.fondo = pygame.transform.scale(self.fondo, DISPLAY)

        self.fondo_game_over = pygame.image.load("./src/assets/imagenes/fondo_game_over.png")
        self.fondo_game_over = pygame.transform.scale(self.fondo_game_over, DISPLAY)

        self.fondo_menu_inicio = pygame.image.load("./src/assets/imagenes/fondo_menu.jpg")
        self.fondo_menu_inicio = pygame.transform.scale(self.fondo_menu_inicio, DISPLAY)

        self.sprites = pygame.sprite.Group() # Crea grupos
        self.plataformas = pygame.sprite.Group()
        self.cuchillo = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.diamante = pygame.sprite.Group()
        self.plata = pygame.sprite.Group()
        self.oro = pygame.sprite.Group()
        self.heal = pygame.sprite.Group()

        self.agregar_sprite(self.cuchillo)
        self.agregar_cuchillos(self.cuchillo)

        self.personaje = Personaje(START_POS)
        self.agregar_sprite(self.personaje) # Aca agrego el personaje como sprite

        self.plataforma = Plataformas("./src/assets/terreno/terreno_plataforma_portal.png", SIZE_PLATAFORMA, (170, 400))
        self.agregar_plataforma(self.plataforma)
        self.agregar_sprite(self.plataforma)

        self.plataforma_2 = Plataformas("./src/assets/terreno/terreno_plataforma_portal.png", SIZE_PLATAFORMA, (WIDTH - 170, 400))
        self.agregar_plataforma(self.plataforma_2)
        self.agregar_sprite(self.plataforma_2)

        self.plataforma_3 = Plataformas("./src/assets/terreno/terreno_plataforma_portal.png", SIZE_PLATAFORMA, (WIDTH // 2, 400))
        self.agregar_plataforma(self.plataforma_3)
        self.agregar_sprite(self.plataforma_3)       

        self.plataforma_suelo = Plataformas("./src/assets/terreno/terreno_suelo.png", SIZE_PLATAFORMA_GRANDE, (WIDTH // 2, 705))
        self.agregar_plataforma(self.plataforma_suelo)
        self.agregar_sprite(self.plataforma_suelo)

        self.barra_vida = Barra_vida(POSICION_VIDA)
        self.agregar_sprite(self.barra_vida)


    def generar_enemigos(self, cantidad):
        if len(self.enemigos) == 0:
            for enemigo in range(cantidad):
                posicion_i = (random.randrange(WIDTH - 5000, -50), POSICION_ENEMIGO_Y)
                posicion_d = (random.randrange(WIDTH + 50, WIDTH + 2000,), POSICION_ENEMIGO_Y)

                enemigo_derecha = Enemigos(posicion_d, SPEED_ENEMIGO)
                enemigo_izquierda = Enemigos(posicion_i, SPEED_ENEMIGO)

                if enemigo_derecha:
                    enemigo_derecha.flag_direccion = True
                elif enemigo_izquierda:
                    enemigo_izquierda.flag_direccion = False

                self.agregar_enemigos(enemigo_izquierda)
                self.agregar_enemigos(enemigo_derecha)
                self.agregar_sprite(enemigo_izquierda)
                self.agregar_sprite(enemigo_derecha)


    def agregar_sprite(self, sprite): # Para mostrar los sprites
        self.sprites.add(sprite)

    def agregar_plataforma(self, plataforma):
        self.plataformas.add(plataforma)

    def agregar_cuchillos(self, cuchillo):
        self.cuchillo.add(cuchillo)

    def agregar_enemigos(self, enemigo):
        self.enemigos.add(enemigo)

    def agregar_vida(self, vida):
        self.barra_vida.add(vida)

    def agregar_diamante(self, diamante):
        self.diamante.add(diamante)

    def agregar_plata(self, plata):
        self.plata.add(plata)

    def agregar_oro(self, oro):
        self.oro.add(oro)

    def agregar_heal(self, heal):
        self.heal.add(heal)


    def actualizar_elementos(self):
        self.generar_enemigos(MAXIMO_ENEMIGOS)
        self.sprites.update()
        for cuchillos in self.cuchillo:
            if cuchillos.rect.left >= WIDTH or cuchillos.rect.right < 0:
                cuchillos.kill()
            cuchillo_esta_colisionando = pygame.sprite.spritecollide(cuchillos, self.plataformas, False)
            if cuchillo_esta_colisionando:
                self.sonido_ataque.play()
                cuchillos.kill()

            cuchillo_esta_colisionando_enemigos = pygame.sprite.spritecollide(cuchillos, self.enemigos, True)
            if cuchillo_esta_colisionando_enemigos:
                enemigo = cuchillo_esta_colisionando_enemigos[0]
                enemigo = enemigo.rect.center
                cuchillos.kill()
                self.sonido_kill.play()
                self.score += 1

                numero_aleatorio = random.randrange(1, 13)
                if numero_aleatorio == 5 and self.barra_vida.vida < 75:
                    heal = Heal(enemigo)
                    self.agregar_sprite(heal)
                    self.agregar_heal(heal)
                elif numero_aleatorio < 3:
                    plata = Plata(enemigo)
                    self.agregar_sprite(plata)
                    self.agregar_plata(plata)
                elif numero_aleatorio > 9 and numero_aleatorio < 12:
                    oro = Oro(enemigo)
                    self.agregar_sprite(oro)
                    self.agregar_oro(oro)
                elif numero_aleatorio == 12 or numero_aleatorio == 13:
                    diamante = Diamante(enemigo)
                    self.agregar_sprite(diamante)
                    self.agregar_diamante(diamante)


        esta_colisionando = pygame.sprite.spritecollide(self.personaje, self.plataformas, False)

        if esta_colisionando:
            piso = esta_colisionando[0] # Agarro a la plataforma
            self.personaje.rect.bottom = piso.rect.top + 1 # el bottom del personaje es el top del piso + 1 para que este arriba
            self.personaje.saltando = False
            self.personaje.speed_y = 0
            self.puede_saltar = True
        else:
            self.puede_saltar = False

        enemigo_esta_colisionando = pygame.sprite.spritecollide(self.personaje, self.enemigos, False)

        if enemigo_esta_colisionando:
            if self.barra_vida.flag_colision == True:
                self.barra_vida.vida -= 25
                self.sonido_damage.play()
                self.barra_vida.flag_colision = False
        elif not self.barra_vida.flag_colision:
            self.barra_vida.flag_colision = True

        if self.barra_vida.flag_muerto:
            self.barra_vida.flag_muerto = False
            self.game_over()

        agarrar_heal = pygame.sprite.spritecollide(self.personaje, self.heal, True)
        agarrar_plata = pygame.sprite.spritecollide(self.personaje, self.plata, True)
        agarrar_oro = pygame.sprite.spritecollide(self.personaje, self.oro, True)
        agarrar_diamante = pygame.sprite.spritecollide(self.personaje, self.diamante, True)

        if agarrar_heal:
            if self.barra_vida.vida < 75:
                self.sonido_heal.play()
                self.barra_vida.vida += 25

        if agarrar_plata:
            self.sonido_moneda.play()
            self.score += 2

        if agarrar_oro:
            self.sonido_moneda.play()
            self.score += 3

        if agarrar_diamante:
            self.sonido_powerup.play()
            self.eliminar_enemigos()
            self.score += 10


    def eliminar_enemigos(self):
        for enemigo in self.enemigos:
            enemigo.kill()


    def render_screen(self):
        if self.cooldown < 46:
            self.cooldown += 1
        self.screen.blit(self.fondo, ORIGIN)
        self.sprites.draw(self.screen)
        self.screen.blit(self.fuente.render(f"SCORE: {self.score}", False, BLACK), SCORE_POS)
        pygame.display.flip()


    def menu_inicio(self):
        self.reiniciar_juego()
        self.flag_menu_inicio = True
        self.musica_g.play(-1)
        while self.flag_menu_inicio:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.musica_g.stop()
                        self.start()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                            self.exit()
                elif evento.type == pygame.QUIT:
                    self.exit()

            texto_titulo = self.fuente_nombre.render("Pirate Vs Sharks", True, WHITE)
            rect_texto_titulo = texto_titulo.get_rect()
            rect_texto_titulo.midtop = POSICION_TITULO

            texto_play = self.fuente_misc.render("PRESS M1 TO PLAY", False, WHITE)
            rect_texto_play = texto_play.get_rect()
            rect_texto_play.midtop = POSICION_PLAY

            texto_exit = self.fuente_misc.render("PRESS ESC TO EXIT", False, WHITE)
            rect_texto_exit = texto_exit.get_rect()
            rect_texto_exit.midtop = POSICION_EXIT

            # texto_high_score = self.fuente_misc.render(f"HIGH SCORE: {self.high_score}", False, WHITE)
            # rect_texto_high_score = texto_high_score.get_rect()
            # rect_texto_high_score.midtop = POSICION_HIGHSCORE

            self.screen.blit(self.fondo_menu_inicio, ORIGIN)

            self.screen.blit(texto_titulo, rect_texto_titulo)
            self.screen.blit(texto_play, rect_texto_play)
            self.screen.blit(texto_exit, rect_texto_exit)
            # self.screen.blit(texto_high_score, rect_texto_high_score)

            pygame.display.flip()


    def start(self):
        self.flag_menu_inicio = False
        self.jugando = True
        self.musica.play(-1)
        while self.jugando:
            self.clock.tick(FPS)

            self.actualizar_elementos()

            self.render_screen()

            self.events()

            self.personaje.update()


    def events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    self.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.pause()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.personaje.speed_x = SPEED_PERSONAJE
            if keys[pygame.K_d]:
                if self.cooldown >= COOLDOWN_CUCHILLO:
                    self.personaje.atacar(self.sprites, self.cuchillo, True)
                    self.cooldown = 0
                    self.sonido_ataque.play()
                    self.personaje.speed_x = 0
            elif keys[pygame.K_a]:
                if self.cooldown >= COOLDOWN_CUCHILLO:
                    self.personaje.atacar(self.sprites, self.cuchillo, False)
                    self.cooldown = 0
                    self.sonido_ataque.play()
                    self.personaje.speed_x = 0
        elif keys[pygame.K_LEFT]:
            self.personaje.speed_x = - SPEED_PERSONAJE # En negativo para que vaya para la izquierda
            if keys[pygame.K_d]:
                if self.cooldown >= COOLDOWN_CUCHILLO:
                    self.personaje.atacar(self.sprites, self.cuchillo, True)
                    self.cooldown = 0
                    self.sonido_ataque.play()
                    self.personaje.speed_x = 0
            elif keys[pygame.K_a]:
                if self.cooldown >= COOLDOWN_CUCHILLO:
                    self.personaje.atacar(self.sprites, self.cuchillo, False)
                    self.cooldown = 0
                    self.sonido_ataque.play()
                    self.personaje.speed_x = 0
        elif keys[pygame.K_UP]:
            if not self.personaje.saltando and self.puede_saltar == True:
                self.personaje.saltando = True
                self.personaje.speed_y = HEIGHT_SALTO
                self.sonido_saltar.play()
            self.personaje.speed_x = 0

        elif keys[pygame.K_d]:
            if self.cooldown >= COOLDOWN_CUCHILLO:
                self.personaje.atacar(self.sprites, self.cuchillo, True)
                self.cooldown = 0
                self.personaje.flag_disparar_d = True
                self.sonido_ataque.play()
                self.personaje.speed_x = 0
        elif keys[pygame.K_a]:
            if self.cooldown >= COOLDOWN_CUCHILLO:
                self.personaje.atacar(self.sprites, self.cuchillo, False)
                self.cooldown = 0
                self.personaje.flag_disparar_i = True
                self.sonido_ataque.play()
                self.personaje.speed_x = 0
        else:
            self.personaje.speed_x = 0
            self.personaje.flag_disparar_d = False
            self.personaje.flag_disparar_i = False

        if self.personaje.saltando:
            self.personaje.rect.y -= self.personaje.speed_y
            self.personaje.speed_y -= GRAVEDAD
        else:
            self.personaje.rect.y += self.personaje.speed_y
            self.personaje.speed_y += GRAVEDAD

        # Esto es para que el personaje no se salga por el lado izquierdo de la pantalla
        if self.personaje.rect.left <= 0: 
            self.personaje.rect.left = 0
        elif self.personaje.rect.right >= WIDTH:
            self.personaje.rect.right = WIDTH


    def game_over(self):
        lista_puntajes = []
        self.jugando = False
        if self.score > self.high_score:
            self.guardar_puntaje(self.score)
            with open(".\src\puntajes.json", "r") as file:
                puntaje = json.load(file)
                for puntajes in puntaje:
                    lista_puntajes.append(puntajes["puntaje"])
                lista_puntajes.sort()
                self.high_score = lista_puntajes[-1]
        self.mostrar_pantalla_fin()


    def mostrar_pantalla_fin(self):
        self.pantalla_fin = True
        self.musica.stop()
        self.musica_g.play(-1)
        while self.pantalla_fin:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.pantalla_fin = False
                        self.musica_g.stop()
                        self.reiniciar_juego()
                        self.start()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        self.musica_g.stop()
                        self.pantalla_fin = False
                        self.menu_inicio()
                elif evento.type == pygame.QUIT:
                    self.exit()

            texto_game_over = self.fuente.render("GAME OVER", False, WHITE)
            rect_texto_game_over = texto_game_over.get_rect()
            rect_texto_game_over.midtop = POSICION_GAME_OVER

            texto_final_score = self.fuente_final_score.render(f"YOUR SCORE: {self.score}", False, WHITE)
            rect_texto_final_score = texto_final_score.get_rect()
            rect_texto_final_score.midtop = POSICION_FINAL_SCORE

            texto_high_score = self.fuente_misc.render(f"HIGH SCORE: {self.high_score}", False, WHITE)
            rect_texto_high_score = texto_high_score.get_rect()
            rect_texto_high_score.midtop = POSICION_HIGHSCORE

            texto_retry = self.fuente_misc.render("PRESS M1 TO RETRY", False, WHITE)
            rect_texto_retry = texto_retry.get_rect()
            rect_texto_retry.midtop = POSICION_RETRY

            texto_exit = self.fuente_misc.render("PRESS ESC TO GO TO MAIN MENU", False, WHITE)
            rect_texto_exit = texto_exit.get_rect()
            rect_texto_exit.midtop = POSICION_EXIT

            self.screen.blit(self.fondo_game_over, ORIGIN)

            
            self.screen.blit(texto_game_over, rect_texto_game_over)
            self.screen.blit(texto_exit, rect_texto_exit)
            self.screen.blit(texto_final_score, rect_texto_final_score)
            self.screen.blit(texto_retry, rect_texto_retry)
            self.screen.blit(texto_high_score, rect_texto_high_score)

            pygame.display.flip()


    def reiniciar_juego(self):
        self.score = 0
        self.sprites.remove(self.personaje, self.barra_vida)
        self.sprites.empty()
        self.cuchillo.empty()
        self.enemigos.empty()
        self.diamante.empty()
        self.plata.empty()
        self.oro.empty()
        self.heal.empty()

        self.personaje = Personaje(START_POS)
        self.agregar_sprite(self.personaje)
        self.barra_vida = Barra_vida(POSICION_VIDA)
        self.agregar_sprite(self.barra_vida)
        self.agregar_sprite(self.cuchillo)
        self.agregar_cuchillos(self.cuchillo)
        self.agregar_enemigos(self.enemigos)
        self.agregar_sprite(self.plataforma)
        self.agregar_sprite(self.plataforma_2)
        self.agregar_sprite(self.plataforma_3)
        self.agregar_sprite(self.plataforma_suelo)

    def pause(self):
        self.flag_pause = True
        self.musica.stop()
        self.musica_g.play(-1)
        while self.flag_pause:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        self.flag_pause = False
                        self.musica_g.stop()
                        self.musica.play(-1)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        self.flag_pause = False
                        self.musica_g.stop()
                        self.menu_inicio()
                elif evento.type == pygame.QUIT:
                    self.exit()

            texto_pause = self.fuente.render("PAUSE", False, WHITE)
            rect_texto_pause = texto_pause.get_rect()
            rect_texto_pause.midtop = POSICION_GAME_OVER

            texto_continue = self.fuente_misc.render("PRESS M1 TO CONTINUE PLAYING", False, WHITE)
            rect_texto_continue = texto_continue.get_rect()
            rect_texto_continue.midtop = POSICION_RETRY

            texto_exit = self.fuente_misc.render("PRESS ESC TO GO TO MAIN MENU", False, WHITE)
            rect_texto_exit = texto_exit.get_rect()
            rect_texto_exit.midtop = POSICION_EXIT

            texto_current_score = self.fuente_final_score.render(f"CURRENT SCORE: {self.score}", False, WHITE)
            rect_texto_current_score = texto_current_score.get_rect()
            rect_texto_current_score.midtop = POSICION_FINAL_SCORE

            self.screen.blit(self.fondo_game_over, ORIGIN)

            self.screen.blit(texto_pause, rect_texto_pause)
            self.screen.blit(texto_exit, rect_texto_exit)
            self.screen.blit(texto_continue, rect_texto_continue)
            self.screen.blit(texto_current_score, rect_texto_current_score)

            pygame.display.flip()

    def cargar_puntaje(self):
        try:
            with open(".\src\puntajes.json", "r") as file:
                puntuacion_alta = json.load(file)
        except FileNotFoundError:
            return False
        
        return puntuacion_alta


    def guardar_puntaje(self, puntaje):
        puntajes = {}

        puntajes["puntaje"] = puntaje

        lista_levantada = self.cargar_puntaje()

        if lista_levantada:
            lista_levantada.append(puntajes)
            with open(".\src\puntajes.json", "w") as file:
                json.dump(lista_levantada, file, indent=2, separators= (", "," : "))
        else:
            self.lista_puntaje.append(puntajes)
            with open(".\src\puntajes.json", "w") as file:
                json.dump(self.lista_puntaje, file, indent=2, separators= (", "," : ") )

    def exit(self):
        pygame.quit()
        sys.exit()