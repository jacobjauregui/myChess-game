import tkinter as tk
import gameSet as sets
class Interface:
    def __init__(self, size):
        self.size = size 
        self.bd = sets.board
        self.assets = {}
        self.window = tk.Tk()
        self.window.title("JakeChess")
        self.window.iconbitmap("./assets/chessicon.ico")
        self.window.geometry(f"{(self.size+1)*8}x{(self.size+1)*8}")
        self.window.resizable(True, True)
        self.interface = tk.Canvas(self.window, borderwidth=0, cursor="hand2")
        self.interface.pack(fill="both", expand=True)
        
    def __call__(self):
        self.window.mainloop()
    
    def drawBoard(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.interface.create_rectangle(i*self.size, j*self.size, (i+1)*self.size, (j+1)*self.size, fill="#f0d9b5")
                else:
                    self.interface.create_rectangle(i*self.size, j*self.size, (i+1)*self.size, (j+1)*self.size, fill="#b58863")

    def squareName(self):
        for i in range(8):
            for j in range(8):
                self.interface.create_text(
                    (i+0.88)*self.size,
                    (j+0.88)*self.size,
                    text=(f"{self.bd[j][i][0]}{self.bd[j][i][1]}"),
                    anchor="center",
                )

    def loadAssets(self):
        pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
        for piece in pieces:
            self.assets[piece] = tk.PhotoImage(file ="./assets/" + piece + ".png")

    def showPieces(self):
        for x in range(8):
            for y in range(8):
                if self.bd[y][x][2] != "--":
                    self.interface.create_image(
                        (x+0.5)*self.size, 
                        (y+0.5)*self.size,
                        image=self.assets[self.bd[y][x][2]],
                        anchor="center"
                    )
                    
JakeChess = Interface(70)

JakeChess.drawBoard()
JakeChess.squareName()
JakeChess.loadAssets()
JakeChess.showPieces()

JakeChess()