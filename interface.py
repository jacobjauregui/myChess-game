import tkinter as tk
from tkinter import dnd

class Colors:
    def __init__(self):
        # ----- Background Dark Theme -----
        self.bg_drk = '#232323'
        self.dark = '#121212'
        self.dark1 = '#212121'
        self.dark2 = '#262626'
        self.dark3 = '#2C2C2C'
        # ----- Highlight Theme -----
        self.bg_hgl = '#D1D2D1'
        self.high1 = '#A8A9AD'
        self.high2 = '#B4B5B8'
        self.high3 = '#CBCCCD'
        self.high4 = '#D7D7D8'
        self.high5 = '#E3E3E3'
        # ----- RGB Colors -----
        self.black = '#000000'
        self.red = '#FF0000'
        self.green = '#00FF00'
        self.blue = '#0000FF'
        self.white = '#FFFFFF'
        # ----- Compose Colors -----
        self.yellow = '#FFFF00'
        self.violet = '#FF00FF'
        self.cian = '#00FFFF'
        self.orange = '#FFA500'
        self.purple = '#800080'
        self.brown = '#A52A2A'
        self.gray = '#808080'
        # ----- Personal Colors -----
        self.blue_drk = '#101020'
        self.gray_hgl = '#D3D3D3'
        self.blood = '#B22222'
        self.carbon = '#404040'
        self.silver = '#C2C1C3'
        self.gold = '#C2A255'
        # ----- Board Themes -----
        self.wood_white = '#F0D9B5'
        self.wood_black = '#B58863'
        self.wood_border = '#57241E'

        self.wood2_white = '#DBBA8F'
        self.wood2_black = '#B87B45'
        self.wood2_border = '#6B4728'
        
        self.metalic_white = '#A9A9A9'
        self.metalic_black = '#696969'
        self.metalic_border = '#C0C0C0'
        
        self.blue_white = '#95D7FF'
        self.blue_black = '#5386B5'
        self.blue_border = '#161632'
        
        self.green_white = '#FFFFDD'
        self.green_black = '#86A666'
        self.green_border = '#485936'


class Screens:
    def __init__(self):
        self.root = tk.Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (self.w, self.h))
        self.root.resizable(True, True)
        self.logo = tk.PhotoImage(file='./assets/logo_64.png')
        self.board_canvas = {}
        # --- Welcome Frame ---
        self.frm_welcome = tk.Frame(
            self.root,
            background=Colors().bg_hgl,
            borderwidth=4,
            width=300,
            height=100,
        )
        # --- Board Frame ---
        self.frm_board = tk.Frame(
            self.root,
            background=Colors().wood_border,
            borderwidth=15,
            width=512,
            height=512,
            cursor="arrow",
            relief="raised"
        )
        # --- TopBar Frame ---
        self.top_bar = tk.Frame(self.root, bg=Colors().silver)
        self.top_bar.pack(side='top', fill='x')
        # --- MenuBar Frame ---
        self.menu_bar = tk.Frame(self.top_bar, bg=Colors().black)
        self.menu_bar.pack(side = 'top', fill='x')
        self.frm_status = tk.Frame(
            self.root,
            background=Colors().blue_drk,
            borderwidth=4,
            width=300,
            height=self.h,
        )
        self.frm_status.pack(side='right', fill='y', expand=False)
        self.status = tk.StringVar()
        self.lbl_status = tk.Label(
            self.frm_status,
            textvariable = self.status,
            fg = Colors().white,
            bg = Colors().blue_drk,
            font = ('Arial', 14),
        )
        self.lbl_status.pack(side='top', fill='x', expand=False)
        self.board_on_screen = False
        self.btn_close_welcome = tk.Button(
            self.frm_welcome,
            text='X',
            font=('Arial', 8, 'bold'),
            bd = 2,
            bg=Colors().blood,
            fg=Colors().white,
            relief='flat',
            cursor='hand2',
            height=1,
            width=1,
            command=self.frm_welcome.destroy
        )


    def main_loop(self):
        self.root.title("JakeChess")
        self.root.iconbitmap("./assets/chessicon.ico")
        self.root.configure(background=Colors().carbon)
        self.root.mainloop()
    
    def welcome(self):
        self.frm_welcome.pack(side='top', expand=False)
        self.btn_close_welcome.pack(side='top', fill='none', expand=False, anchor='ne')
        self.lbl_welcome = tk.Label(
            self.frm_welcome,
            text = "Welcome to: ",
            font = ("Times", 14),
            background = Colors().bg_hgl,
            foreground = Colors().black
        )
        self.lbl_welcome.pack(side = 'top', expand = False, anchor='w')
        self.can_welcome = tk.Canvas(
            self.frm_welcome,
            background = Colors().bg_hgl,
            height=128,
            highlightthickness=0,

        )
        self.can_welcome.create_image(
            50,
            45,
            image = self.logo
        )
        self.can_welcome.create_text(
            184,
            54,
            text = "JakeChess",
            font = ("Castellar", 24),
            fill = Colors().gold
        )
        self.can_welcome.pack(side = 'left', expand = False, anchor='e')
        
    def make_board(self):
        self.frm_board.pack(side='top', expand=False)
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8]
        self.rows.reverse()
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.w_frames = {}
        self.w_canvas = {}
        self.b_frames = {}
        self.b_canvas = {}
        for x, col in enumerate(self.columns):
            for y, row in enumerate(self.rows):
                if (x + y) % 2 == 0:
                    # ----- White Frames -----
                    self.frm_w_sq = tk.Frame(
                        self.frm_board,
                        background = Colors().wood_white,
                        width = 64,
                        height = 64,
                        highlightthickness = 0
                    )
                    self.frm_w_sq.grid(column = x, row = y)
                    # ----- White Canvas -----                    
                    self.w_can = tk.Canvas(
                        self.frm_w_sq,
                        background = Colors().wood_white,
                        width = 64,
                        height = 64,
                        highlightthickness = 0
                    )
                    # ----- Coordenates -----
                    self.w_can.create_text(
                        60,
                        60,
                        text = f'{col}{row}',
                        fill = '#232223',
                        anchor = 'se'
                    )
                    self.w_can.pack()
                    
                    self.w_frames[f'{col}{row}'] = self.frm_w_sq
                    self.w_canvas[f'{col}{row}'] = self.w_can
                else:
                    # ----- Black Frames -----
                    self.frm_b_sq = tk.Frame(
                        self.frm_board,
                        background = Colors().wood_black,
                        width = 64,
                        height = 64,
                        highlightthickness = 0
                    )
                    self.frm_b_sq.grid(column=x, row=y)
                    # ----- Black Canvas -----
                    self.b_can = tk.Canvas(
                        self.frm_b_sq,
                        background = Colors().wood_black,
                        width = 64,
                        height = 64,
                        highlightthickness = 0
                    )
                    self.b_can.create_text(
                        60,
                        60,
                        text = f'{col}{row}',
                        fill = '#232223',
                        anchor = 'se'
                    )
                    self.b_can.pack()
                    
                    self.b_frames[f'{col}{row}'] = self.frm_b_sq
                    self.b_canvas[f'{col}{row}'] = self.b_can
        self.board_on_screen = True
        self.board_canvas = self.w_canvas | self.b_canvas
        self.board_frames = self.w_frames | self.b_frames
        return self.board_canvas, self.board_frames
