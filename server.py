'''
this is the server module
threading and queue modules

https://www.tutorialspoint.com/python3/python_multithreading.htm
'''

import pygame
from grid import Grid
import os
import queue


os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'


surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe Server')

import threading


def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()



import socket

# Define the socket

HOST = '127.0.0.1'
PORT = 65432

connection_established = False
conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1) # how many connections you need, for 5 players use 5


def recieve_data():
    while true:
        data = conn.recv(1024).decode()
        print(data)



def waiting_for_connection():
    global connection_established, conn, addr
    conn, addr = sock.accept()
    print('client is connected')
    connection_established = True
    recieve_data()


create_thread(waiting_for_connection)


grid = Grid()


running = True
player = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                # work for sending to client
                cellX, cellY = pos[0] // 200, pos[1] // 200
                grid.get_mouse(cellX, cellY, player)
                send_data = '{}-{}'.format(cellX, cellY).encode()
                conn.send(send_data) # THAT'S HOW SERVER SENDS DATA

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
