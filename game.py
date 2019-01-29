import pygame
from grid import Grid
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = '400, 100' # Establish the upper
                            # corner window's position to display on the computer's
                            # screen
surface = pygame.display.set_mode((600, 600)) # set the size of the
                            # Tic- Tac - Toe board
pygame.display.set_caption('Tic-Tac-Toe') # Set the name of the board

grid = Grid() # create an instance of the class Grid




running = True # set the running variable to start the loop

player = 'x'

while running:
    for event in pygame.event.get(): # search in the pygame.event for QUIT.
                             # to make it possible to close the window
        if event.type == pygame.QUIT: # if click on the close button,
               #  end the program
               running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                # print(pos[0]//200, pos[1]//200)
                grid.get_mouse(pos[0]//200, pos[1]//200, player)
                if player == 'x':
                    player = 'o'
                else:
                    player = 'x'

                grid.print_grid()


    surface.fill((0, 0, 0)) # fill the surface with color black
    grid.draw(surface)   # draw the grid on the board using draw method
    # of the class Grid
    pygame.display.flip() # update the window