from games import game
from games import player

class TicTacToe(game.Game):

    def _init_board(self):
        self.board = [["."] * 3 for _ in range(3)]

    def _process_move(self, move):
        #if the move is invalid, they lose their turn
        if (move != None
            and move[0] in [0, 1, 2] 
            and move[1] in [0, 1, 2] 
            and self.board[move[0]][move[1]] == "."):
            if (self.log): print("The move was valid")
            self.board[move[0]][move[1]] = self.current_player
            self._print_board()
        else:
            if (self.log): print("The move was invalid")

    def _is_player_winner(self, player):
        for row in self.board:
            if all(map(lambda x: x == player, row)):
                return True
        for i in range(3):
            if all(map(lambda x: x[i] == player, self.board)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def _format_move(self, move):
        return move[0] + 1, move[1] + 1
    
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

if __name__ == "__main__":
    player1 = player.Player(choose_move_manually)
    player2 = player.Player(choose_move_randomly)
    game = TicTacToe(player1, player2)
    game.run(log = True)