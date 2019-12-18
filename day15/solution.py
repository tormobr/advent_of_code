from copy import deepcopy
from plotter import Animater
from collections import defaultdict
import time 
import random
from intcoder import Intcoder
import os
import sys
from copy import deepcopy

class Maze_solver:
    def __init__(self, data):
        self.grid =  0
        self.directions = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
        self.backtracking = {1: 2, 2: 1, 3:4, 4:3}
        self.visited = set()
        self.computer = Intcoder(data, 0)
        self.max_x = 41  #fetched from part 1
        self.max_y = 41  #fetched from part 1
        self.base_x = (self.max_x//2)+1
        self.base_y = (self.max_y//2)+1
        self.grid = [[0]*self.max_x for i in range(self.max_y)]
        self.arrays = [deepcopy(self.grid)]

    def draw_frame(self, arr):
        #os.system("clear")
        ret = ""
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0: ret += " "
                elif arr[i][j] == 1: ret += "."
                elif arr[i][j] == 2: ret += "D"
                elif arr[i][j] == 3: ret += "#"
                elif arr[i][j] == 4: ret += "O"
                else: ret += "B"
            ret += "\n"
        print(ret)
        #time.sleep(0.1)

    def part1(self, data):
        results = []

        res = self.rec(self.base_x, self.base_y, 1, results)
        depth = self.get_depth(9, 3, 0)-1
        
        return results, depth


    def get_depth(self, x, y, depth):
        self.grid[y][x] = 10-(depth*0.01)
        self.arrays.append(deepcopy(self.grid))
        self.draw_frame(self.grid) 
        time.sleep(0.001)
        depths = [0,0,0,0]
        if self.grid[y][x] == 1:
            return 0
        for i in range(1,5):
            new_x = x+self.directions[i][0]
            new_y = y+self.directions[i][1]
            if self.grid[new_y][new_x] == 1:
                depths[i-1] = self.get_depth(new_x, new_y, depth+1)
        return max(depths) +1

    def rec(self, x, y, steps, results):
        self.draw_frame(self.grid)
        self.arrays.append(deepcopy(self.grid))
        time.sleep(.001)
        self.grid[y][x] = 2
        self.arrays.append(deepcopy(self.grid))
        self.visited.add((x,y))
        for i in range(1,5):
            new_x = x + self.directions[i][0]
            new_y = y + self.directions[i][1]
            if (new_x, new_y) in self.visited:
                continue
            out = self.computer.eval(i) 
            if out == 0:
                self.grid[new_y][new_x] = 3
                continue
            elif out == 1:
                self.grid[new_y][new_x] = 2
                self.grid[y][x] = 1
                self.rec(new_x, new_y, steps+1, results)
                self.computer.eval(self.backtracking[i])
                self.grid[y][x] = 2
            elif out == 2:
                self.grid[new_y][new_x] = 4
                self.computer.eval(self.backtracking[i])
                results.append(steps)
        self.grid[y][x] = 1

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    M = Maze_solver(data.copy())
    print(M.part1(data.copy()))
    Animater(M.arrays)
