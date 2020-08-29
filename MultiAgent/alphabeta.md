# Alpha-beta pruning #

## Alpha-beta #

Alpha-beta pruning allows the agent to avoid searching nodes that cannot lead to better outcomes
than what they've already searched by keeping track of the upper and lower bounds of the value for each branch. 

- The lower bound is called alpha, 
- and the upper bound is called beta.

At every state in the game tree:
- α represents the guaranteed worst-case score that the MAX player could achieve
- β represents the guaranteed worst-case score that the MIN player could achieve.

## Alpha-beta pruning implementation ##

```python

def alpha_beta_search(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value. A move is a pair of coordinates
    corresponding to a legal move for the searching player.
    Ignore the special case of calling this function from a terminal state.
    """
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for a in gameState.actions():
        v = min_value(gameState.result(a), alpha, beta)
        alpha = max(alpha, v)
        if v > best_score:
            best_score = v
            best_move = a
    return best_move

# TODO: modify the function signature to accept an alpha and beta parameter
def min_value(gameState, alpha, beta):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    v = float("inf")
    for a in gameState.actions():
        v = min(v, max_value(gameState.result(a), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

# TODO: modify the function signature to accept an alpha and beta parameter
def max_value(gameState, alpha, beta):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    v = float("-inf")
    for a in gameState.actions():
        v = max(v, min_value(gameState.result(a), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v
```alphabeta