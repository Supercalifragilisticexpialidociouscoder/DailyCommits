import random
import time

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    win_states = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_states

def get_free_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            r, c = divmod(move, 3)
            if board[r][c] == " ":
                board[r][c] = "X"
                break
            else:
                print("Cell already taken!")
        except (ValueError, IndexError):
            print("Invalid move. Try again.")

def ai_move(board):
    free = get_free_positions(board)
    move = random.choice(free)
    board[move[0]][move[1]] = "O"
    print("AI is thinking...")
    time.sleep(1)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)
    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            ai_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            return
        elif check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            return
    print("It's a draw!")

if __name__ == "__main__":
    main()