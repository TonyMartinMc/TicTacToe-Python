def draw_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")


def check_win(board, player):
    
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):  
            return True
    
    if all([board[i][i] == player for i in range(3)]):  
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  
        return True
    return False


def check_tie(board):
    return all([cell != " " for row in board for cell in row])

def main():
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X, Player 2: O")

    while not game_over:
        
        draw_board(board)

        
        try:
            row, col = map(int, input(f"Player {current_player}, enter row (0-2) and column (0-2): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        
        board[row][col] = current_player

        
        if check_win(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        
        elif check_tie(board):
            draw_board(board)
            print("It's a tie!")
            game_over = True
        
        else:
            current_player = "O" if current_player == "X" else "X"

    print("Thanks for playing!")

if __name__ == "__main__":
    main()