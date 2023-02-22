import tkinter as tk
import gameSet as gs
class JakeChess:
    def __init__(self):
        self.root = tk.Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.geometry = f'{self.w}x{self.h}'
        self.root.resizable(True, True)
        self.sq_white = '#F0D9B5'
        self.sq_black = '#B58863'
        self.wood = '#57241E'
        self.silver = '#C3C1C3'
        self.carbon = '#232223'
        self.dark = '#404040'
        self.frm_board = tk.Frame(
            self.root,
            background=self.wood,
            borderwidth=15,
            cursor="hand2",
            relief="raised"
        )
        self.board_drawing = False
        self.lbl_coord = tk.Canvas()


    def main_loop(self):
        self.root.title("JakeChess")
        self.root.iconbitmap("./assets/chessicon.ico")
        self.root.configure(background=self.dark)
        self.frm_board.pack(side='top', expand=False)
        self.root.mainloop()
        
    def make_board(self):
        self.rows = [8, 7, 6, 5, 4, 3, 2, 1]
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.w_frames = []
        self.w_canvas = []
        self.b_frames = []
        self.b_canvas = []
        self.white_squares = []
        self.black_squares = []
        for r, row in enumerate(self.rows):
            for c, column in enumerate(self.columns):
                if (r + c) % 2 == 0:
                    self.w_sq = gs.Square(row, column, 'white', 'w_ghost')
                    self.frm_w_sq = tk.Frame(self.frm_board, background=self.sq_white, width=64, height=64, highlightthickness=0)
                    self.frm_w_sq.grid(row=r, column=c)
                    self.w_can = tk.Canvas(self.frm_w_sq, background=self.sq_white, width=64, height=64, highlightthickness=0)
                    self.w_can.create_text(60,60,text=self.w_sq.name_sq, fill='#232223', anchor='se')
                    self.w_can.pack()
                    self.w_frames.append(self.frm_w_sq)
                    self.w_canvas.append(self.w_can)
                    self.white_squares.append(self.w_sq.name_sq)
                else:
                    self.b_sq = gs.Square(row, column, 'black', 'b_ghost')
                    self.frm_b_sq = tk.Frame(self.frm_board, background=self.sq_black, width=64, height=64, highlightthickness=0)
                    self.frm_b_sq.grid(row=r, column=c)
                    self.b_can = tk.Canvas(self.frm_b_sq, background=self.sq_black, width=64, height=64, highlightthickness=0)
                    self.b_can.create_text(60,60,text=self.w_sq.name_sq, fill='#232223', anchor='se')
                    self.b_can.pack()
                    self.b_frames.append(self.frm_b_sq)
                    self.b_canvas.append(self.b_can)
                    self.black_squares.append(self.b_sq.name_sq)
        self.board_drawing = True

gui = JakeChess()
gui.make_board()

bR = gs.Piece('black', 'rook', 'T')
bN = gs.Piece('black', 'knight', 'C')
bB = gs.Piece('black', 'bishop', 'A')
bQ = gs.Piece('black', 'queen', 'D')
bK = gs.Piece('black', 'king', 'R')
bP = gs.Piece('black', 'pawn', 'P')
wR = gs.Piece('white', 'rook', 'T')  
wN = gs.Piece('white', 'knight', 'C')
wB = gs.Piece('white', 'bishop', 'A')
wQ = gs.Piece('white', 'queen', 'D')
wK = gs.Piece('white', 'king', 'R')
wP = gs.Piece('white', 'pawn', 'P')
wG = gs.Piece('white', 'ghost', 'G')
bG = gs.Piece('black', 'ghost', 'G')

a8 = gui.w_canvas[0]
b8 = gui.b_canvas[0]
c8 = gui.w_canvas[1]
d8 = gui.b_canvas[1]
e8 = gui.w_canvas[2]
f8 = gui.b_canvas[2]
g8 = gui.w_canvas[3]
h8 = gui.b_canvas[3]

a7 = gui.b_canvas[4]
b7 = gui.w_canvas[4]
c7 = gui.b_canvas[5]
d7 = gui.w_canvas[5]
e7 = gui.b_canvas[6]
f7 = gui.w_canvas[6]
g7 = gui.b_canvas[7]
h7 = gui.w_canvas[7]

a6 = gui.w_canvas[8]
b6 = gui.b_canvas[8]
c6 = gui.w_canvas[9]
d6 = gui.b_canvas[9]
e6 = gui.w_canvas[10]
f6 = gui.b_canvas[10]
g6 = gui.w_canvas[11]
h6 = gui.b_canvas[11]

a5 = gui.b_canvas[12]
b5 = gui.w_canvas[12]
c5 = gui.b_canvas[13]
d5 = gui.w_canvas[13]
e5 = gui.b_canvas[14]
f5 = gui.w_canvas[14]
g5 = gui.b_canvas[15]
h5 = gui.w_canvas[15]

a4 = gui.w_canvas[16]
b4 = gui.b_canvas[16]
c4 = gui.w_canvas[17]
d4 = gui.b_canvas[17]
e4 = gui.w_canvas[18]
f4 = gui.b_canvas[18]
g4 = gui.w_canvas[19]
h4 = gui.b_canvas[19]

a3 = gui.b_canvas[20]
b3 = gui.w_canvas[20]
c3 = gui.b_canvas[21]
d3 = gui.w_canvas[21]
e3 = gui.b_canvas[22]
f3 = gui.w_canvas[22]
g3 = gui.b_canvas[23]
h3 = gui.b_canvas[23]

a2 = gui.w_canvas[24]
b2 = gui.b_canvas[24]
c2 = gui.w_canvas[25]
d2 = gui.b_canvas[25]
e2 = gui.w_canvas[26]
f2 = gui.b_canvas[26]
g2 = gui.w_canvas[27]
h2 = gui.b_canvas[27]

a1 = gui.b_canvas[28]
b1 = gui.w_canvas[28]
c1 = gui.b_canvas[29]
d1 = gui.w_canvas[29]
e1 = gui.b_canvas[30]
f1 = gui.w_canvas[30]
g1 = gui.b_canvas[31]
h1 = gui.w_canvas[31]

Pieces = [bR, bN, bB, bQ, bK, bP, wR, wN, wB, wQ, wK, wP, wG, bG]
print(gui.white_squares + gui.black_squares, Pieces)

def put(piece, square):
    square.create_image(32, 32, image=piece.image)
    #print(f'{piece.name} placed on {square}')


put(bR, a8)
put(bN, b8)
put(bB, c8)
put(bQ, d8)
put(bK, e8)
put(bB, f8)
put(bN, g8)
put(bR, h8)
put(bP, a7)
put(bP, b7)
put(bP, c7)
put(bP, d7)
put(bP, e7)
put(bP, f7)
put(bP, g7)
put(bP, h7)
put(wP, h2)
put(wP, g2)
put(wP, f2)
put(wP, e2)
put(wP, d2)
put(wP, c2)
put(wP, b2)
put(wP, a2)
put(wR, a1)
put(wN, b1)
put(wB, c1)
put(wQ, d1)
put(wK, e1)
put(wB, f1)
put(wN, g1)
put(wR, h1)
gui.main_loop()