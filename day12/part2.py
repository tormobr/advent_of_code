import math
import numpy as np
from collections import defaultdict


def read_lines(lines):
    moons = []
    velos = []
    for line in lines:
        splitted = line.split(",")
        x = int(splitted[0].strip()[3:])
        y = int(splitted[1].strip()[2:])
        z = int(splitted[2].strip()[2:-1])
        moons.append([x,y,z])
        velos.append([0,0,0])
        print(x,y,z)
    return moons, velos 

def compare_og(axis, moons, og_moons):
    for i in range(len(moons)):
        if moons[i][axis] != og_moons[i][axis]:
            return False
    return True

def part1(moons, velos):
    og_moons = [[x for x in row] for row in moons]
    og_velos = [[x for x in row] for row in velos]
    dones = [0,0,0]
    print(moons, og_moons)
    iterations = 3000
    ret = 1
    while 0 in dones:
        for index, m in enumerate(moons):
            for m2 in moons:
                for i in range(3):
                    if m[i] < m2[i]:
                        velos[index][i] += 1
                    elif m[i] > m2[i]:
                        velos[index][i] -= 1
        for i, m in enumerate(moons):
            for j in range(3):
                m[j] += velos[i][j]
        for axis in range(3):
            if dones[axis] != 0: continue
            if compare_og(axis, moons, og_moons) and sum([velos[k][axis] for k in range(3)]) == 0:
                print(dones)
                dones[axis] = ret

        if ret % 100000 == 0:
            print("GOLYY")
        ret += 1 
    print("Res: ",dones)
    print(math.lcm(dones))
    return "this is part one"

def get_total_energy(moons, velos):
    res = 0
    for i, m in enumerate(moons):
        pot = sum([abs(x) for x in m])
        kin = sum([abs(x) for x in velos[i]])
        res += pot * kin
    return res

if __name__ == "__main__":
    lines = [line.strip() for line in open("input.txt", "r")]
    data = read_lines(lines)
    print(f"Part 1 answer: {part1(*data)}")


