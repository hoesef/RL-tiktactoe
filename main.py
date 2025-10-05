from game import Game
from agents import *

def train(game, agent, oponent, iterations=1000000):

    for i in range(iterations):
        game.reset()
        while not game.game_finished:
            agent.act(game)
            if not game.game_finished:
                oponent.act(game)
            
        agent.learn(game.board_history)
        oponent.learn(game.board_history)
    
    for b, v in agent.value_function.items():
        print(b, v)
    print(agent.epsilon)

def evaluate(game, agent, oponent, n_games):
    wins, losses, draws = 0, 0, 0
    for i in range(n_games):
        game.reset()
        while not game.game_finished:
            agent.act(game)
            game.display()
            if not game.game_finished:
                oponent.act(game)
                game.display()
        if game.winner == 'x':
            print("Agent won!")
            wins += 1
        elif game.winner == 'o':
            print("Agent lost!")
            losses += 1
        else:
            print("Agent drew.")
            draws += 1

    print(f"Agent won: {wins} / {n_games} games")
    print(f"Agent lost: {losses} / {n_games} games")
    print(f"Agent drew: {draws} / {n_games} games")

def play(game, agent, n_games=1):
    wins, losses, draws = 0, 0, 0
    for i in range(n_games):
        game.reset()
        while not game.game_finished:
            agent.act(game)
            game.display()
            if not game.game_finished:
                player = -1
                while player not in game.valid_positions:
                    player = int(input("Enter your play (0-8): "))
                game.place_piece(player)
            game.display()
        if game.winner == 'x':
            print("Agent won!")
            wins += 1
        elif game.winner == 'o':
            print("Agent lost!")
            losses += 1
        else:
            print("Agent drew.")
            draws += 1

    print(f"Agent won: {wins} / {n_games} games")
    print(f"Agent lost: {losses} / {n_games} games")
    print(f"Agent drew: {draws} / {n_games} games")
            

if __name__ == '__main__':
    game = Game()
    agent = SmartAgent()
    oponent = RandomAgent()
    # oponent = SmartAgent()

    train(game, agent, oponent, 500000)
    evaluate(game, agent, oponent, 50)

    play(game, agent, 3)