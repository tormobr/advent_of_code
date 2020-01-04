from level import Level
from copy import deepcopy


def part1(data):
    SEEN = [data]
    L = Level(data=data)
    while True:
        L.iteration()
        data = deepcopy(L.data)
        if data in SEEN:
            return get_biodiv(data)
        SEEN.append(data)

def draw(data):
    res = ""
    for line in data:
        for c in line:
            res += c
        res += "\n"
    print(res)

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
