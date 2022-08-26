from tabnanny import check
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

def check_win(player):
    # vertical win check
    for col in range(BOARD_Cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(BOARD_Rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player  == 1:
        color = Circle_Color
    elif player == 2:
        color == Cross_Color

    pygame.draw.line(window, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color == Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(window, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color == Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(window, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color == Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(window, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():  
    window.fill(BG_Color)
    draw_lines()
    player = 1
    for row in range(BOARD_Rows):
        for col in range(BOARD_Cols):
            board[row][col] = 0
draw_lines()

player = 1
game_over = False

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x-coordinate
            mouseY = event.pos[1] # y-coordinate
            
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win( player ):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win( player ):
                        game_over = True
                    player = 1
                
                draw_sprites()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: 
                game_over = False
                restart()    

    pygame.display.update()