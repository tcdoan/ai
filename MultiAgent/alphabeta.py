
def alpha_beta_search(gameState):
    """ Return the move along a branch of the game tree that 
    has the best possible value. A move is a pair of (column, row) 
    order corresponding to a legal move for the searching player.
    """
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for action in gameState.actions():
        val = min_value(gameState.result(action), alpha, beta)
        alpha = max(val, alpha)
        if val > best_score:
            best_score = val
            best_move = action
    return best_move

def min_value(gameState, alpha, beta):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    val = float("inf")
    for action in gameState.actions():
        val = min(val, max_value(gameState.result(action), alpha, beta))
        if val <= alpha:
            return val
        beta = min(val, beta)
    return val

def max_value(gameState, alpha, beta):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    val = float("-inf")
    for action in gameState.actions():
        val = max(val, min_value(gameState.result(action), alpha, beta))
        if val >= beta:
            return val
        alpha = max(alpha, val)
    return val
