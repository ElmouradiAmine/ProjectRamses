import pygame

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello world!")

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WHITE)
    pygame.draw.rect(window,BLACK,[400,300,50,50])

    pygame.display.update()
pygame.quit()
quit()
