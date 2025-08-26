class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.result = None
        self.log = False
        self._init_board()

    def _init_board(self):
        self.board = [["."] * 3 for _ in range(3)]

    def run(self, log=False):
        if self.player1 == None or self.player2 == None:
            raise Exception("Must have two players to start the game...")
        self.log = log
        if(self.log): print("Starting game...")
        
        self.current_player = 1

        while(self.result == None):
            print(f"Player {self.current_player}'s turn...")
            self._request_move()
            self.result = self._check_result()
            #next player turn
            self.current_player = 1 if self.current_player == 2 else 2

        #always print result
        self._print_result()

    
    def _print_result(self):
        result_desc = None
        result_desc = "Player 1 wins" if self.result == 1 else ("Player 2 wins" if self.result == 2 else "The game was a draw")
        print(result_desc)

    def _request_move(self):
        move = None
        board_copy = list(map(lambda x: x.copy(), self.board))
        if self.current_player == 1:
            move = self.player1.choose_move(board_copy)
        elif self.current_player == 2:
            move = self.player2.choose_move(board_copy)

        if (self.log): print(f"Player {self.current_player} chose the move: {self._format_move(move)}")

        self._process_move(move)


    def _process_move(self, move):
        raise NotImplementedError()

    
    def _check_result(self):
        if self._is_player_winner(self.current_player):
            return self.current_player
        
        if self._is_draw():
            # 0 means draw
            return 0

        return None

    def _is_player_winner(self, player):
        raise NotImplementedError()
    
    def _is_draw(self):
        return all(self.board[i][j] != "." for i in range(len(self.board)) for j in range(len(self.board[0])))
    
    def _print_board(self):
        for row in self.board:
            output = "| " + " ".join(map(lambda x: str(x), row)) + " |"
            print(output)

    def _format_move(self, move):
        raise NotImplementedError()