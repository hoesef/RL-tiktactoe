# RL-tiktactoe
A simple reinforcement learning agent that learns to play tiktactoe.

## Overview
This is a very simple tabular, $\epsilon$-greedy reinforcement learning agent that learns to play tiktactoe. First all possible board states are created including invalid states, such as those with multiple winners, moves after a win, too many of one piece, etc. This is then filtered down to the set of all valid boards, and then further filtered down to the set of all unique board states.

Next these unique board states are assessed for their type ('x' win positions, 'o' win positions, draws, all other boards), the boards are then added as a key to a dictionary "value_function", with the value being either 1, 0, or 0.5. These serve as the agents initial assessment of each board state, and their values are learnt during training to reflect the actual benefit of a state for a given opponent.

The value function is updated with the simple equation:
$$
V(S_t) = V(S_t) + \alpha \cdot \left[V(S_{t+1}) - V(S_t)\right]
$$
where:
- $V(S_t)$ is the value of the board at time t
- $\alpha$ is the learning rate

In order to encourage early exploration, the agent is given an $\epsilon$ value and an $\epsilon$ decay value. With probability $\epsilon$ the agent will take a random (legal) action and the value of $\epsilon$ is reduced each timestep using the $\epsilon$ decay.

## Potential improvements:
### Hyperparameter tuning:
I have not spend very long tuning the hyperparameters, there are almost certainly better parameter values to be found.
### Code optimisations
This was just a quick project, I didn't really plan out anything and so nothing has been optimised. A different learning agent may be better suited to this task, a different class structure may be more logical or conform to better code standards (not really an optimisation but oh well).

The only optimization I did add was to reduce the "legal board states" down to purley the "unique board states". This reduced the state space down from 5,478 -> 765 boards.