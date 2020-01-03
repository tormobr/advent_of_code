import time

def part1(data, deck_size):
    cards = [i for i in range(deck_size)]
    for line in data:
        #print(line)
        n = 0
        if "deal into new" not in line:
            n = int(line.split()[-1])

        if "deal into new s" in line:
            cards.reverse()
        if "cut" in line:
            cards = cards[n:] + cards[:n]

        if "deal with inc" in line:
            new_cards = [0 for i in range(deck_size)] 
            index = 0
            for i in range(deck_size):
                new_cards[index%deck_size] = cards[i]
                #print("new_cards:", new_cards)
                index += n 
            cards = new_cards.copy()
    return cards.index(2019)


def deal_into_new(index, deck_size):
    return (-index - 1) % deck_size

def cut(index, deck_size, n):
    return (index - n) % deck_size

def deal_with_inc(index, deck_size, n):
    return (index * n) % deck_size

def part2(data, deck_size, target):
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

if __name__ == "__main__":
    data = [line.strip() for line in open("input.txt")]
    s = time.time()
    print("Part 1 answer:", part1(data, 10007))
    e = time.time()
    print("Runtime: ", e-s)
    n = 10
    s = time.time()
    print("Part 2 answer: ",part2(data, 119315717514047, 2019))
    e = time.time()
    print("Runtime: ", e-s)
