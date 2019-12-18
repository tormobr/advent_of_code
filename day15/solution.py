from collections import defaultdict
import time 
import random
from intcoder import Intcoder
import os
import sys
from copy import deepcopy
sys.setrecursionlimit(10**6) 
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
    directions = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
    out = 0
    found = False
    x, y = 0, 0
    max_x = 50
    max_y = 50
    base_x = (max_x//2) +1
    base_y = 25
    arr = [[0]*max_x for i in range(max_y)]
    arr[base_y+y][base_x+x] = 2
    count = 0
    visited = defaultdict(int)
    haxors = [2,1,3,4]
    results = []
    """
    while out != -1:
        hax = random.randrange(1,5)
        n = 0
        print("is this loopping")
        while (x+directions[hax][0], y+directions[hax][1]) in visited.keys() and n <= 5:
            print("foreever?")
            hax = random.randrange(1,5)
            n += 1
        #hax = int(input())
        #time.sleep(4)
        if True:
            visited[(x+directions[hax][0],y+directions[hax][1])] += 1 
            dirr = hax
            print(dirr)
            inn = dirr
            out = computer.eval(inn)
            if out == 0:
                #print("hit wall")
                t_x = base_x+x+directions[dirr][0]
                t_y = base_y+y+directions[dirr][1]
                arr[t_y][t_x] = 3
            elif out == 1:
                #print("allews gut ")
                count += 1
                arr[base_y+y][base_x+x] = 1
                print("visited: ", x,y)
                x += directions[dirr][0]
                y += directions[dirr][1]
                arr[base_y+y][base_x+x] = 2
            elif out == 2:
                print("doons")
                found = True
            print("out", out)
        os.system("clear")
        draw_frame(arr)
        """
    rec(computer, arr,  base_x, base_y, 1, results, 0)

    return results

directions = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
backtracking = {1: 2, 2: 1, 3:4, 4:3}
visited = set()
def rec(computer,arr, x, y, steps, results, inputt):
    steppers = []
    print(steps)
    time.sleep(.01)
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
            arr[new_y][new_x] = 4
            results.append(steps)
            print("doons", results)
            computer.eval(backtracking[i])
            #time.sleep(2)
            draw_frame(arr)
            return
    #print("bacxktrascking")
    arr[y][x] = 1
    return 100

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(part1(data.copy()))
    #print(part2(data))
