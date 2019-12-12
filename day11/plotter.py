
from collections import defaultdict
import numpy as np
from intcoder import Intcoder
import matplotlib.animation as animation
from matplotlib import pyplot as plt

# Solves part one and part 2
def part_n(data, inn):
    computer = Intcoder(data, 0)
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    x, y, color, dir_index = 0, 0, 0, 0
    arr = np.full((6,43),-1)
    arrays = [arr]
    iterations = 0
    # While intcode program is not done paint new square and move
    while color != -1:
        new_arr = arrays[-1].copy()
        color = computer.eval(inn)
        new_arr[y][x] = color	
        arrays.append(new_arr)

        turn_dir = computer.eval(inn)
        dir_index += 1 if turn_dir else -1
        x += directions[dir_index%4][0]
        y += directions[dir_index%4][1]
        inn.append(new_arr[y][x])
        iterations += 1

    return arrays, iterations

def generate_data(arrays, i):
    return arrays[i]

def update(data):
    mat.set_data(data)
    return mat 

def data_gen(arrays, iterations):
    for i in range(iterations):
        yield generate_data(arrays, i)


if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    arrays, iterations = part_n(data.copy(), [1])

    fig, ax = plt.subplots()
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    mat = ax.matshow(generate_data(arrays, -1))
    ani = animation.FuncAnimation(fig, update, lambda: data_gen(arrays, iterations), interval=50, save_count=iterations)
    plt.show()
    ani.save("plot.mp4", )
