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
