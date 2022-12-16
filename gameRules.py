class GameFlow:
    def __init__(self, new_game):
        self.new_game = new_game
        self.playing = False 
        self.current_turn = None
        self.w_time = 0
        self.b_time = 0
        self.w_moves = 0
        self.b_moves = 0
        self.game_over = True

    def timeOver(self):
        while self.playing:
            print(self.w_time)
            print(self.b_time)
            if self.w_time == 0:
                self.playing = False
                self.game_over = True
                print("Game Over")
                print("Black wins")
            elif self.b_time == 0:
                self.playing = False
                self.game_over = True
                print("Game Over")
                print("White wins")