import tkinter as tk
from abc import ABCMeta, abstractmethod
class Piece:
    @abstractmethod
    def __init__(self, color, name, _id):
        self._color = color
        self._name = name
        self._id = _id
        self._image = tk.PhotoImage(file=f'./assets/{name}_{color}.png')
        self._relative_value = 0
        self._max_range = 0
        self._on_board = False
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = True
        self._position = None
    
    def __repr__(self):
        return f"{self._name[0].capitalize()}{self._color[0]}"

    def set_name(self, name):
        self._name = name
        return self._name
    
    def get_name(self):
        return self._name.capitalize()
    
    def set_color(self, color):
        self._color = color
        return self._color
    
    def get_color(self):
        return self._color
    
    def set_id(self, _id):
        self._id = _id
        return self._id
    
    def get_id(self):
        return self._id
    
    def set_position(self, position):
        self._position = position
        return self._position

    def get_position(self):
        return self._position
    
    def set_image(self, image):
        self._image = image
        return self._image
    
    def get_image(self):
        return self._image
    
    def select(self):
        self._selected = True
        print('Selected')
        return self._selected

    def unselect(self):
        self._selected = False
        print('Is not selected')
        return self._selected
    
    
    
    def get_status(self):
        self.get_name()
        self.get_position()
        self.get_color()
        self.get_id()
        self.get_image()
        print(self, self._position)
        return self._on_board and self._selected and self._moved and self._captured
    

    def move(self, position):
        self.set_position(position)
        self._on_board = True
        self._selected = False
        self._moved = True
        self._captured = False
 
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, name='peon', _id='P')
        self._relative_value = 1
        self._max_range = 1
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, name='torre', _id='T')
        self._relative_value = 5
        self._max_range = 7
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None
    
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, name='caballo', _id='C')
        self._relative_value = 3
        self._max_range = 1
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None
        
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, name='alfil', _id='A')
        self._relative_value = 3
        self._max_range = 7
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, name='dama', _id='D')
        self._relative_value = 9
        self._max_range = 7
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None

class King(Piece):
    def __init__(self, color):
        super().__init__(color, name='rey', _id='R')
        self._relative_value = 0
        self._max_range = 1
        self._on_board = True
        self._selected = False 
        self._moved = False
        self._attacked = False
        self._captured = False
        self._position = None

class Square:
    def __init__(self, column, row, color):
        self._column = column
        self._row = row
        self._color = color
        self._name = f'{self._column}{self._row}'
        self._piece = None 

    def __repr__(self):
        return f"{self._name}"
    
    def get_column(self):
        return self._column
    
    def get_row(self):
        return self._row
    
    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color

    def set_piece(self, piece):
        self._piece = piece
        return self._piece
    
    def get_piece(self):
        return self._piece
    