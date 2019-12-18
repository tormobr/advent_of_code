from collections import defaultdict
import time 
import random
from intcoder import Intcoder
import os
import sys
from copy import deepcopy

class Maze_solver:
    def __init__(self, data):
        self.arr =  0
        self.directions = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
        self.backtracking = {1: 2, 2: 1, 3:4, 4:3}
        self.visited = set()
        self.computer = Intcoder(data, 0)
        self.max_x = 42  #fetched from part 1
        self.max_y = 42  #fetched from part 1
        self.base_x = (self.max_x//2)
        self.base_y = (self.max_y//2)
        self.arr = [[0]*self.max_x for i in range(self.max_y)]

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
            ret += "\n"
        print(ret)
        #time.sleep(0.1)

    def part1(self, data):
        results = []

        res = self.rec(self.base_x, self.base_y, 1, results)
        depth = self.get_depth(9, 3, -1)
        
        return results, depth


    def get_depth(self, x, y, depth):
        self.arr[y][x] = 2
        self.draw_frame(self.arr) 
        time.sleep(0.001)
        depths = [0,0,0,0]
        if self.arr[y][x] == 1:
            return 0
        for i in range(1,5):
            new_x = x+self.directions[i][0]
            new_y = y+self.directions[i][1]
            if self.arr[new_y][new_x] == 1:
                depths[i-1] = self.get_depth(new_x, new_y, depth+1)
        return max(depths) +1

    def rec(self, x, y, steps, results):
        steppers = []
        print(steps)
        time.sleep(.001)
        self.arr[y][x] = 2
        self.visited.add((x,y))
        for i in range(1,5):
            new_x = x + self.directions[i][0]
            new_y = y + self.directions[i][1]
            if (new_x, new_y) in self.visited:
                continue
            out = self.computer.eval(i) 
            if out == 0:
                self.arr[new_y][new_x] = 3
                self.draw_frame(self.arr)
                continue
            elif out == 1:
                self.draw_frame(self.arr)
                self.arr[new_y][new_x] = 2
                self.arr[y][x] = 1
                steppers.append(self.rec(new_x, new_y, steps+1, results))
                self.computer.eval(self.backtracking[i])
                self.arr[y][x] = 2
            elif out == 2:
                print(new_x, new_y)
                self.arr[new_y][new_x] = 4
                print("doons", results)
                self.computer.eval(self.backtracking[i])
                self.draw_frame(self.arr)
        
                results.append(steps)
        self.arr[y][x] = 1

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    M = Maze_solver(data.copy())
    print(M.part1(data.copy()))
