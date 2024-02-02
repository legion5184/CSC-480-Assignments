"""
Tic Tac Toe Player
"""
# This is the solution file that I tested

import math
import random
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None


def initial_state():
  """
  Returns starting state of the board.
  """
  return [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Scan board for entries and determine next player:

    X_count = 0
    O_count = 0
    EMPTY_count = 0

    for row in board:
      X_count += row.count(X)
      O_count += row.count(O)
      EMPTY_count += row.count(EMPTY)

    # If X has more squares than O, its O's turn:
    if X_count > O_count:
      return O
    # Otherwise it is X's turn:
    else:
      return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i represents the board row, j the board column, both 0, 1 or 2
    The actions are represented as the tuple (i, j) where the piece can be placed.
    """
    action_set = set()

    for i in range(board):
        for j in range(board[i]):
            if board[i][j] == EMPTY:
                action_set.add((i, j))

    return action_set




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    # Check move is valid:
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
      raise InvalidActionError(action, board, 'Result function given an invalid board position for action: ')
    elif board[i][j] != EMPTY:
      raise InvalidActionError(action, board, 'Result function tried to perform invalid action on occupaied tile: ')

    # Make a deep copy of the board and update with the current player's move:
    board_copy = deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    otherwise return None
    """

    # Check rows:
    for row in board:
        if all([cell == X for cell in row]):
            return X
        elif all([cell == O for cell in row]):
            return O

    # Check columns:
    for col in range(3):
        if all([board[row][col] == X for row in range(3)]):
            return X
        elif all([board[row][col] == O for row in range(3)]):
            return O

    # Check diagonals
    if all([board[i][i] == X for i in range(3)]) or all([board[i][2 - i] == X for i in range(3)]):
        return X
    if all([board[i][i] == O for i in range(3)]) or all([board[i][2 - i] == O for i in range(3)]):
        return O

    # Otherwise no current winner, return None
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """ 
    # Game is over if it is a winning board or all tiles are full (no actions):

    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
      return 1
    elif winner(board) == 'O':
      return -1
    else:
      return 0

actions_explored = 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    #  TO BE IMPLEMENTED
    raise NotImplementedError

