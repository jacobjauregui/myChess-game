class Piece:
    def __init__(self, piece_id, max_range, r_value):
        self.piece_id = piece_id
        self.max_range = max_range
        self.r_value = r_value
        self.team = None
        self.moved = False
        self.attacked = False
        self.captured = False
        self.selected = False

    def move(self):
        pass

    def capture(self):
        pass

ghost = Piece(" ", 0, 0)
pawn = Piece("P", 1, 1,)
rook = Piece("R", 7, 5)
knight = Piece("N", 2, 3)
bishop = Piece("B", 7, 3)
queen = Piece("Q", 7, 9)
king = Piece("K", 1, 100)