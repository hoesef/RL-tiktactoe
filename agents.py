from game import Game

class AgentTemplate():
    
    def __init__(self):
        pass

    def act(self, game):
        pass

    def learn(self, board_history):
        pass

from itertools import product
from random import uniform, choice
from utils import get_canonical_board

class SmartAgent(AgentTemplate):
    def __init__(self, piece, alpha=0.1, epsilon=1, epsilon_decay=0.999999):
        self.piece = piece
        self.alpha = alpha
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay

        self.value_function = {}
        self.generate_value_function()

    def generate_value_function(self):
        all_boards = product(' xo', repeat=9)

        for board in all_boards:
            x_num = board.count('x')
            o_num = board.count('o')

            if not (x_num == o_num or x_num == o_num + 1):
                continue

            x_winner = Game.has_winnier(board, 'x')
            o_winner = Game.has_winnier(board, 'o')

            if x_winner and o_winner:
                continue

            if x_winner and (x_num != o_num + 1):
                continue

            if o_winner and (x_num != o_num):
                continue

            board = get_canonical_board(board)

            if x_winner:
                self.value_function[board] = 1 * (self.piece == 'x')
            elif o_winner:
                self.value_function[board] = 1 * (self.piece == 'o')
            elif x_num + o_num == 9:
                self.value_function[board] = 0
            else:
                self.value_function[board] = 0.5
 
    def act(self, game):
        actions = game.valid_positions

        if uniform(0, 1) < self.epsilon:
            self.epsilon = max(self.epsilon * self.epsilon_decay, 0.1)
            action = choice(actions)
            game.place_piece(action)
            return

        self.epsilon = max(self.epsilon * self.epsilon_decay, 0.1)
        
        best_value = 0
        best_action = actions[0]

        for action in actions:
            potential_board = game.look_ahead(action)
            canonical = get_canonical_board(potential_board)
            if self.value_function[canonical] > best_value:
                best_value = self.value_function[canonical]
                best_action = action
        
        game.place_piece(best_action)

    def learn(self, board_history):
        for i in range(1, len(board_history)):
            current = get_canonical_board(board_history[i])
            nxt = get_canonical_board(board_history[i-1])
            self.value_function[current] += self.alpha * (self.value_function[nxt] - self.value_function[current])

class RandomAgent(AgentTemplate):

    def __init__(self):
        pass
    
    def act(self, game):
        actions = game.valid_positions
        action = choice(actions)
        game.place_piece(action)

if __name__ == '__main__':
    pass