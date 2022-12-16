import myPieces as pz

n_pawn = pz.pawn.piece_id
w_pawn = pz.pawn.piece_id
n_rook = pz.rook.piece_id
w_rook = pz.rook.piece_id
n_knight = pz.knight.piece_id
w_knight = pz.knight.piece_id
n_bishop = pz.bishop.piece_id
w_bishop = pz.bishop.piece_id
n_king = pz.king.piece_id
w_king = pz.king.piece_id
n_queen = pz.queen.piece_id
w_queen = pz.queen.piece_id
ghost = pz.ghost.piece_id

board = [
    [["a", 8, ghost], ["b", 8, ghost], ["c", 8, ghost], ["d", 8, ghost], ["e", 8, ghost], ["f", 8, ghost], ["g", 8, ghost], ["h", 8, ghost]],
    [["a", 7, ghost], ["b", 7, ghost], ["c", 7, ghost], ["d", 7, ghost], ["e", 7, ghost], ["f", 7, ghost], ["g", 7, ghost], ["h", 7, ghost]],
    [["a", 6, ghost], ["b", 6, ghost], ["c", 6, ghost], ["d", 6, ghost], ["e", 6, ghost], ["f", 6, ghost], ["g", 6, ghost], ["h", 6, ghost]],
    [["a", 5, ghost], ["b", 5, ghost], ["c", 5, ghost], ["d", 5, ghost], ["e", 5, ghost], ["f", 5, ghost], ["g", 5, ghost], ["h", 5, ghost]],
    [["a", 4, ghost], ["b", 4, ghost], ["c", 4, ghost], ["d", 4, ghost], ["e", 4, ghost], ["f", 4, ghost], ["g", 4, ghost], ["h", 4, ghost]],
    [["a", 3, ghost], ["b", 3, ghost], ["c", 3, ghost], ["d", 3, ghost], ["e", 3, ghost], ["f", 3, ghost], ["g", 3, ghost], ["h", 3, ghost]],
    [["a", 2, ghost], ["b", 2, ghost], ["c", 2, ghost], ["d", 2, ghost], ["e", 2, ghost], ["f", 2, ghost], ["g", 2, ghost], ["h", 2, ghost]],
    [["a", 1, ghost], ["b", 1, ghost], ["c", 1, ghost], ["d", 1, ghost], ["e", 1, ghost], ["f", 1, ghost], ["g", 1, ghost], ["h", 1, ghost]],
]

board[0][0][2] = n_rook
board[0][7][2] = n_rook
board[7][0][2] = w_rook
board[7][7][2] = w_rook

board[0][1][2] = n_knight
board[0][6][2] = n_knight
board[7][1][2] = w_knight
board[7][6][2] = w_knight

board[0][2][2] = n_bishop
board[0][5][2] = n_bishop
board[7][2][2] = w_bishop
board[7][5][2] = w_bishop

board[0][3][2] = n_queen
board[7][3][2] = w_queen
board[0][4][2] = n_king 
board[7][4][2] = w_king 

board[1][0][2] = n_pawn
board[1][1][2] = n_pawn
board[1][2][2] = n_pawn
board[1][3][2] = n_pawn
board[1][4][2] = n_pawn
board[1][5][2] = n_pawn
board[1][6][2] = n_pawn
board[1][7][2] = n_pawn
board[6][0][2] = w_pawn
board[6][1][2] = w_pawn
board[6][2][2] = w_pawn
board[6][3][2] = w_pawn
board[6][4][2] = w_pawn
board[6][5][2] = w_pawn
board[6][6][2] = w_pawn
board[6][7][2] = w_pawn

print(board)
'''
def selectPiece():
    init_col = input('select Col')
    init_row = input('select Row')

    selected = board[init_col][init_row][2]
    print(selected)

    return selected
    final_col = input(int('select destiny col'))
    final_row = input(int('select destiny row'))

    board[final_col][final_row][2] = board[init_col][init_row][2]
selectPiece()
'''