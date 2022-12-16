import tkinter as tk
import time
import gameSet 
import gameRules

class ChessEngine:
    def __init__(self, square_size):
        self.square_size = square_size
        self.assets = {}
         
        self.gs = gameSet.PiecesSet()
        self.bd = gameSet.Board()
        
        self.window = tk.Tk()
        self.window.title("JakeChess")
        self.window.iconbitmap("chessicon.ico")
        self.window.geometry("550x550")
        self.window.resizable(True, True)
        
        self.interface = tk.Canvas(self.window, borderwidth=1, cursor="hand2")
        self.interface.pack(fill="both", expand=True)
        
        self.play = gameRules.GameFlow("y")

    def __call__(self):
        self.window.mainloop()

    def drawBoard(self):
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    self.interface.create_rectangle(
                        x*self.square_size, 
                        y*self.square_size, 
                        (x+1)*self.square_size, 
                        (y+1)*self.square_size, 
                        fill="#f0d9b5"
                    )
                else:                                                                               
                    self.interface.create_rectangle(
                        x*self.square_size, 
                        y*self.square_size, 
                        (x+1)*self.square_size, 
                        (y+1)*self.square_size, 
                        fill="#b58863"
                    )

    def loadAssets(self):
        pieces = ["bP", "bR", "bN", "bB", "bQ", "bK", "wP", "wR", "wN", "wB", "wQ", "wK"]
        for piece in pieces:
            self.assets[piece] = tk.PhotoImage(file="./assets/" + piece + ".png")

    def showPieces(self):
        for row, x in enumerate(self.gs.pieces):
            for col, y in enumerate(x):
                if y != "--":
                    self.interface.create_image(
                        (col+0.5)*self.square_size, 
                        (row+0.5)*self.square_size,
                        image=self.assets[y],
                        anchor="center"
                    )

    def squareName(self):
        for row, x in enumerate(self.bd.board):
            for col, y in enumerate(x):
                self.interface.create_text(
                    (col+0.88)*self.square_size,
                    (row+0.88)*self.square_size,
                    text=str(y),
                    anchor="center",
                )

    def showWClock(self):
        self.interface.create_rectangle(60, 60, 120, 120, fill="#ffffff")
        self.interface.create_text(90, 90, text=str(self.play.w_time), anchor="center")

    def showBClock(self):
        self.interface.create_rectangle(60, 60, 120, 120, fill="#616151")
        self.interface.create_text(90, 90, text=str(self.play.b_time), anchor="center")
        
    def letsPlay(self):
        if self.play.new_game == "y":
            self.play.playing = True
            self.play.current_turn = "white"
            self.play.w_time = 300
            self.play.b_time = 300
            self.play.game_over = False
            
    def alternTurn(self):
        while self.play.playing:
            if self.play.current_turn == "white":
                self.play.w_moves += 1
                self.play.current_turn = "black"
            elif self.play.current_turn == "black":
                self.play.b_moves += 1
                self.play.current_turn = "white"

    def timeControl(self):
        while self.play.playing:
            if self.play.current_turn == "white" and self.play.w_time > 0:
                    self.showWClock()
                    self.play.w_time -= 1
                    time.sleep(1)
            elif self.play.current_turn == "black" and self.play.b_time > 0:
                    self.showBClock()
                    self.play.b_time -= 1
                    time.sleep(1)

JakeChess = ChessEngine(68)
JakeChess.drawBoard()
JakeChess.loadAssets()
JakeChess.showPieces()
JakeChess.squareName()
JakeChess.letsPlay()
JakeChess.timeControl()

JakeChess()