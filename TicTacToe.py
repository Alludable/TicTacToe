import pygame, sys
pygame.init()

WIDTH = 600
HEIGHT = 600
Line_Width = 15
RED = (255, 0, 0)
BG_Color = (65, 65, 65)
Line_Color = (114, 114, 114)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
window.fill(BG_Color)

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

draw_lines()
# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    pygame.display.update()