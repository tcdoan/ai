from sample_players import DataPlayer
import random

class AlphabetaPlayer(DataPlayer):
    """ Implementation of Alpha–beta pruning adversarial search agent 
    to play knight's Isolation
    """    
    def get_action(self, state):
        """ Employ alpha–beta pruning search algorithm to decrease the 
        number of nodes that are evaluated by the minimax to obtain 
        an action (a move) available in the current state.
        """        
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            depth=5
            while True:
              action = self.alphaBeta(state, depth)
              self.queue.put(action)
              depth += 1

    def alphaBeta(self, state, depth):
        """ Return the move along a branch of the game tree that
        has the best possible value.	
        """
        def min_value(state, depth, alpha, beta):
            if state.terminal_test():
                return state.utility(self.player_id)
            if depth <= 0: 
                return self.score(state)

            v = float("inf")
            for a in state.actions():
                v = min(v, max_value(state.result(a), depth-1, alpha, beta))
                beta = min(beta, v)
                if v < alpha: 
                    return v
            return v

        def max_value(state, depth, alpha, beta):
            if state.terminal_test(): 
                return state.utility(self.player_id)
            if depth <= 0: 
                return self.score(state)

            v = float("-inf")
            for a in state.actions():
                v = max(v, min_value(state.result(a), depth-1, alpha, beta))
                alpha = max(alpha, v)
                if v > beta:
                    return beta
            return v

        # Alpha: Worst-case lower bound score that the MAX player could attain	
        # Beta: Worst-case upper bound score that the MIN player could attain	
        alpha = float("-inf")
        beta = float("inf")
        bestScore = float("-inf")
        bestAction = None

        for a in state.actions():	
            v = min_value(state.result(a), depth-1, alpha, beta)	
            alpha = max(v, alpha)
            if v > bestScore:
                bestScore = v
                bestAction = a

        if bestAction is None: 
            bestAction = random.choice(state.actions())
        return bestAction

    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)
