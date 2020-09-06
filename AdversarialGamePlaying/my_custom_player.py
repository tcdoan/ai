
from sample_players import DataPlayer

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state.

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            depth=5
            while True:
              self.queue.put(self.alphabeta(state, depth))
              depth += 1

    def alphabeta(self, state, depth):
        """ Return the move along a branch of the game tree that
        has the best possible value.
        """
        def min_value(state, depth, alpha, beta):
          if state.terminal_test(): return state.utility(self.player_id)
          if depth <= 0: return self.score(state)

          v = float("inf")
          for a in state.actions():
            v = min(v, max_value(state.result(a), depth-1, alpha, beta))
            beta = min(beta, v)
            if v < alpha: return v
          return v

        def max_value(state, depth, alpha, beta):
          if state.terminal_test(): return state.utility(self.player_id)
          if depth <= 0: return self.score(state)
          v = float("-inf")
          for a in state.actions():
            v = max(v, min_value(state.result(a), alpha, beta))
            alpha = max(alpha, v)
            if v > beta: return beta
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
        return bestAction

    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)

