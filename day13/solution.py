import time
import os
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

    def play(self, data):
        self.data[0] = 2    # play for free mode
        inn = None
        while True:
            x = self.computer.eval(inn)
            y = self.computer.eval(inn)
            self.tile_id = self.computer.eval(inn)
            inn = self.parse_output(x, y)

            if x == -1 and y == 0:
                self.current_score = self.tile_id
                continue
            elif self.tile_id == -1:
                return self.current_score

            self.arr[y,x] = self.tile_id
            self.arrays.append(self.arr.copy())

    def parse_output(self, x,y):
        # moving paddle and ball
        if self.tile_id == 4: 
            self.ball_x = x
        elif self.tile_id == 3: 
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
    score = b.play(data)
    print(f"Part 2 answer: {score}")
    Animater(b.arrays)
