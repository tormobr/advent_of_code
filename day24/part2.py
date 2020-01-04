from level import Level
from copy import deepcopy

def part2(data, levels=500):
    SEEN = [data]
    none_data = [["." for _ in range(5)] for _ in range(5)]
    none_data[2][2] = "?"
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
            print("level:", i)
            draw(level.data)
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

def draw(data):
    res = ""
    for line in data:
        for c in line:
            res += c
        res += "\n"
    print(res)

def get_bug_count(L):
    count = 0
    for level in L:
        #print("drawing level")
        #draw(level.data)
        for line in level.data:
            for c in line:
                if c == "#":
                    count += 1
    return count

def get_biodiv(data):
    index = 0
    res = 0
    for line in data:
        for c in line:
            if c == "#":
                res += 2 ** index
            index += 1
    return res

if __name__ == "__main__":
    data = [[c for c in line.strip()] for line in open("input.txt")]

    print("Part 1 answer:", part2(data))
