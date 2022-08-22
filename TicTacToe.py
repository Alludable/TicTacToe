import pygame, sys
import numpy as np


pygame.init()

WIDTH = 600
HEIGHT = 600
Line_Width = 15
BOARD_Rows = 3
BOARD_Cols = 3
CIRCLE_Radius = 60
CIRCLE_Width = 15
CROSS_Width = 25
SPACE = 55
RED = (255, 0, 0)
BG_Color = (65, 65, 65)
Line_Color = (114, 114, 114)
Circle_Color = (0, 0, 0)
Cross_Color = (255, 255, 255)

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

def draw_sprites():
    for row in range(BOARD_Rows):
        for col in range(BOARD_Cols):
            if board[row][col] == 1:
                pygame.draw.line(window, Cross_Color, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_Width)
                pygame.draw.line(window, Cross_Color, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_Width)
            elif board[row][col] == 2:
                 pygame.draw.circle(window, Circle_Color ,(int( col * 200 + 100), int( row * 200 + 100)), CIRCLE_Radius, CIRCLE_Width)
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0 

def is_board_full():
    for row in range(BOARD_Rows):
        for col in range(BOARD_Cols):
            if board[row][col] == 0:
                return False
    
    return True


draw_lines()

player = 1

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] # x-coordinate
            mouseY = event.pos[1] # y-coordinate
            
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1
                
                draw_sprites()
                
            


    pygame.display.update()