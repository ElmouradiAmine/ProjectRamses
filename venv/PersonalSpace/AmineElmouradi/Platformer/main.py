
# Game Architecture learning!
import pygame
import random
from settings import *
from colors import *

class Game :
    def __init__(self):
        #Initialise the window ect
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.run()


    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False #if you stop playing the game (self.playing = False) then you stop the chole program 


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def show_start_screen(self):
        pass

    def show_gameover_screen(self):
        pass

    def close(self):
        pygame.quit()
        quit()


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()

g.close()