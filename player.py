import pygame


WIDTH = 480
HEIGHT = 600
FPS = 60
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/sprites/LUla (2).png")
        self.image = pygame.transform.scale(self.image, [50, 70])
        self.rect = pygame.Rect(200, 520, 100, 100)


#lógica
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4.5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4.5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0