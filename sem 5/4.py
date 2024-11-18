import math

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    for row in board:
        if " " in row:
            return None 
    
    return "Draw" 

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == "X":
        return -1 
    elif result == "O":
        return 1 
    elif result == "Draw":
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        display_board(board)
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move. Try again.")

        if check_winner(board) == "X":
            display_board(board)
            print("Congratulations! You win!")
            break
        elif check_winner(board) == "Draw":
            display_board(board)
            print("It's a draw!")
            break
        
        ai_move(board)
        
        if check_winner(board) == "O":
            display_board(board)
            print("AI wins!")
            break
        elif check_winner(board) == "Draw":
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
