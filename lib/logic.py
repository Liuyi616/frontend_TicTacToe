# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    tie = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X' and board[i][j] != 'O':
                tie = False
                break
    _to_win = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]],
               [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
               [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
               [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    for r in _to_win:
        if board[r[0][0]][r[0][1]] == board[r[1][0]][r[1][1]] == board[r[2][0]][r[2][1]] and board[r[0][0]][r[0][1]]:
            return board[r[0][0]][r[0][1]]
    if tie:
        return 'Tie'
    else:
        return None  # FIXME


def other_move(move):
    """Given the character for a player, returns the other player."""
    if move == 'X':
        return 'O'
    return "X"  # FIXME





def print_board(board):
    print("\t{0} | {1} | {2}".format(board[0][0], board[0][1], board[0][2]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[1][0], board[1][1], board[1][2]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[2][0], board[2][1], board[2][2]))


def ai_move_step(valid, board):
    import random
    pos = random.sample(valid, 1)[0]
    valid.remove(pos)
    pos = int(pos)
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    board[row][col] = 'O'
    
    return get_winner(board)
def ai_move(valid, board):
    import random
    print("This is AI's turn!")
    print_board(board)
    pos = random.sample(valid, 1)[0]
    valid.remove(pos)
    pos = int(pos)
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    board[row][col] = 'O'
    print("AI select the chess position: %g" % (row * 3 + col + 1))
    return get_winner(board)

def stepsCounter(board, player):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                counter += 1
    return counter