import sys

class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board, x, y):
        return []

    def __str__(self):
        return self.symbol

class King(Piece):
    symbol = 'K'

    def valid_moves(self, board, x, y):
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not board[ny][nx] or board[ny][nx].color != self.color:
                        moves.append((nx, ny))
        return moves

class Queen(Piece):
    symbol = 'Q'

    def valid_moves(self, board, x, y):
        return Rook(self.color).valid_moves(board, x, y) + Bishop(self.color).valid_moves(board, x, y)

class Rook(Piece):
    symbol = 'R'

    def valid_moves(self, board, x, y):
        moves = []
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not board[ny][nx]:
                        moves.append((nx, ny))
                    elif board[ny][nx].color != self.color:
                        moves.append((nx, ny))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Bishop(Piece):
    symbol = 'B'

    def valid_moves(self, board, x, y):
        moves = []
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not board[ny][nx]:
                        moves.append((nx, ny))
                    elif board[ny][nx].color != self.color:
                        moves.append((nx, ny))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Knight(Piece):
    symbol = 'N'

