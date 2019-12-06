
# solution for part 1
def part1(data):
    orbits = {}
    for line in data:
        A,B = line.split(")")
        if A not in orbits.keys():
            orbits[A] = [B]
        else: orbits[A].append(B)
    parents = get_parent(orbits)

    res = 0
    ind = {}
    for key in parents.keys():
        print(key)
        p = parents[key]
        ind[key] = [p]
        while True:
            if p == "COM": 
                break 
            p = parents[p]
            ind[key].append(p)
            res += 1
        res+=1
    print(res)  
    
    rec(parents, "YOU", [])

def rec(orbits, current, paths, n):
    if parents[current] = "SAN": paths.append(n)
    for 
    print(start)

def get_parent(orbits):
    new = {}
    for key, value in orbits.items():
        for v in value:
            new[v] = (key)
    return new


# solution for part 2
def part2(data):
    pass


if __name__ == "__main__":
    data = [line[:-1] for line in open("input.txt", "r")]
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
