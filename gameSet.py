class Piece:
    def __init__(self, piece_id, piece_name, color_team, max_range, r_value):
        self.piece_id = piece_id
        self.piece_name = piece_name
        self.color_team = color_team
        self.max_range = max_range
        self.r_value = r_value
        self.moved = False
        self.attacked = False
        self.captured = False
        self.selected = False

    def selectPiece(self):
        self.col = input('select Col')
        self.row = input('select Row')

        print(self.selected)

        return self.selected

    def move(self):
        final_col = input(int('select destiny col'))
        final_row = input(int('select destiny row'))
    
    def capture(self):
        pass

x_ghost =  Piece("--", "Ghost", None, 0, 0)
b_pawn =   Piece("bP", "Pawn", "BLACK", 1, 1)
w_pawn =   Piece("wP", "Pawn", "WHITE", 1, 1) 
b_rook =   Piece('bR', "Rook", "BLACK", 7, 5)
w_rook =   Piece("wR", "Rook", "WHITE", 7, 5)
b_knight = Piece("bN", "Knight", "BLACK", 2, 3)
w_knight = Piece("wN", "Knight", "WHITE", 2, 3)
b_bishop = Piece("bB", "Bishop", "BLACK", 7, 3)
w_bishop = Piece("wB", "Bishop", "WHITE", 7, 3)
b_queen =  Piece("bQ", "Queen", "BLACK", 7, 9)
w_queen =  Piece("wQ", "Queen", "WHITE", 7, 9)
b_king =   Piece("bK", "King", "BLACK", 1, 100)
w_king =   Piece("wK", "King", "WHITE", 1, 100)

board = [
    [["a", 8, "--"], ["b", 8, "--"], ["c", 8, "--"], ["d", 8, "--"], ["e", 8, "--"], ["f", 8, "--"], ["g", 8, "--"], ["h", 8, "--"]],
    [["a", 7, "--"], ["b", 7, "--"], ["c", 7, "--"], ["d", 7, "--"], ["e", 7, "--"], ["f", 7, "--"], ["g", 7, "--"], ["h", 7, "--"]],
    [["a", 6, "--"], ["b", 6, "--"], ["c", 6, "--"], ["d", 6, "--"], ["e", 6, "--"], ["f", 6, "--"], ["g", 6, "--"], ["h", 6, "--"]],
    [["a", 5, "--"], ["b", 5, "--"], ["c", 5, "--"], ["d", 5, "--"], ["e", 5, "--"], ["f", 5, "--"], ["g", 5, "--"], ["h", 5, "--"]],
    [["a", 4, "--"], ["b", 4, "--"], ["c", 4, "--"], ["d", 4, "--"], ["e", 4, "--"], ["f", 4, "--"], ["g", 4, "--"], ["h", 4, "--"]],
    [["a", 3, "--"], ["b", 3, "--"], ["c", 3, "--"], ["d", 3, "--"], ["e", 3, "--"], ["f", 3, "--"], ["g", 3, "--"], ["h", 3, "--"]],
    [["a", 2, "--"], ["b", 2, "--"], ["c", 2, "--"], ["d", 2, "--"], ["e", 2, "--"], ["f", 2, "--"], ["g", 2, "--"], ["h", 2, "--"]],
    [["a", 1, "--"], ["b", 1, "--"], ["c", 1, "--"], ["d", 1, "--"], ["e", 1, "--"], ["f", 1, "--"], ["g", 1, "--"], ["h", 1, "--"]],
]

# initial position of all pieces

board[0][0][2] = b_rook.piece_id
board[0][7][2] = b_rook.piece_id
board[0][1][2] = b_knight.piece_id
board[0][6][2] = b_knight.piece_id
board[0][2][2] = b_bishop.piece_id
board[0][5][2] = b_bishop.piece_id
board[0][3][2] = b_queen.piece_id
board[0][4][2] = b_king.piece_id
board[1][0][2] = b_pawn.piece_id
board[1][1][2] = b_pawn.piece_id
board[1][2][2] = b_pawn.piece_id
board[1][3][2] = b_pawn.piece_id
board[1][4][2] = b_pawn.piece_id
board[1][5][2] = b_pawn.piece_id
board[1][6][2] = b_pawn.piece_id
board[1][7][2] = b_pawn.piece_id

board[7][0][2] = w_rook.piece_id
board[7][7][2] = w_rook.piece_id
board[7][1][2] = w_knight.piece_id
board[7][6][2] = w_knight.piece_id
board[7][2][2] = w_bishop.piece_id
board[7][5][2] = w_bishop.piece_id
board[7][3][2] = w_queen.piece_id
board[7][4][2] = w_king.piece_id
board[6][0][2] = w_pawn.piece_id
board[6][1][2] = w_pawn.piece_id
board[6][2][2] = w_pawn.piece_id
board[6][3][2] = w_pawn.piece_id
board[6][4][2] = w_pawn.piece_id
board[6][5][2] = w_pawn.piece_id
board[6][6][2] = w_pawn.piece_id
board[6][7][2] = w_pawn.piece_id

# Some moves to test the board

board[6][4][2] = x_ghost.piece_id
board[4][4][2] = w_pawn.piece_id

board[1][4][2] = x_ghost.piece_id
board[3][4][2] = b_pawn.piece_id

board[7][6][2] = x_ghost.piece_id
board[5][5][2] = w_knight.piece_id

board[0][1][2] = x_ghost.piece_id
board[2][2][2] = b_knight.piece_id

board[7][5][2] = x_ghost.piece_id
board[4][2][2] = w_bishop.piece_id