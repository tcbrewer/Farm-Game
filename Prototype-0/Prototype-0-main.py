import pygame
import os
pygame.font.init()

#caption
pygame.display.set_caption("Prototype 0!")
#window
WIDTH, HEIGHT = 825, 510 #thought a golden(-ish) rectangle would be cute here
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#colors (boring placeholders before we pick a palette)
WHT = (255, 255, 255)
BLK = (0, 0, 0)
RED = (255, 0, 0)
YLW = (255, 255, 0)
GRN = (0, 255, 0)
CYN = (0, 255, 255)
BLU = (0, 0, 255)
MAG = (255, 0, 255)
#frames per second (the one I chose is arbitrary)
FPS = 24


def draw_window():
    WIN.fill(GRN)


    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Without this, the x button doesn't work!!
                run = False
                pygame.quit()
        


if __name__ == "__main__":
    main()