moved = False
attacked = False
captured = False
selected = False
moves = {}
row = []
board = []

def make_rows():
    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    piece = "--"
    board = []
    row = []
    for i, col in enumerate(column):
        for j in range(8):
            square = [f'{col}{(8-j)}', piece]
            board.append(square)        
            row = [board[r::8] for r in range(8)]
    return row

def start_position():
    row = make_rows()
    for bp in row[1]:
        bp[1] =  "bP"
    for wp in row[6]:
        wp[1] = "wP"
    for br in row[0][::7]:
        br[1] = "bR"
    for wr in row[7][::7]:
        wr[1] = "wR"
    for bn in row[0][1::5]:
        bn[1] = "bN"
    for wn in row[7][1::5]:
        wn[1] = "wN"
    for bb in row[0][2::3]:
        bb[1] = "bB"
    for wb in row[7][2::3]:
        wb[1] = "wB"
    row[0][3][1] = "bQ"
    row[0][4][1] = "bK"
    row[7][3][1] = "wQ"
    row[7][4][1] = "wK"
    initial_pos = row
    return initial_pos

def print_pos():
    position = start_position()
    print(position)


'''


def select_square(self):
    self.Piece.selected = False
    for r, rows in enumerate(row.start_position()):
        for s in self.rows:
            if self.square in s:
                ini = f"{s[0]}"
                piece = f"{s[1]}"
                selected = True
                return ini
def locate(self):
    if "nN" in self.row:
        print("nN")

print(self.row[0])
#def move_piece(ini, end):
#    row = start_position()
#    if  piece != "--":
#        moves = {
#            ini.square_selected("e4"):end 
#        }
#        row = moves
#        print(piece)
#        print(ini)
#        print(end)
#        #if piece in ini:
#
#        #for r, rows in enumerate(row):
#        #    for move in rows:
#        #        for piece in move:
#        #print(piece)
#            #print(moves)
#            #print(row)
#
#move_piece( "e4") 
'''