

def part1(filename):
    a = [int(x) for x in open(filename).read().split(",")]
    for i in range(0, len(a), 4):
        opcode = a[i]
        b = a[i+1]
        c = a[i+2]
        loc = a[i+3]
        if opcode == 1:
            a[loc] = a[b] + a[c]
        elif opcode == 2:
            a[loc] = a[b] * a[c]
        if opcode == 99:
            break
    return a[0]

print(part1("input.txt"))
