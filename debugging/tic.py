#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Input validation loop for row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0,1,2]:
                    print("Invalid row. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer 0, 1, or 2.")
        
        # Input validation loop for col
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0,1,2]:
                    print("Invalid column. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer 0, 1, or 2.")
        
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        
        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
