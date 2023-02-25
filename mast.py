import gameSet as gs
import interface as itf
import time as tm
import tkinter as tk
from tkinter import dnd

gui = itf.Screens()
gui.welcome()
cl = itf.Colors()


white_squares = {} 
black_squares = {}
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [1, 2, 3, 4, 5, 6, 7, 8]
rows.reverse()
for c, col in enumerate(columns):
    for r, row in enumerate(rows):
        if (c + r) % 2 == 0:
            white_squares[f'{col}{row}'] = gs.Square(col, row, 'black')
        else:
            black_squares[f'{col}{row}'] = gs.Square(col, row, 'white')

tb = gs.Rook('blanco')
cb = gs.Knight('blanco')
ab = gs.Bishop('blanco')
db = gs.Queen('blanco')
rb = gs.King('blanco')
pb = gs.Pawn('blanco')
tn = gs.Rook('negro')  
cn = gs.Knight('negro')
an = gs.Bishop('negro')
dn = gs.Queen('negro')
rn = gs.King('negro')
pn = gs.Pawn('negro')

pieces = {
    'Tb': tb,
    'Cb': cb,
    'Ab': ab,
    'Db': db,
    'Rb': rb,
    'Pb': pb,
    'Tn': tn,
    'Cn': cn,
    'An': an,
    'Dn': dn,
    'Rn': rn,
    'Pn': pn
}

squares = white_squares | black_squares

def play():
    gui.make_board()
    put_on_board('Tn', 'a8')
    put_on_board('Cn', 'b8')
    put_on_board('An', 'c8')
    put_on_board('Dn', 'd8')
    put_on_board('Rn', 'e8')
    put_on_board('An', 'f8')
    put_on_board('Cn', 'g8')
    put_on_board('Tn', 'h8')
    put_on_board('Pn', 'a7')
    put_on_board('Pn', 'b7')
    put_on_board('Pn', 'c7')
    put_on_board('Pn', 'd7')
    put_on_board('Pn', 'e7')
    put_on_board('Pn', 'f7')
    put_on_board('Pn', 'g7')
    put_on_board('Pn', 'h7')
    put_on_board('Pb', 'a2')
    put_on_board('Pb', 'b2')
    put_on_board('Pb', 'c2')
    put_on_board('Pb', 'd2')
    put_on_board('Pb', 'e4')
    put_on_board('Pb', 'f2')
    put_on_board('Pb', 'g2')
    put_on_board('Pb', 'h2')
    put_on_board('Tb', 'a1')
    put_on_board('Cb', 'b1')
    put_on_board('Ab', 'c1')
    put_on_board('Db', 'd1')
    put_on_board('Rb', 'e1')
    put_on_board('Ab', 'f1')
    put_on_board('Cb', 'g1')
    put_on_board('Tb', 'h1')


def put_on_board(pz, sq):
    cv = gui.board_canvas
    cv[sq].create_image(32, 32, image=pieces[pz]._image)
    p = squares[sq].set_piece(pieces[pz])
    s = pieces[pz].set_position(squares[sq])
    c = cv[sq]
    binds(p, s, c)
    return p and s and c


def binds(p, s, c):
    original_color = c.cget('bg')
    if p._selected == False:
        c.bind('<Button-1>', lambda event: select_piece(p, s, c, original_color))
        c.bind('<Enter>', lambda event: hover(p, s, c))
        c.bind('<Leave>', lambda event: unhover(p, s, c, original_color))
    else:
        c.bind('<Button-1>', lambda event: unselect_piece(p, s, c, original_color))
        c.unbind('<Enter>', lambda event: hover(p, s, c))
        c.unbind('<Leave>', lambda event: unhover(p, s, c, original_color))
    
def hover(p, s, c):
    p.set_position(s)
    s.set_piece(p)
    p.get_status()
    c.configure(cursor='hand2', bg=cl.yellow)

def unhover(p, s, c, original_color):
    c.configure(cursor='hand2', bg=original_color)


def select_piece(p, s, c, original_color):
    original_color = c.cget('bg')
    p.get_status()
    if not p._selected == True:
        original_color = c.cget('bg')
        c.bind('<Enter>', lambda event: hover(p,  c, original_color))
        c.bind('<Button-1>', lambda event: unselect_piece(p, s, c, original_color))
        p.select()
        c.configure(bg=cl.green)
        c.bind('<Leave>' , lambda event: unhover(p, s, c, cl.green))
    elif p._selected == True:
        c.configure(bg=original_color)
        
        c.bind('<Leave>', lambda event: unhover(p, s, c, original_color))
        c.bind('<Button-1>', lambda event: unselect_piece(p, s, c, original_color))
        #c.bind('<Enter>', lambda event: o_hover(p, s, c))
        #c.bind('<Leave>', lambda event: unhover(p, s, c, original_color))
        #c.bind('<Button-1>', lambda event: unselect_piece(p, s, c, original_color))
def unselect_piece(p, s, c, original_color):
    if p._selected == True:
        p.unselect()
        c.configure(bg = original_color)
        c.bind('<Button-1>', lambda event: select_piece(p, s, c, original_color))
    #if not p._selected == True:


'''
events = {
    'l_click': '<Button-1>',
    'r_click': '<Button-3>',
    'm_click': '<Button-2>',
    'hover': '<Enter>',
    'unhover': '<Leave>',
}

def bind(event, callback):
    widget.bind(event, callback)

def select_scuare(event):
    gui.board_canvas.keys()
    print(event.widget)
    print(event.widget.keys())


gui.root.bind('<Button-1>', callback)
  
def left(piece, x,y):
    x = -64
    y = 0
    piece.move(x, y)
def right(x, y):
    x = 64
    y = 0
def up(x, y):
    x = 0
    y = 64
def down(x, y):
    x = 0
    y = -64
    a8.move(x, y)

a1.bind('<left>', left(a1, 1,1))
a8.bind('<right>', right(1,1))
c6.bind('<up>', up(1,1))
c8.root.bind('<down>', down(1,1))
'''


# btn_board = tk.Button(
#     gui.menu_bar,
#     text = 'Board',
#     font = ('Times', 10, 'bold'),
#     bd = 5,
#     bg = cl.carbon,
#     fg = cl.white,
#     relief = 'flat',
#     cursor = 'hand2',
#     command = gui.make_board
# )

# btn_showCan = tk.Button(
#     gui.menu_bar,
#     text = 'Show Canvas',
#     font = ('Times', 10, 'bold'),
#     bd = 5,
#     bg = cl.carbon,
#     fg = cl.white,
#     relief = 'flat',
#     cursor = 'hand2',
#     command = show_canvas
# )

btn_exit = tk.Button(
    gui.menu_bar,
    text='Exit',
    font=('Times', 10, 'bold'),
    bd = 5,
    bg = cl.blood,
    fg=cl.white,
    relief='flat',
    cursor='hand2',
    command=gui.root.destroy
)
btn_close = tk.Button(
    gui.menu_bar,
    text='Close',
    font=('Times', 10, 'bold'),
    bd = 5,
    bg=cl.blood,
    fg=cl.white,
    relief='flat',
    cursor='hand2',
    command=gui.frm_board.pack_forget
)
btn_play = tk.Button(
    gui.menu_bar,
    text='Play',
    font=('Times', 10, 'bold'),
    bd = 5,
    bg=cl.silver,
    fg=cl.dark,
    relief='flat',
    cursor='hand2',
    command=play
)
btn_exit.grid(column=0, row=0, padx=5, pady=2)
# btn_board.grid(column=1, row=0, padx=5, pady=2)
btn_close.grid(column=2, row=0, padx=5, pady=2)
btn_play.grid(column=3, row=0, padx=5, pady=2)
#btn_showCan.grid(column=4, row=0, padx=5, pady=2)

gui.main_loop()