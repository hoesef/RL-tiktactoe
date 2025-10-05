from game import Game
from agents import *

def train(agent, oponent, iterations=1000000):
    game = 0

    for i in range(iterations):
        agent.game.reset()
        game += 1
        while not agent.game.game_finished:
            agent.act()
            if not agent.game.game_finished:
                oponent.act()
            
        agent.learn()
    
    for b, v in agent.value_function.items():
        print(b, v)
    print(agent.epsilon)

if __name__ == '__main__':
    game = Game()
    agent = SmartAgent(game)
    oponent = RandomAgent(game)

    train(agent, oponent)