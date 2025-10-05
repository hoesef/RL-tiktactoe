def rotate_90(board):
    return ((board[6], board[3], board[0], board[7], board[4], board[1], board[8], board[5], board[2]),
            (6,3,0,7,4,1,8,5,2))

def rotate_180(board):
    return ((board[8], board[7], board[6], board[5], board[4], board[3], board[2], board[1], board[0]),
            (8,7,6,5,4,3,2,1,0))

def rotate_270(board):
    return ((board[2], board[5], board[8], board[1], board[4], board[7], board[0], board[3], board[6]),
            (2,5,8,1,4,7,0,3,6))

def flip_horiz(board):
    return ((board[2], board[1], board[0], board[5], board[4], board[3], board[8], board[7], board[6]),
            (2,1,0,5,4,3,8,7,6))

def flip_vert(board):
    return ((board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2]),
            (6,7,8,3,4,5,0,1,2))

def flip_diag_1(board):
    return ((board[8], board[5], board[2], board[7], board[4], board[1], board[6], board[3], board[0]),
            (8,5,2,7,4,1,6,3,0))

def flip_diag_2(board):
    return ((board[0], board[3], board[6], board[1], board[4], board[7], board[2], board[5], board[8]),
            (0,3,6,1,4,7,2,5,8))

def get_canonical_board(board):
    boards = {}
    board, key = board, (0,1,2,3,4,5,6,7,8)
    rot_90, key_90 = rotate_90(board)
    rot_180, key_180 = rotate_180(board)
    rot_270, key_270 = rotate_270(board)
    flip_v, key_v = flip_vert(board)
    flip_h, key_h = flip_horiz(board)
    flip_d1, key_d1 = flip_diag_1(board)
    flip_d2, key_d2 = flip_diag_2(board)

    boards[board] = key
    boards[rot_90] = key_90
    boards[rot_180] = key_180
    boards[rot_270] = key_270
    boards[flip_h] = key_h
    boards[flip_v] = key_v
    boards[flip_d1] = key_d1
    boards[flip_d2] = key_d2
    
    canonical = min(board, rot_90, rot_180, rot_270, flip_v, flip_h, flip_d1, flip_d2)
    key = boards[canonical]

    return (canonical, key)


if __name__ == '__main__':    
    board = ('x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', )
    board, key = get_canonical_board(board)
    print(board)