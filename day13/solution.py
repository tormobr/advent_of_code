import numpy as np
from intcoder import Intcoder 
from plotter import Animater

class Breakout:
    def __init__(self, data):
        self.data = data
        self.computer = Intcoder(data, 0)
        self.arrays = []    # used for animation
        self.data[0] = 2
        self.current_score, self.paddle_x, self.ball_x = 0, 0, 0
        self.grid_x = 45    # hardcoded from part1
        self.grid_y = 23    # hardcoded from part1
        self.arr = np.zeros((self.grid_y,self.grid_x))
    
    # AI plays a good game of breakout
    def play(self):
        self.data[0] = 2    # play for free mode
        inn = None
        while True:
            x = self.computer.eval(inn)
            y = self.computer.eval(inn)
            tile_id = self.computer.eval(inn)
            inn = self.parse_output(x, y, tile_id)

            if x == -1 and y == 0:
                self.current_score = tile_id
                continue
            elif tile_id == -1:
                return self.current_score

            self.arr[y,x] = tile_id
            self.arrays.append(self.arr.copy())
    
    # Parses the output from intcode computer and acts accordingly
    def parse_output(self, x, y, tile_id):
        # moving paddle and ball
        if tile_id == 4: 
            self.ball_x = x
        elif tile_id == 3: 
            self.paddle_x = x 
        
        # getting the next input for intcoder
        if self.paddle_x < self.ball_x: 
            return 1
        elif self.paddle_x > self.ball_x: 
            return -1
        else: 
            return 0


if __name__ == "__main__":
    data = {i:int(x) for (i,x) in  enumerate(open("input.txt", "r").read().split(","))}
    b = Breakout(data)
    score = b.play()
    print(f"Part 2 answer: {score}")
    Animater(b.arrays)
