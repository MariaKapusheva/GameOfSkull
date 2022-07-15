import pygame
from .board import Board
# from .player import Player
# TODO: handle errors, 
# put limits on actions: the player should not be able to play, pass or bet if they are not in the correct phase

# Known errors: self.board[card.row][card.col] = 0
# AttributeError: 'int' object has no attribute 'row'
# File "/home/maria/Downloads/Uni/BachelorsProject/game/game_of_skull/board.py", line 128, in get_valid_actions
#     return phase, valid_actions
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 1
        self.phase = 0
        self.actions = ['play', 'bet', 'pass', 'flip']
        self.valid_actions = []
        # self.player1 = Player(1, self.board.board[1])
        # self.player2 = Player(-1, self.board.board[0])
        # self.valid_actions = {'0': ('play', 'bet'), '1':('bet', 'pass'), '2': 'flip'}
        self.history = []

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()
    
    def get_action(self, row, col):
        if row == -2 and col == -2:
            action = 'bet'
        elif row == -3 and col == -3:
            action = 'pass'
        elif row == -1 or col == -1:
            action = ''
        elif type(col) != int:
            action = 'flip'
        else:
            action = 'play'
        return action
        
# might have to fix recursion
    def select(self, row, col):
        action = self.get_action(row, col)
        result = None
        if self.selected and action and action in self.valid_actions:
            #   if action == 'play' and self.board.get_card(row, col).player == self.turn:
            #   AttributeError: 'int' object has no attribute 'player'
            if action == 'play' and self.board.get_card(row, col).player == self.turn:
                result = self._move(row,col)
            elif action == 'bet':
                result = self._bet()
                self.board.display_current_bet(self.win)
            elif action == 'pass':
                result = self._pass_turn()
            elif action == 'flip':
                result = self._flip(row, int(col)) # it might fuck up here because we need slots' rows and cols
            if not result:
                self.selected = None
                self.select(row, col)
            
        else:
            if action == 'play':
                card = self.board.get_card(row, col)
                if card != 0 and card.player == self.turn:
                    self.selected = card
            elif action == 'bet' or action == 'pass':
                self.selected = action
            
            self.phase, self.valid_actions = self.board.get_valid_actions(self.history)
            print('-----------')
            for i in range(len(self.valid_actions)):
                print(self.valid_actions[i])
            return True

        return False

    def _move(self, row, col):
        card = self.board.get_card(row, col)
        if self.selected and self.phase == 0:
            self.history.append(self.board.play(card))
            self.change_turn()
        else:
            return False
        
        return True

    def _pass_turn(self):
        if self.selected and self.phase == 1:
            self.history.append(self.board.pass_turn())
            self.change_turn() 
        else:
            return False
        
        return True

    def _bet(self):
        if self.selected and (self.phase == 1 or self.phase == 0):
            result = self.board.bet()
            if result:
                self.history.append(self.board.bet())
                self.change_turn()
            else:
                return False
        else:
            return False

        return True
    
    def _flip(self, row, col):
        if col == 0:
            card = self.board.slots.own[row]
        else:
            card = self.board.slots.opp[row]
        if self.selected and self.phase == 2:
            self.history.append(self.board.flip(card, self.turn))
            #self.change_turn
        else:
            return False
        return True


    def change_turn(self):
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1



