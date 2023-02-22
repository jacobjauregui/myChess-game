import tkinter as tk
class Piece:
    pass
    def __init__(self, color, name,_id):
        self.color = color
        self.name = name
        self._id = _id
        self.image = tk.PhotoImage(file=f'./assets/{color}_{name}.png')
        self.r_value = 0
        self.max_range = 0
        self.on_board = False
        self.selected = False 
        self.moved = False
        self.attacked = False
        self.captured = True
        self.position = None


class Square:
    def __init__(self, row, column, color, piece):
        self.color = color
        self.row = row
        self.column = column
        self.piece = piece
        self.name_sq = f'{self.column}{self.row}'