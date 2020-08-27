
# Representing the Game State  for the mini-Isolation game 
# that meet the three requirements specified

# Game Class Requirements
# The game state object needs to enforce all of the rules of the game, and represent all of the 
# information describing a single configuration of the game at a specific point in time. 

# Isolation GameState class needs properties that can:
# - keep track of which cells are open and closed
# - identify which player has initiative (whose turn it is to move)
# - track the current position each player on the board

from copy import deepcopy

class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
    
    _parity: bool
        Keep track of active player initiative (which 
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player 2
    
    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player 1 is at (0, 0) and player 2 is at (1, 0)
    """

    def __init__(self, xlim=3, ylim=2):
        """The GameState class constructor performs required
        initializations when an instance is created. The class
        should:
        
        1) Keep track of which cells are open/closed
        2) Identify which player has initiative
        3) Record the current location of each player
        
        Parameters
        ----------
        self:
            instance methods automatically take "self" as an
            argument in python
        xlim:
            board dimension x
        ylim:
            board dimension y
        Returns
        -------
        None
        """
        self.MOVES = [(1, 0), (1, -1), (0, -1), (-1, -1),
                      (-1, 0), (-1, 1), (0, 1), (1, 1)]
        self._xlim = xlim
        self._ylim = ylim
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1
        self._player = 0
        self._player_locations = [None, None]

    def player(self):
        return self._player

    def actions(self):
        """ Return a list of legal actions for the active player         
        You are free to choose any convention to represent actions,
        but one option is to represent actions by the (row, column)
        of the endpoint for the token. For example, if your token is
        in (0, 0), and your opponent is in (1, 0) then the legal
        actions could be encoded as (0, 1) and (0, 2).
        """
        actions = self.liberties(self._player_locations[self._player])
        return actions

    def result(self, action):
        """ Return a new state that results from applying the given
        action in the current state
        """
        assert action in self.actions(), "Attempted to plan an illegal move"
        new_board = deepcopy(self)
        new_board._board[action[0]][action[1]] = 1
        new_board._player_locations[self._player] = action
        new_board._player ^= 1
        return new_board

    def terminal_test(self):
        """ return True if the current state is terminal,
        and False otherwise
        
        Hint: an Isolation state is terminal if _either_
        player has no remaining liberties (even if the
        player is not active in the current state)
        """
        terminated = (not self._has_liberties(self._player) or  
                      not self._has_liberties(1-self._player))
        return terminated

    def liberties(self, loc):
        """ Return a list of all open cells in the
        neighborhood of the specified location.  The list 
        should include all open spaces in a straight line
        along any row, column or diagonal from the current
        position. (Tokens CANNOT move through obstacles
        or blocked squares in queens Isolation.)
        """
        if loc is None: 
            return self._get_blank_spaces()
        moves = []
        for dx, dy in self.MOVES: # check each move direction
            _x, _y = loc
            while 0 <= _x + dx < self._xlim and 0 <= _y + dy < self._ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]: # found blocked cell
                    break
                moves.append((_x, _y))
        return moves

    def _has_liberties(self, player_id):
        """ Check to see if the specified player has any liberties """
        return any(self.liberties(self._player_locations[player_id]))

    def _get_blank_spaces(self):
        """ Return a list of blank spaces on the board."""
        blanks = [(x, y) for y in range(self._ylim) for x in range(self._xlim) if not self._board[x][y] ]
        return blanks

if __name__ == "__main__":
    # This code is only executed if "gameagent.py" is the run
    # as a script (i.e., it is not run if "gameagent.py" is
    # imported as a module)
    emptyState = GameState()  # create an instance of the object
