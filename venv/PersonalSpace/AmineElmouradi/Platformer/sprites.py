from settings import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image;get_rect()
        self.vx = 0
        self.vy = 0


        def update(self):
            self.vx = 0
            keys = pg.keys.get_pressed()

