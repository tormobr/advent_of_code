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

def part1(moons, velos):
    iterations = 1000
    for _ in range(iterations):
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
    return get_total_energy(moons, velos)

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


