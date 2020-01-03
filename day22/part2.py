
def part2(data, deck_size, shuffles, target):
    a, b = 1,0
    for line in data:
        n = 0
        if "deal into new" in line:
            a,b = deal_into_new(deck_size, a, b)
        else:
            n = int(line.strip().split()[-1])

        if "cut" in line:
            a,b = cut(deck_size, a, b, n)

        elif "deal with inc" in line:
            a,b = deal_with_inc(deck_size, a, b, n)

    r = (b * pow(1-a, deck_size-2, deck_size)) % deck_size
    res = ((target - r) * pow(a, shuffles*(deck_size-2), deck_size) + r) % deck_size
    return res


def deal_into_new(deck_size, a, b):
    return (-a % deck_size, (deck_size-1-b) % deck_size)

def cut(deck_size, a, b, n):
    return (a, (b-n) % deck_size)

def deal_with_inc(deck_size, a, b, n):
    return (a*n % deck_size, b*n % deck_size)

if __name__ == "__main__":
    deck_size = 119315717514047
    shuffles = 101741582076661
    target = 2020
    data = [line.strip() for line in open("input.txt")]
    print("Part 2 answer: ", part2(data, deck_size, shuffles, target))
