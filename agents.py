from game import Game

class AgentTemplate():
    
    def __init__(self, game):
        self.game = game
        pass

    def act(self):
        pass

    def learn(self):
        pass

from itertools import product
from random import uniform, choice

class SmartAgent(AgentTemplate):
    def __init__(self, game, alpha=0.1, epsilon=1, epsilon_decay=0.999999):
        super().__init__(game)
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

            if x_winner:
                self.value_function[board] = 1
            elif o_winner or (x_num + o_num == 9):
                self.value_function[board] = 0
            else:
                self.value_function[board] = 0.5
 
    def act(self):
        actions = self.game.valid_positions

        if uniform(0, 1) < self.epsilon:
            self.epsilon = max(self.epsilon * self.epsilon_decay, 0.1)
            action = choice(actions)
            self.game.place_piece(action)
            return
        
        best_value = 0
        best_action = actions[0]

        for action in actions:
            potential_board = self.game.look_ahead(action)
            if self.value_function[potential_board] > best_value:
                best_value = self.value_function[potential_board]
                best_action = action
        
        self.game.place_piece(action)

    def learn(self):
        for i in range(1, len(self.game.board_history)):
            current = self.game.board_history[i]
            next = self.game.board_history[i-1]
            self.value_function[current] += self.alpha * (self.value_function[next] - self.value_function[current])

class RandomAgent(AgentTemplate):

    def __init__(self, game):
        super().__init__(game)
    
    def act(self):
        actions = self.game.valid_positions
        action = choice(actions)
        self.game.place_piece(action)

if __name__ == '__main__':
    pass