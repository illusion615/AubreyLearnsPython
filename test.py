# This file are used for module testing
import pygame
import sys
from pygame.locals import *

#from Utilities.utilityPygame import utilPygame

white = (255, 255, 255)
black = (0, 0, 0)
msg = 'Hello, This the first message to the world.'

pygame.init()
window = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
msgFont = pygame.font.SysFont('Arial', 20)


def msgbox(surface, text, pos, font, color=pygame.Color('white')):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


message = msgFont.render(msg, True, white)
msgPos = (
    (window.get_size()[0] - message.get_size()[0]) / 2,
    (window.get_size()[1] - message.get_size()[1]) / 2
)

while True:
    window.fill(black)
    message = msgFont.render(msg, True, white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                msg = 'key down pressed.'
                # Tuples value cannot be modified, and have to reconstruct the value.
                msgPos = (msgPos[0], msgPos[1] + 10)
            if event.key == K_UP:
                msg = 'key up pressed.'
                msgPos = (msgPos[0], msgPos[1] - 10)
            if event.key == K_LEFT:
                msg = 'key left pressed.'
                msgPos = (msgPos[0] - 10, msgPos[1])
            if event.key == K_RIGHT:
                msg = 'key right pressed.'
                msgPos = (msgPos[0] + 10, msgPos[1])
        if event.type = MOUSEBUTTONDOWN:
            
    msgbox = pygame.draw.rect(
        window,
        white,
        (
            msgPos[0] - 10,
            msgPos[1] - 10,
            message.get_rect()[2] + 20,
            message.get_rect()[3] + 20
        ),
        3)
    window.blit(message, msgPos)
    pygame.display.update()
