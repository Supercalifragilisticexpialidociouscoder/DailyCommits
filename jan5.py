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

    def valid_moves(self, board, x, y):
        moves = []
        for dx, dy in [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if not board[ny][nx] or board[ny][nx].color != self.color:
                    moves.append((nx, ny))
        return moves

class Pawn(Piece):
    symbol = 'P'

    def valid_moves(self, board, x, y):
        moves = []
        direction = -1 if self.color == 'w' else 1
        # Move forward
        if 0 <= y + direction < 8 and not board[y + direction][x]:
            moves.append((x, y + direction))
            # First move double
            if (self.color == 'w' and y == 6) or (self.color == 'b' and y == 1):
                if not board[y + 2 * direction][x]:
                    moves.append((x, y + 2 * direction))
        # Captures
        for dx in [-1, 1]:
            nx = x + dx
            ny = y + direction
            if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] and board[ny][nx].color != self.color:
                moves.append((nx, ny))
        return moves

def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    # Place pieces
    for color, y_pawn, y_back in [('w', 6, 7), ('b', 1, 0)]:
        for x in range(8):
            board[y_pawn][x] = Pawn(color)
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for x, piece in enumerate(pieces):
            board[y_back][x] = piece(color)
    return board

def print_board(board):
    print("  a b c d e f g h")
    for y in range(8):
        print(8 - y, end=' ')
        for x in range(8):
            piece = board[y][x]
            if piece:
                s = piece.symbol if piece.color == 'w' else piece.symbol.lower()
                print(s, end=' ')
            else:
                print('.', end=' ')
        print(8 - y)
    print("  a b c d e f g h")

def parse_move(move):
    if len(move) != 4:
        return None
    x1 = ord(move[0]) - ord('a')
    y1 = 8 - int(move[1])
    x2 = ord(move[2]) - ord('a')
    y2 = 8 - int(move[3])
    if 0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8:
        return x1, y1, x2, y2
    return None

def main():
    board = create_board()
    turn = 'w'
    while True:
        print_board(board)
        print(f"{'White' if turn == 'w' else 'Black'}'s move (e.g. e2e4): ", end='')
        move = input().strip()
        if move == 'exit':
            break
        parsed = parse_move(move)
        if not parsed:
            print("Invalid move format.")
            continue
        x1, y1, x2, y2 = parsed
        piece = board[y1][x1]
        if not piece or piece.color != turn:
            print("No piece of yours at that position.")
            continue
        valid = piece.valid_moves(board, x1, y1)
        if (x2, y2) not in valid:
            print("Invalid move for that piece.")
            continue
        board[y2][x2] = piece
        board[y1][x1] = None
        turn = 'b' if turn == 'w' else 'w'

if __name__ == "__main__":
    main()