import math


def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    for row in board:
        for cell in row:
            if cell == "-":
                return None
    return "Tie"


def minimax(board, depth, alpha, beta, is_maximizing):
    result = evaluate(board)
    if result is not None:
        if result == "X":
            return 1
        elif result == "O":
            return -1
        else:
            return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = "-"
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = "-"
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score


def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "X"
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = "-"
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        result = evaluate(board)
        if result is not None:
            if result == "X":
                print("X wins!")
            elif result == "O":
                print("O wins!")
            else:
                print("It's a tie!")
            break

        if current_player == "X":
            row, col = find_best_move(board)
            board[row][col] = current_player
            current_player = "O"
        else:
            while True:
                row, col = map(int, input("Enter your move (row col): ").split())
                if board[row][col] == "-":
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            current_player = "X"


if __name__ == "__main__":
    play_game()
