from collections import defaultdict
import time 
import random
from intcoder import Intcoder
import os
import sys
from copy import deepcopy

def draw_frame(arr):
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

def part1(data):
    computer = Intcoder(data, 0)
    max_x = 42
    max_y = 42
    base_x = (max_x//2)
    base_y = (max_y//2)
    arr = [[0]*max_x for i in range(max_y)]
    #arr[base_y+y][base_x+x] = 2
    count = 0
    visited = defaultdict(int)
    haxors = [2,1,3,4]
    results = []
    res = rec(computer, arr,  base_x, base_y, 1, results, 0)
    #print(res)
    print(arr)
    print(get_depth(arr, 9, 3, 0))
    
    #return max(results)

directions = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
backtracking = {1: 2, 2: 1, 3:4, 4:3}

visited2 = set()
def get_depth(arr, x, y, depth):
    print("current_val:", arr[y][x])
    arr[y][x] = 2
    draw_frame(arr) 
    time.sleep(0.1)
    visited.add((x,y))
    print(depth, x,y)
    depths = [0,0,0,0]
    if arr[y][x] == 1:
        return 0
    for i in range(1,5):
        print("direction i: ", i)
        new_x = x+directions[i][0]
        new_y = y+directions[i][1]
        print("potential next val: ", arr[new_y][new_x])
        if arr[new_y][new_x] == 1:
            print("recusing")
            depths[i-1] = get_depth(arr, new_x, new_y, depth+1)
    print("depths: ",depths)
    return max(depths) +1

visited = set()
def rec(computer,arr, x, y, steps, results, inputt):
    steppers = []
    print(steps)
    time.sleep(.001)
    arr[y][x] = 2
    visited.add((x,y))
    for i in range(1,5):
        #print(x,y, steps, i)
        new_x = x + directions[i][0]
        new_y = y + directions[i][1]
        if (new_x, new_y) in visited:
            continue
        #print("moving", i)

        #print("current x,y: ", x,y)
        out = computer.eval(i) 
        #print("out", out)
        if out == 0:
            arr[new_y][new_x] = 3
            draw_frame(arr)
            continue
        elif out == 1:
            draw_frame(arr)
            arr[new_y][new_x] = 2
            arr[y][x] = 1
            #print("recursion")
            steppers.append(rec(computer,arr, new_x, new_y, steps+1, results, 0))
            computer.eval(backtracking[i])
            arr[y][x] = 2
            #print("backtrach")
        elif out == 2:
            print(new_x, new_y)
            arr[new_y][new_x] = 4
            print("doons", results)
            computer.eval(backtracking[i])
            draw_frame(arr)
    
    results.append(steps)
    #print("bacxktrascking")
    arr[y][x] = 1

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(part1(data.copy()))
    #print(part2(data))
