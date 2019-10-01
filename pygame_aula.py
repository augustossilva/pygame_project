backgrond_image_filename = 'fundo.jpg'
mouse_image_filename = 'mouse.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Olá Mundo")

backgrond = pygame.image.load(backgrond_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(backgrond,(0,0))

        x, y = pygame.mouse.get_pos()
        x-= mouse_cursor_get_width() / 2
        x-= mouse_cursor_get_height() / 2
        screen.blit(mouse_cursor,(x, y))

        pygame.display.update()