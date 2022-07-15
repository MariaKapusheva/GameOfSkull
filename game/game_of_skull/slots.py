import math
import pygame
from .constants import ORANGE
from .card import Card

class Pixel:

    def __init__(self, screen, color, pos, size=2):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.size = size

    def update(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)

class Slots:
    def __init__(self):
        self.own = []
        self.opp = []

    def fill_slot(self, card, player):
        if player == 1:
            self.own.append(card)
            return self
        else:
            self.opp.append(card)
            return self

        

    def draw_slots(self, win):
        for k in range(4):
            for j in range(2):
                pixels = []
                x = 175 * k + 176
                if j == 1:
                    y = 175*j + 90
                else:
                    y = 500 - 175*j
                step = 4
                angle = 0
                for i in range(72):
                    x -= math.sin(angle*math.pi/180) * step
                    y += math.cos(angle*math.pi/180) * step 
                    angle += 5
                    pixels.append(Pixel(win, ORANGE, (int(x), int(y))))
                for p in pixels:
                    p.update()
                pixels.clear()

