import time
from copy import deepcopy
import os
import numpy as np
from intcoder import Intcoder 
from matplotlib import pyplot as plt
from matplotlib import animation

def part1(data):
    computer = Intcoder(data, 0)
    ret = 0 
    tile_id = 0
    arr = np.zeros((45,23))
    while tile_id != -1:
        x = computer.eval([None])
        y = computer.eval([None])
        tile_id = computer.eval([None])
        if tile_id == 2:
            ret += 1
        arr[x,y] = tile_id
    return ret
def draw_frame(arr):
    ret = ""
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0: ret += "  "
            elif arr[i][j] == 1: ret += "X "
            elif arr[i][j] == 2: ret += "B "
            elif arr[i][j] == 3: ret += "_ "
            elif arr[i][j] == 4: ret += "O "
        ret += "\n"
    print(ret)
    

def part2(data):
    arrays = []
    data[0] = 2
    computer = Intcoder(data, 0)
    ret = 0 
    tile_id = 0
    arr = np.zeros((23,45))
    current_score = 0
    paddle_x = 0
    ball_x = 0
    inn = [0]
    counter = 0
    scores = []
    while tile_id != -1:
        #if counter > 45*22:
            #os.system("clear")
            #draw_frame(arr)
            #time.sleep(0.0001 / (current_score+1))
        counter += 1
        x = computer.eval(inn[1:])
        y = computer.eval(inn[1:])
        tile_id = computer.eval(inn[1:])
        if tile_id == 4:
            ball_x = x
        elif tile_id == 3:
            paddle_x = x 

        
        if paddle_x < ball_x and tile_id == 4:
            inn.append(1)
        elif paddle_x > ball_x and tile_id == 4:
            inn.append(-1)
        elif paddle_x == ball_x and tile_id == 4:
            inn.append(0)
        if x == -1 and y == 0:
            current_score = tile_id
            scores.append(current_score)
        else:
            arr[y,x] = tile_id
            arrays.append(arr.copy())
        print(current_score)
    return max(scores), arrays

def generate_data(arrays, i):
    return arrays[i]

def update(data):
    mat.set_data(data)
    return mat 

def data_gen(arrays, iterations):
    for i in range(iterations):
        yield generate_data(arrays, i)
if __name__ == "__main__":
    data = {i:int(x) for (i,x) in  enumerate(open("input.txt", "r").read().split(","))}
    part2_res, arrays = part2(data)
    fig, ax = plt.subplots()
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    mat = ax.matshow(generate_data(arrays, len(arrays)-1))
    ani = animation.FuncAnimation(fig, update, lambda: data_gen(arrays, len(arrays)), interval=1, save_count=len(arrays))
    plt.show()
    ani.save("plot.mp4", )
