import pygame
import random
from player import Player
from asteroid import Asteroid
import os

WIDTH = 480
HEIGHT = 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configuração do jogo
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva dos Asteróides")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)

game_over = False  # adiciona a variável game_over para controlar a exibição da tela de "Game Over"
pontos = 0  # adiciona a variável pontos para controlar a contagem de pontos

pygame.mixer.music.load("data/sons/the_field_of_dreams.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, asteroids, False)
        if hits:
            game_over = True  # colisão detectada, configura a variável game_over para True
            pygame.mixer.music.load("data/sons/sounds_ping_pong_8bit/ping_pong_8bit_beeep.ogg") #musica da tela de game over
            pygame.mixer.music.play(0)

            pontos = 0  # reinicia a contagem de pontos

        # verifica se o jogador passou por um asteroide
        for a in asteroids:
            if a.rect.top > HEIGHT:
                a.kill()
                novo_asteroide = Asteroid()
                all_sprites.add(novo_asteroide)
                asteroids.add(novo_asteroide)
                pontos += 10  # adiciona 10 pontos quando o jogador passa por um asteroide

        screen.fill(BLACK)
        all_sprites.draw(screen)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Pontos: {}".format(pontos), True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()

    else:
        # novo loop para exibir a tela de "Game Over"
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over", True, WHITE) 
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        # espera que o jogador pressione a tecla "ESC" ou feche a janela do jogo para sair
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
