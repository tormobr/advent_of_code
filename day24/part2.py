from plotter import Animater
import time
import numpy as np
from level import Level
from copy import deepcopy

def part2(data, arrays, iterations=200, levels=300, main=None):
    SEEN = [data]
    none_data = np.array([[0 for _ in range(5)] for _ in range(5)])
    L = []
    for i in range(levels):
        L.append(Level(data=none_data, ID=i))
    set_parents(L, levels)
    L[(levels//2)].set_data(data)

    for i in range(iterations):
        arrays.append(deepcopy(main))
        for i,level in enumerate(L):
            print(level.data)
            level.iteration()
        for i,level in enumerate(L):
            level.set_nexxt()
            update_main(main, level, levels)

    print("bugcount: ", get_bug_count(L))

def update_main(main, level, levels):
    start_y = ((level.ID // 15) *5)
    end_y = start_y+5
    start_x = ((level.ID % 15) * 5)
    end_x = start_x+5
    i, j = 0,0
    for y in range(start_y, end_y):
        j = 0
        for x in range(start_x, end_x):
            print(main[y,x])
            print(x,y, j,i )
            main[y,x] = level.data[i,j]
            j += 1
        i += 1

def set_parents(L, levels):
    for i in range(len(L)):
        if i == 0:
            L[i].set_parent(child=L[i+1])
        elif i == levels-1:
            L[i].set_parent(parent=L[i-1])
        else:
            L[i].set_parent(parent=L[i-1], child=L[i+1])

def get_bug_count(L):
    count = 0
    for level in L:
        for line in level.data:
            for c in line:
                if c == 1:
                    count += 1
    return count

if __name__ == "__main__":
    data = np.array([[c for c in line.strip()] for line in open("input.txt")])

    data = np.where(data=="#", 1, 0)
    iterations = 200
    levels = 225
    main = np.zeros((75, 75))
    arrays = []
    print("Part 2 answer:", part2(data, arrays, iterations=iterations, levels=levels, main=main))
    Animater(arrays)
