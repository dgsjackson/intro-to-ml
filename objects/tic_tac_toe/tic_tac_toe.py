class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [["."] * 3 for _ in range(3)]
        self.current_player = None
        self.result = None
        self.log = False

    def run(self, log=False):
        if self.player1 == None or self.player2 == None:
            raise Exception("Must have two players to start the game...")
        self.log = log
        if(self.log): print("Starting game...")
        
        self.current_player = 1

        while(self.result == None):
            print(f"Player {self.current_player}'s turn...")
            self._request_turn()
            self.result = self._check_result()

        #always print result
        self._print_result()

    
    def _print_result(self):
        result_desc = None
        result_desc = "Player 1 wins" if self.result == 1 else ("Player 2 wins" if self.result == 2 else "The game was a draw")
        print(result_desc)

    def _request_turn(self):
        move = None
        board_copy = list(map(lambda x: x.copy(), self.board))
        if self.current_player == 1:
            move = self.player1.choose_move(board_copy)
        elif self.current_player == 2:
            move = self.player2.choose_move(board_copy)

        if (self.log): print(f"Player {self.current_player} chose the move: {move[0] + 1, move[1] + 1}")

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

        self.current_player = 1 if self.current_player == 2 else 2

    
    def _check_result(self):
        if self._is_player_winner(1):
            return 1
        if self._is_player_winner(2):
            return 2
        
        if (all(self.board[i][j] != "." for i in range(3) for j in range(3))):
            # 0 means draw
            return 0

        return None

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
    
    def _print_board(self):
        for row in self.board:
            print(row)

    
class Player():

    def __init__(self, strategy):
        self.strategy = strategy

    def choose_move(self, board):
        return self.strategy(board)
    
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


                
player1 = Player(choose_move_manually)
player2 = Player(choose_move_randomly)
game = Game(player1, player2)
game.run(log = True)