import random

# Constants for players and board positions
EMPTY = ' '
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'

def print_board(board):
    # Prints the board state
    print('---------')
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' ')
        print('|')
    print('---------')

def get_empty_cells(board):
    # Returns a list of indices of empty cells on the board
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells.append((i, j))
    return empty_cells

def check_winner(board):
    # Checks if there is a winner or a tie
    # Returns the winner ('X' or 'O'), 'TIE' if it's a tie, or None if the game is not over yet
    # Checks rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    # Checks columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    # Checks diagonals
    if (board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[1][1]
    # Checks if it's a tie
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return 'TIE'
    return None

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner == AI_PLAYER:
        return 1
    elif winner == HUMAN_PLAYER:
        return -1
    elif winner == 'TIE':
        return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = AI_PLAYER
            eval_score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = HUMAN_PLAYER
            eval_score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval_score)
        return min_eval

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = AI_PLAYER
        move_score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if move_score > best_score:
            best_score = move_score
            best_move = (i, j)
    return best_move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Let's play Tic-Tac-Toe!")
    print_board(board)
    while True:
        # AI's turn
        if check_winner(board) is None:
            print("AI's turn...")
            i, j = get_best_move(board)
            board[i][j] = AI_PLAYER
            print_board(board)
        else:
            break
        
        # Human's turn
        if check_winner(board) is None:
            print("Your turn! Enter row (0-2) and column (0-2) separated by space:")
            valid_input = False
            while not valid_input:
                move = input().strip().split()
                if len(move) == 2:
                    row, col = move
                    if row.isdigit() and col.isdigit() and int(row) in range(3) and int(col) in range(3) and board[int(row)][int(col)] == EMPTY:
                        board[int(row)][int(col)] = HUMAN_PLAYER
                        valid_input = True
                if not valid_input:
                    print("Invalid move. Please try again.")
            print_board(board)
        else:
            break

    winner = check_winner(board)
    if winner == AI_PLAYER:
        print("AI wins!")
    elif winner == HUMAN_PLAYER:
        print("You win!")
    else:
        print("It's a tie!")

# Start the game
play_game()
