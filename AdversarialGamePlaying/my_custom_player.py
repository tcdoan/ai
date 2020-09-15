from sample_players import DataPlayer
import random
import math

class CustomPlayer(DataPlayer):
    """ Implementation of Monte Carlo tree search agent to play knight's Isolation
    """    
    def get_action(self, state):
        """ Employ MCTS adversarial search technique to choose an action 
        (a move) available in the current state.
        """        
        v0 = MctNode(state, None)
        while True:
            _, v1 = self.treePolicy(v0)
            delta = self.defaultPolicy(v1.state)
            self.backupNegaMax(v1, delta)
            action, _ = v0.bestChild(0)
            self.queue.put(action)
            
    def treePolicy(self, v):
        a = None
        while v.nonTerminal():
          if not v.fullyExpanded(): 
              return v.expand()
          else: 
              a, v = v.bestChild(1.4)
        return a, v

    def backupNegaMax(self, v, delta):
        while v is not None:
            v.N, v.Q = v.N + 1, v.Q + delta
            delta = -delta
            v = v.parent

    def defaultPolicy(self, state):
        s = state
        player = s.player()
        while not s.terminal_test():
            a = random.choice(s.actions())
            s = s.result(a)
        return 1 if s.utility(player)  < 0 else -1

    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)

class MctNode:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.untriedActions = state.actions()
        self.actions = []
        self.children = []
        self.Q = 0
        self.N = 0
                    
    def nonTerminal(self):
        return (not self.state.terminal_test())

    def fullyExpanded(self):
        return len(self.untriedActions) == 0

    def bestChild(self, c = 1.4):
        bestAction, bestChild, bestReward = None, None, float("-inf")
        for a, v2 in zip(self.actions, self.children):
            v2Reward = v2.Q/v2.N + c * math.sqrt(2 * math.log(self.N) / v2.N)
            if v2Reward > bestReward:
                bestReward, bestAction = v2Reward, a
                bestChild = v2
        return bestAction, bestChild

    def expand(self):
        a = random.choice(self.untriedActions)
        self.untriedActions.remove(a)
        s2 = self.state.result(a)
        v2 = MctNode(s2, self)
        self.actions.append(a)
        self.children.append(v2)
        return a, v2
