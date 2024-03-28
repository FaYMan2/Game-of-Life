import pygame
import numpy as np

class Cell:
    def __init__(self):
        self.clicked = 0
        

def drawGrid(grid_size):
    board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]

    pygame.init()
    window = pygame.display.set_mode((grid_size*50,grid_size*50))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if event.button == 1:
                    row = event.pos[1] // (grid_size*2)
                    col = event.pos[0] // (grid_size*2)
                    if board[row][col].clicked == 1:
                        board[row][col].clicked = 0
                    else :
                        board[row][col].clicked = 1

        window.fill(0)
        for iy, rowOfCells in enumerate(board):
            for ix, cell in enumerate(rowOfCells):
                color = (64, 64, 64) if cell.clicked == 1 else (164, 164, 164)
                pygame.draw.rect(window, color, (ix*(grid_size*2)+1, iy*(grid_size*2)+1, grid_size,grid_size))
        pygame.display.flip()

    pygame.quit()
    image = np.zeros(grid_size * grid_size)
    image = image.reshape(grid_size,grid_size)
    
    for iy,rowOfCells in enumerate(board):
        for ix,cell in enumerate(rowOfCells):
            image[iy][ix] = cell.clicked
    print(image)
    return image
