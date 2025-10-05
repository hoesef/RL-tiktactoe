class Game():

    def __init__(self):
        self.board = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        self.board_history = [self.board]
        self.player = 'x'
        self.winner = ' '

    @property
    def game_finished(self):
        x_winner = self.has_winnier(self.board, 'x')
        o_winner = self.has_winnier(self.board, 'o')
        if x_winner:
            self.winner = 'x'
        if o_winner:
            self.winner = 'o'
        return (x_winner or o_winner or self.board.count(' ') == 0)
    
    @property
    def valid_positions(self):
        return [i for i in range(9) if self.board[i] == ' ']
    
    @classmethod
    def has_winnier(cls, board, player):
        return ((board[0] == player and board[1] == player and board[2] == player) or
                (board[3] == player and board[4] == player and board[5] == player) or
                (board[6] == player and board[7] == player and board[8] == player) or
                (board[0] == player and board[3] == player and board[6] == player) or
                (board[1] == player and board[4] == player and board[7] == player) or
                (board[2] == player and board[5] == player and board[8] == player) or
                (board[0] == player and board[4] == player and board[8] == player) or
                (board[2] == player and board[4] == player and board[6] == player))
    
    def reset(self):
        self.board = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        self.board_history = [self.board]
        self.player = 'x'
        self.winner = ' '

    def display(self):
        print('| ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' |' + '\n' +
              "-------------" + '\n' +
              '| ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' |' + '\n' +
              "-------------" + '\n' +
              '| ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' |' + '\n')

    def look_ahead(self, pos):
        board = list(self.board)
        board[pos] = self.player
        return tuple(board)

    def place_piece(self,pos):
        board = list(self.board)
        board[pos] = self.player
        self.board = tuple(board)
        self.board_history = [self.board] + self.board_history
        self.player = 'x' if self.player == 'o' else 'o'

if __name__ == '__main__':
    board = Game()
    print(board.game_finished)