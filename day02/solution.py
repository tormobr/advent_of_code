

def part1(filename):
    a = [int(x) for x in open(filename).read().split(",")]
    a[1] = 12
    a[2] = 2
    for i in range(0, len(a), 4):
        opcode = a[i]
        b = a[i+1]
        c = a[i+2]
        loc = a[i+3]
        if opcode == 1:
            a[loc] = a[b] + a[c]
        elif opcode == 2:
            a[loc] = a[b] * a[c]
        elif opcode == 99:
            break
    return a[0]


def part2(filename):
    intcodes = [int(x) for x in open(filename).read().split(",")]
    for noun in range(100):
        for verb in range(100):
            a = intcodes.copy()

            a[1] = noun
            a[2] = verb

            for i in range(0, len(a), 4):
                opcode = a[i]
                b = a[i+1]
                c = a[i+2]
                loc = a[i+3]
                if opcode == 1:
                    a[loc] = a[b] + a[c]
                elif opcode == 2:
                    a[loc] = a[b] * a[c]
                elif opcode == 99:
                    break
                i += 4
            if a[0] == 19690720:
                return noun*100 + verb
            

print(part1("input.txt"))
print(part2("input.txt"))


