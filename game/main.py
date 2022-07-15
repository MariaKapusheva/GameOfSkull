import pygame
from game_of_skull.constants import WIDTH, HEIGHT
from game_of_skull.board import Board
from game_of_skull.game import Game
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game of Skull')

def get_row_col_from_mouse(pos):
    x, y = pos
    n = 0
    row, col = -1, -1
    if y > 80 and y < 200:
        col =  1
    elif y > 520 and y < 700:
        col = 0

    if y > 220 and y < 340:
        col = 1.1
        print('here')
    elif y > 440 and y < 560:
        col = 0.1
        print('here')

    for i in range(4):
        n = 175 * i + 130
        if x < n + 50 and x > n - 50:
            row = i
    
    if (row == -1 or col == -1) and y < 770 and y > 720:
        if x < 280 and x > 200:
            row, col = -2, -2
        elif x < 580 and x > 500:
            row, col = -3, -3

    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

                # if row != -1 and col != -1:
                #     print(row)
                #     print(col)
                    # card = board.get_card(row, col)
                #     if card != 0:
                #         board.play(card)
                #     else:
                #         print("No card to move here")
                # else:
                #     print("Not a card")
        
        game.update()
    
    pygame.quit()

main()