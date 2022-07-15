import pygame
import itertools
import random
from .constants import BLACK, GREY, ROWS, WHITE, RED, SQUARE_SIZE, COLS, FONT
from .card import Card
from .slots import Slots


class Board:
    def __init__(self):
        self.board = []
        self.cards = self.opp_cards = 4
        self.cards_board = self.opp_cards_board = 0
        self.x_coords = []
        self.y_coords = []
        self.slots = Slots()
        self.current_bet = 0
        self.last_player = 0
        self.flipped = []
        # self.phase = 0
        self.create_board()

    def draw_cubes(self, win):
        win.fill(WHITE)
        y = 770 - COLS*175
        for row in range(ROWS):
            x = row*175 + 80
            pygame.draw.rect(win, GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE+20))
            pygame.draw.rect(win, GREY, (x, 650-y, SQUARE_SIZE, SQUARE_SIZE+20))
            self.x_coords.append(x)

        self.y_coords.append(y)
        self.y_coords.append(650-y)

    def draw_buttons(self, win):
        
        text_pass = FONT.render('pass', True, WHITE)
        text_bet = FONT.render('bet', True, WHITE)
        
        pygame.draw.rect(win, RED, (200, 720, 80, 50))
        pygame.draw.rect(win, BLACK, (500, 720, 80, 50))
        win.blit(text_bet, (220, 732))
        win.blit(text_pass, (512, 732))
    
    def display_current_bet(self, win):
        text = FONT.render('Current bet: ' + str(self.current_bet), True, BLACK)

        pygame.draw.rect(win, WHITE, (350, 370, 100, 60))
        win.blit(text, (320, 370))
    
    def get_card(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        player = 0
        random_1 = random.randint(1, 4)
        random_2 = random.randint(1, 4)

        y_coord = 770 - COLS*175
        self.y_coords.append(y_coord)
        self.y_coords.append(650-y_coord)
        for row in range(ROWS):
            x_coord = row*175 + 80
            self.x_coords.append(x_coord)
        
        for i in range(4):
            self.board.append([])
            for j in range(2):
                skull = False
                if j == 1:
                    player = -1
                    if i == random_1:
                        skull = True
                else:
                    player = 1
                    if i == random_2:
                        skull = True
                self.board[i].append(Card(i, j, player, skull))
# if bet <= len(self.slots.own)+len(self.slots.opp), make so that skulls are random in the hand
    def winner(self):
        skull = False
        if self.flipped and self.last_player != 0:
            for i in range(len(self.flipped)):
                if self.flipped[i].skull:
                    skull = True
                    winner = -1*self.last_player
                    if winner == -1:
                        print('You flipped a skull, WINNER: Player 2')
                    else:
                        print('You flipped a skull, WINNER: Player 1')
                    return winner
                elif i == self.current_bet-1 and not skull:
                    winner = self.last_player
                    if winner == -1:
                        print('You did not flip a skull, WINNER: Player 2')  
                    else:
                        print('You did not flip a skull, WINNER: Player 1')
                    return winner
                        
                    



    def play(self, card):
        self.board[card.row][card.col] = 0
        self.slots = card.play(self.slots)
        return 'play'

    def flip(self, card, player):
        self.last_player = player
        self.flipped.append(card)
        card.flip()
        return 'flip'

    def draw(self, win):
        self.draw_cubes(win)
        self.slots.draw_slots(win)
        self.draw_buttons(win)
        self.display_current_bet(win)
        for i in range(4):
            for j in range(2):
                if self.board[i][j] != 0:
                    card = self.board[i][j]
                    card.draw(win)
        for i in range(len(self.slots.own)):
            card = self.slots.own[i]
            card.draw(win)
        for i in range(len(self.slots.opp)):
            card = self.slots.opp[i]
            card.draw(win)
        
    def bet(self):
        if self.current_bet < len(self.slots.own)+len(self.slots.opp):
            self.current_bet +=1
            return 'bet'
        else:
            return None
    
    def pass_turn(self):
        return 'pass'

    def get_valid_actions(self, history):
        count_pass, count_bet = 0, 0
        phase = 0
        for x, y in itertools.groupby(history):
            if len(list(y)) >= 1:
                if x == 'pass':
                    count_pass = 1
        for i in range(len(history)):
            if history[i] == 'bet':
                count_bet = 1
                break
        if len(history) <= 1:
            valid_actions = ['play']
            phase = 0
        elif len(history) > 1:
            if count_bet == 0:
                valid_actions = ['play', 'bet']
                phase = 0
            if count_bet == 1:
                valid_actions = ['bet', 'pass']
                phase = 1
            if count_pass == 1:
                phase = 2
                valid_actions = ['flip']

        return phase, valid_actions
        

    
    
