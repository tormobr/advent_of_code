import numpy as np
from level import Level
from copy import deepcopy

def part2(data, levels=300):
    SEEN = [data]
    none_data = np.array([[0 for _ in range(5)] for _ in range(5)])
    datas = []
    L = []
    for i in range(levels):
        L.append(Level(data=none_data))
        datas.append(none_data)
    set_parents(L, levels)
    L[(levels//2)].set_data(data)

    datas[(levels//2)] = data
    

    for i in range(200):
        for i,level in enumerate(L):
            print(level.data)
            level.iteration()
            datas[i] = deepcopy(level.data)
        for i,level in enumerate(L):
            level.set_nexxt()

    for i,level in enumerate(L):
        print("level:", (levels//2)-i)
        draw(level.data)

    print("bugcount: ", get_bug_count(L))

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
    print("Part 1 answer:", part2(data))
