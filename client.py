'''
this is the client module
'''

import pygame
from grid import Grid

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'


surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

import threading
def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
import socket
HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

def receive_data():
    pass

create_thread(receive_data)
grid = Grid()


running = True
player = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                if grid.switch_player:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False


    surface.fill((0,0,0))

    grid.draw(surface)

    pygame.display.flip()