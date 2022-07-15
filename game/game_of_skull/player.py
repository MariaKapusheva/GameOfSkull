import pygame
from .board import Board
from .card import Card

class Player:
    def __init__(self, player_id, cards):
        self.player_id = player_id
        self.actions = []
        self.card_slots = []
        self.cards_hand = cards
        self.current_bet = 0
        self.flip = False
        

    def winner(self, slots):
        if self.current_bet != 0:
            self.final(slots)

    def bet(self, current_bet):
        self.current_bet = current_bet

    def final(self):
        pass

    

