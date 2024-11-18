import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board):
    lines = board + [list(col) for col in zip(*board)] + [[board[i][i] for i in range(3)]] + [[board[i][2 - i] for i in range(3)]]
    if ['X'] * 3 in lines:
        return 'X'
    if ['O'] * 3 in lines:
        return 'O'
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O': return 10 - depth
    if winner == 'X': return depth - 10
    if is_full(board): return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if is_maximizing else 'X'
                scores.append(minimax(board, depth + 1, not is_maximizing))
                board[i][j] = ' '
    return max(scores) if is_maximizing else min(scores)

def best_move(board):
    best_score, move = -math.inf, None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score, move = score, (i, j)
    return move

def tic_tac_toe():
    board = [[' '] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'.")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:  # Player's turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    i, j = divmod(move, 3)
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        break
                    print("Cell already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number between 1 and 9.")
        else:  # AI's turn
            i, j = best_move(board)
            board[i][j] = 'O'

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return

    print("It's a draw!")

tic_tac_toe()
