"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if action not in actions(board):
        raise Exception("This is not a valid action")
    else:
        i, j = action
        if player(new_board) == X:
            new_board[i][j] = X
        else:
            new_board[i][j] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def value(board):
        if terminal(board):
            return utility(board)

        if player(board) == X:
            best_score = -math.inf

            for action in actions(board):
                new_board =result(board, action=action)
                score = value(new_board)

                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf

            for action in actions(board):
                new_board = result(board, action=action)
                score = value(new_board)

                best_score = min(best_score, score)
            return best_score

    if player(board) == X:
        best_score = -math.inf
        best_move = None

        for action in actions(board):
            new_board = result(board, action=action)
            score = value(new_board)

            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        best_score = math.inf
        best_move = None

        for action in actions(board):
            new_board = result(board, action=action)
            score = value(new_board)

            if score < best_score:
                best_score = score
                best_move = action
        return best_move