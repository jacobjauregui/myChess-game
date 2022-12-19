import tkinter as tk
import gameSet as gs 
class JakeChess:
    def __init__(self, size):
        self.size = size 
        self.assets = {}
        self.window = tk.Tk()
        self.window.title("JakeChess")
        self.window.iconbitmap("./assets/chessicon.ico")
        self.window.geometry("800x640")
        self.window.resizable(True, True)
        self.interface = tk.Canvas(self.window, borderwidth=0, cursor="hand2")
        self.interface.pack(fill="both", expand=True)
        self.board_drawing = False
        self.row = gs.make_rows()
        self.initial_pos = gs.start_position()

    def __call__(self):
        self.window.mainloop()

    # BOARD
    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.interface.create_rectangle(
                        i*self.size,
                        j*self.size,
                        (i+1)*self.size,
                        (j+1)*self.size,
                        fill="#f0d9b5"
                    )
                else:
                    self.interface.create_rectangle(
                        i*self.size,
                        j*self.size,
                        (i+1)*self.size,
                        (j+1)*self.size,
                        fill="#b58863"
                    )
        for i in range(8):
            for j in range(8):
                self.interface.create_text(
                    (i+0.88)*self.size,
                    (j+0.88)*self.size,
                    text=(f"{self.row[j][i][0]}"),
                    anchor="center",
                )
        self.board_drawing = True
        self.btn_startGame()
# GAME    
    def new_game(self):
        pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
        for piece in pieces:
            self.assets[piece] = tk.PhotoImage(file="./assets/" + piece + ".png")
        if self.board_drawing == True:
            gs.start_position()
            for i in range(8):
                for j in range(8):
                    if self.initial_pos[j][i][1] != "--":
                        self.interface.create_image(
                        (i+0.5)*self.size, 
                        (j+0.5)*self.size,
                        image=self.assets[self.initial_pos[j][i][1]],
                        anchor="center"
                    )
        else:
            pass

    def btn_drawBoard(self):
        tk.Button(
            self.window,
            text="Draw Board",
            command=self.draw_board 
        ).pack()

    def btn_startGame(self):
        tk.Button(
            self.window,
            text="New Game",
            command=self.new_game
        ).pack()

Menu = JakeChess(70)
Menu.btn_drawBoard()

Menu()