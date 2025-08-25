import game
import player
    
def choose_move_randomly(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "."):
                return (i, j)
        
    return None

def choose_move_manually(board):
    row, col = None, None

    while(row not in ["1","2","3"] or col not in ["1","2","3"]):
        player_input = input("Enter your move... eg. '2,1' for 2nd row, 1st column)\n")
        split_input = player_input.split(",")
        if len(split_input) == 2:
            row, col = split_input
    
    row_digit = int(row) - 1
    col_digit = int(col) - 1

    return (row_digit, col_digit)

player1 = player.Player(choose_move_manually)
player2 = player.Player(choose_move_randomly)
game = game.Game(player1, player2)
game.run(log = True)