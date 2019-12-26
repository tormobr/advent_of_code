
def part1(data, n):
    cards = [i for i in range(n)]
    for line in data:
        print(line)
        n = 0
        if "deal into new" not in line:
            n = int(line.split()[-1])

        if "deal into new s" in line:
            cards.reverse()
        if "cut" in line:
            cards = cards[n:] + cards[:n]

        if "deal with inc" in line:
            new_cards = [0 for i in range(n)] 
            index = 0
            for i in range(n):
                new_cards[index%n] = cards[i]
                #print("new_cards:", new_cards)
                index += n 
            cards = new_cards.copy()
    print(cards.index(2019))

if __name__ == "__main__":
    data = [line.strip() for line in open("input.txt")]
    part1(data)
