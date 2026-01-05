import sys

class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board, x, y):
        return []

    def __str__(self):
        return self.symbol

