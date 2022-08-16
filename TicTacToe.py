import pygame, sys
import numpy as np


pygame.init()

WIDTH = 600
HEIGHT = 600
Line_Width = 15
BOARD_Rows = 3
BOARD_Cols = 3
RED = (255, 0, 0)
BG_Color = (65, 65, 65)
Line_Color = (114, 114, 114)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
window.fill(BG_Color)

# board
board = np.zeros( (BOARD_Cols, BOARD_Rows) )
#print(board)

# pygame.draw.line(window, RED, (10, 10), (300, 300), 10 )

def draw_lines():
    # First horizontal line
    pygame.draw.line (window, Line_Color, (0, 200), (600, 200), Line_Width)
    # Second horizontal line
    pygame.draw.line (window, Line_Color, (0, 400), (600, 400), Line_Width)

    # First vertical line
    pygame.draw.line (window, Line_Color, (200, 0), (200, 600), Line_Width)
    #Second vertical line
    pygame.draw.line (window, Line_Color, (400, 0), (400, 600), Line_Width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0 

def is_board_full():
    for row in range(BOARD_Rows):
        for col in range(BOARD_Cols):
            if board[row][col] == 0:
                return False
    else:
        return True
# Middle square availability check
print(is_board_full())
for row in range(BOARD_Rows):
        for col in range(BOARD_Cols):
            mark_square(row, col, 1)
print(is_board_full())

draw_lines()
# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    pygame.display.update()