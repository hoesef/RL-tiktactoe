from itertools import product
from random import choice, uniform

def print_board(board):
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |' + '\n' +
          "-------------" + '\n' +
          '| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |' + '\n' +
          "-------------" + '\n' +
          '| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |' + '\n')

def get_actions(board):
    return [x for x in range(0,9) if board[x] == ' ']

def finished(board):
    return (has_winner(board, 'x') or has_winner(board, 'o') or (board.count('x') + board.count('o') == 9))

def has_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def generate_value_function():

    board_states = {}
    
    all_boards = product(' xo', repeat=9)

    for board in all_boards:

        ##TODO: Get canonical representation
        ##TODO: Check if state in boards
        ##TODO: Break if it is
        ##TODO: Continue if not

        x_num = board.count('x')
        o_num = board.count('o')

        if not(x_num == o_num or x_num == o_num + 1):
            continue

        x_winner = has_winner(board, 'x')
        o_winner = has_winner(board, 'o')

        if x_winner and o_winner:
            continue

        if x_winner and (x_num != o_num + 1):
            continue

        if o_winner and (x_num != o_num):
            continue

        if x_winner:
            board_states[board] = 1
        elif o_winner or x_num + o_num == 9:
            board_states[board] = 0
        else:
            board_states[board] = 0.5

    return board_states

def take_action(board, action, player='x'):
    board = list(board)
    board[action] = player
    return tuple(board)

def select_action(board, value_function, epsilon):
    actions = get_actions(board)

    if uniform(0, 1) < epsilon:
        return choice(actions)
    
    best_value = 0
    best_action = actions[0]
    
    for action in actions:
        potential = take_action(board, action, 'x')
        if value_function[potential] > best_value:
            best_value = value_function[potential]
            best_action = action
    
    return best_action

def random_agent_step(board):
    action = choice(get_actions(board))
    board = take_action(board, action, 'o')
    return board

def train(iterations):
    value_function = generate_value_function()
    alpha = 0.1
    epsilon = 1
    epsilon_decay = 0.999999

    game = 0

    for i in range(iterations):
        board = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        episode_history = []
        game += 1
        while not finished(board):
            # Choose action
            episode_history = [board] + episode_history
            action = select_action(board, value_function, epsilon)
            epsilon = max(epsilon_decay * epsilon, 0.1)
            # Observe next board
            next_board = take_action(board, action)
            #Update value function
            board = next_board
            episode_history = [board] + episode_history
            # Check for game over
            if not finished(board):
                board = random_agent_step(board)

            episode_history = [board] + episode_history
            
        for i in range(1, len(episode_history)):
            value_function[episode_history[i]] += alpha * (value_function[episode_history[i-1]] - value_function[episode_history[i]])

    return value_function

def evaluate(games, value_function):
    wins, losses, draws = 0, 0, 0
    for i in range(games):
        board = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        while not finished(board):
            action = select_action(board, value_function, 0)
            board = take_action(board, action)
            print_board(board)
            if not finished(board):
                board = random_agent_step(board)
            print_board(board)
        if has_winner(board, 'x'):
            print("Agent won!")
            wins += 1
        elif has_winner(board, 'o'):
            print("Agent lost!")
            losses += 1
        else:
            print("Agent drew.")
            draws += 1

    print(f"Agent won: {wins} / {games} games")
    print(f"Agent lost: {losses} / {games} games")
    print(f"Agent drew: {draws} / {games} games")

        
def play(value_function, games=1):
    wins, losses, draws = 0, 0, 0
    for i in range(games):
        board = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        while not finished(board):
            action = select_action(board, value_function, 0)
            board = take_action(board, action)
            print_board(board)
            print(f"Agent rates this board: {value_function[board]}")
            if not finished(board):
                player = -1
                while player not in get_actions(board):
                    player = int(input("Enter your play (0-8): "))
                board = take_action(board, player, 'o')
            print_board(board)
        if has_winner(board, 'x'):
            print("Agent won!")
            wins += 1
        elif has_winner(board, 'o'):
            print("Agent lost!")
            losses += 1
        else:
            print("Agent drew.")
            draws += 1
    print(f"Agent won: {wins} / {games} games")
    print(f"Agent lost: {losses} / {games} games")
    print(f"Agent drew: {draws} / {games} games")

if __name__ == '__main__':
    # value_function = train(500000)
    # evaluate(50, value_function)
    # play(value_function, 5)

    a = 'x o x    '
    b = 'xxo o    '
    print(min(a, b))
