def rotate_90(board):
    return (board[6], board[3], board[0], board[7], board[4], board[1], board[8], board[5], board[2])
            
def rotate_180(board):
    return (board[8], board[7], board[6], board[5], board[4], board[3], board[2], board[1], board[0])

def rotate_270(board):
    return (board[2], board[5], board[8], board[1], board[4], board[7], board[0], board[3], board[6])

def flip_horiz(board):
    return (board[2], board[1], board[0], board[5], board[4], board[3], board[8], board[7], board[6])

def flip_vert(board):
    return (board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2])

def flip_diag_1(board):
    return (board[8], board[5], board[2], board[7], board[4], board[1], board[6], board[3], board[0])

def flip_diag_2(board):
    return (board[0], board[3], board[6], board[1], board[4], board[7], board[2], board[5], board[8])

def get_canonical_board(board):
    board = board
    rot_90 = rotate_90(board)
    rot_180 = rotate_180(board)
    rot_270 = rotate_270(board)
    flip_v = flip_vert(board)
    flip_h = flip_horiz(board)
    flip_d1 = flip_diag_1(board)
    flip_d2 = flip_diag_2(board)

    canonical = min(board, rot_90, rot_180, rot_270, flip_v, flip_h, flip_d1, flip_d2)

    return canonical


if __name__ == '__main__':    
    board = ('x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', )
    board = get_canonical_board(board)
    print(board)