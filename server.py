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


def receive_data():
    global turn
    while true:
        data = conn.recv(1024).decode()
        data = data.split('-')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'O')

        print(data)



def waiting_for_connection():
    global connection_established, conn, addr
    conn, addr = sock.accept()
    print('client is connected')
    connection_established = True
    receive_data()


create_thread(waiting_for_connection)


grid = Grid()


running = True
player = "X"
turn = True
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]:

                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    # work for sending to client
                    cellX, cellY = pos[0] // 200, pos[1] // 200
                    grid.get_mouse(cellX, cellY, player)
                    send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'yourturn', playing).encode()
                    conn.send(send_data) # THAT'S HOW SERVER SENDS DATA
                    turn = False

                # if grid.switch_player:
                #     if player == "X":
                #         player = "O"
                #     else:
                #         player = "X"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False
    surface.fill((0,0,0))
    grid.draw(surface)
    pygame.display.flip()
