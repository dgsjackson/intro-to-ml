from games import game
from games import player
import random

class ConnectFour(game.Game):

    def _init_board(self):
        self.board = [["."] * 7 for _ in range(6)]

    def _process_move(self, move):
        if move in range(7) and self.board[0][move] == ".":
            if self.log: print("The move was valid")
            for i in range(7):
                if i == 6 or self.board[i][move] != ".":
                    self.board[i - 1][move] = self.current_player
                    self.move_pos = (i - 1, move)
                    break
            self._print_board()
        else:
            if self.log: print("The move was invalid")
    
    def _is_player_winner(self, player):
        return self._is_horizontal_win(player) or self._is_vertical_win(player) or self._is_diagonal_win(player, main=True) or self._is_diagonal_win(player, main=False)
  
    def _is_vertical_win(self, player):
        score = 0
        col = self.move_pos[1]
        for i in range(6):
            if self.board[i][col] == player:
                score += 1
                if (score == 4):
                    return True
            else:
                score = 0
        return False

    def _is_horizontal_win(self, player):
        score = 0
        row = self.move_pos[0]
        for i in range(7):
            if self.board[row][i] == player:
                score += 1
                if score == 4:
                    return True
            else:
                score = 0
        return False
      
    def _is_diagonal_win(self, player, main=True):
        score = 0
        for i in range(-3, 4):
            row = self.move_pos[0] + i if main else self.move_pos[0] - i
            col = self.move_pos[1] + i
            if row in range(6) and col in range(7) and self.board[row][col] == player:
                score += 1
                if score == 4:
                    return True
            else:
                score = 0
        return False
    
    def _format_move(self, move):
        return f"Column {move + 1}"
    

def choose_move_randomly(board):
    options = list(filter(lambda x: board[0][x] == ".", range(7)))
    return random.choice(options)

def choose_move_manually(board):
    col = None
    while col not in map(lambda x: str(x), range(7)):
        col = input("Enter a column between 1 and 7 for your move...\n")
    col_digit = int(col) - 1
    return col_digit

if __name__ == "__main__":
    player1 = player.Player(choose_move_manually)
    player2 = player.Player(choose_move_randomly)
    game = ConnectFour(player1, player2)
    game.run(log=True)