import time

def part1(data, deck_size, target):
    for line in data:
        n = 0
        if "deal into new" in line:
            target = deal_into_new(target, deck_size)
        else:
            n = int(line.strip().split()[-1])

        if "cut" in line:
            target = cut(target, deck_size, n)

        elif "deal with inc" in line:
            target = deal_with_inc(target, deck_size, n)
    return target

def deal_into_new(index, deck_size):
    return (-index - 1) % deck_size

def cut(index, deck_size, n):
    return (index - n) % deck_size

def deal_with_inc(index, deck_size, n):
    return (index * n) % deck_size


if __name__ == "__main__":
    data = [line.strip() for line in open("input.txt")]
    print("Part 1 answer:", part1(data, 10007, 2019))

