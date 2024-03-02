def initialize_board():
    return [['' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def player_move(board, symbol):
    while True:
        try:
            row = int(input("Enter row number (0-2): "))
            col = int(input("Enter column number (0-2): "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            if board[row][col] != '':
                print("That position is already taken. Please choose another.")
                continue
            board[row][col] = symbol
            break
        except ValueError:
            print("Invalid input. Please enter integers.")

def check_win(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == symbol for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == symbol for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2-i] == symbol for i in range(3)):  # Check secondary diagonal
        return True
    return False

def check_tie(board):
    for row in board:
        for square in row:
            if square == '':
                return False  # If any square is empty, game is not tied
    return True  # All squares filled and no winner, so game is tied

def play_game():
    board = initialize_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn:")
        player_move(board, players[current_player])

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

play_game()
