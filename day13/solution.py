import time
import os
import numpy as np
from intcoder import Intcoder 
from plotter import Animater

class Breakout:
    
    def __init__(self, data):
        self.data = data
        self.arrays = []
        self.data[0] = 2
        self.computer = Intcoder(data, 0)
        self.tile_id = 0
        self.current_score = 0
        self.paddle_x = 0
        self.ball_x = 0
        self.grid_x = 45
        self.grid_y = 23
        arr = np.zeros((self.grid_y,self.grid_x))


    def part1(self, data):
        computer = Intcoder(data, 0)
        ret = 0 
        tile_id = 0
        arr = np.zeros((45,23))
        while tile_id != -1:
            x = computer.eval(None)
            y = computer.eval(None)
            tile_id = computer.eval(None)
            if tile_id == 2:
                ret += 1
            arr[x,y] = tile_id
        return ret

    def part2(self, data):
        arrays = []
        data[0] = 2
        computer = Intcoder(data, 0)
        tile_id = 0
        arr = np.zeros((23,45))
        current_score = 0
        paddle_x = 0
        ball_x = 0
        inn = None
        while tile_id != -1:
            x = computer.eval(inn)
            y = computer.eval(inn)
            tile_id = computer.eval(inn)
            
            self.parse_output(x, y, tile_id)

            if tile_id == 4:
                ball_x = x
            elif tile_id == 3:
                paddle_x = x 

            inn = 0 
            if paddle_x < ball_x: inn = 1
            elif paddle_x > ball_x: inn = -1

            if x == -1 and y == 0:
                current_score = tile_id
            else:
                if tile_id == -1:
                    return current_score, arrays
                arr[y,x] = tile_id
                arrays.append(arr.copy())
            print(current_score)

    def parse_output(self, x,y,tile_id):
        pass


if __name__ == "__main__":
    data = {i:int(x) for (i,x) in  enumerate(open("input.txt", "r").read().split(","))}
    b = Breakout(data)
    part2_res, arrays = b.part2(data)
    Animater(arrays)
