# Opening Book #

An opening book isn't specific to Minimax search. It's a general technique for game playing that builds on the intuitive idea that we can learn from experience which opening moves are most likely to result in a win. Opening books are usually built by analyzing a large corpus of games between expert players to find the most promising opening lines.

If you don't have a large corpus of historical matches, then you can create a corpus by either using random rollouts (or by using your agent) to play many games while accumulating statistics on which opening moves are best. An opening book can be as simple as a dictionary `book = {hashable_game_state: action_to_take}` for as many pairs of game states and actions as you choose.

Keep in mind that opening books are estimates of the best move. It's possible for the book to learn bad moves, especially if you don't have much data or if your data is noisy. The game tree grows exponentially, so it can take an enormous number of games to collect reliable statistics on the opening moves. You can improve the quality of the estimates by incorporating more domain knowledge in the process (like the symmetries discussed for 5x5 Isolation).

## NOTE: ##

- Python3 uses a secure hashing scheme that makes object hashes (generally) non-portable between runs. 
The game state object in the project can safely be used as a key, but for this quiz you will need to use `state.hashable` as a key.

```python

import random

from gamestate import GameState

NUM_ROUNDS = 10

def build_table(num_rounds=NUM_ROUNDS):
    # Builds a table that maps from game state -> action
    # by choosing the action that accumulates the most
    # wins for the active player. (Note that this uses
    # raw win counts, which are a poor statistic to
    # estimate the value of an action; better statistics
    # exist.)
    from collections import defaultdict, Counter
    book = defaultdict(Counter)
    for _ in range(num_rounds):
        state = GameState()
        build_tree(state, book)
    return {k: max(v, key=v.get) for k, v in book.items()}

def build_tree(state, book, depth=2):
    if depth <= 0 or state.terminal_test():
        return -simulate(state)
    action = random.choice(state.actions())
    reward = build_tree(state.result(action), book, depth - 1)
    book[state.hashable][action] += reward
    return -reward

def simulate(state):
    player_id = state._parity
    while not state.terminal_test():
        state = state.result(random.choice(state.actions()))
    return -1 if state.utility(player_id) < 0 else 1
```
