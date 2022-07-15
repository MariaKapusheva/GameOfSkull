import pygame
from .constants import SQUARE_SIZE, BLACK, RED, DARK, ROSE, SKULL, WHITE

class Card:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, player, skull):
        self.row = row
        self.col = col
        self.player = player
        self.skull = skull
        self.color = WHITE
        self.in_hand = True
        self.time_to_flip = False
        
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = 175 * self.row + 130
        if self.col == 1:
            self.y = 175*self.col - 45
        else:
            self.y = 640 - 175*self.col
    
    # def play_card(self):
    #     self.in_hand = False
    def play(self, slots):
        slots = slots.fill_slot(self, self.player)
        self.in_hand = False

        if self.player == 1:
            self.x = 175*(len(slots.own) - 1) + 130
            self.y = 500
            return slots
        else:
            self.x = 175*(len(slots.opp) - 1) + 130
            self.y = 175 + 90
            return slots
    
    def flip(self):
        self.time_to_flip = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        if self.player == -1 and not self.time_to_flip:
            pygame.draw.circle(win, self.color, (self.x, self.y), radius) 
            if self.skull:
                win.blit(SKULL, (self.x - SKULL.get_width()//2, self.y - SKULL.get_height()//2))
            else:
                win.blit(ROSE, (self.x - ROSE.get_width()//2, self.y - ROSE.get_height()//2))
            pygame.draw.circle(win, DARK, (self.x, self.y), radius + self.OUTLINE)
        elif self.player == 1 and self.in_hand and not self.time_to_flip:
            pygame.draw.circle(win, DARK, (self.x, self.y), radius + self.OUTLINE)
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)
            if self.skull:
                win.blit(SKULL, (self.x - SKULL.get_width()//2, self.y - SKULL.get_height()//2))
            else:
                win.blit(ROSE, (self.x - ROSE.get_width()//2, self.y - ROSE.get_height()//2))
        elif self.player == 1 and not self.in_hand and not self.time_to_flip:
            pygame.draw.circle(win, self.color, (self.x, self.y), radius) 
            if self.skull:
                win.blit(SKULL, (self.x - SKULL.get_width()//2, self.y - SKULL.get_height()//2))
            else:
                win.blit(ROSE, (self.x - ROSE.get_width()//2, self.y - ROSE.get_height()//2))
            pygame.draw.circle(win, DARK, (self.x, self.y), radius + self.OUTLINE)
        elif self.time_to_flip:
            pygame.draw.circle(win, DARK, (self.x, self.y), radius + self.OUTLINE)
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)
            if self.skull:
                win.blit(SKULL, (self.x - SKULL.get_width()//2, self.y - SKULL.get_height()//2))
            else:
                win.blit(ROSE, (self.x - ROSE.get_width()//2, self.y - ROSE.get_height()//2))


            


    def __repr__(self):
        return str(self.skull)
    
    
        
        