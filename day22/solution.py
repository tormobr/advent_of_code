
def part1(data):
    cards = [i for i in range(119315717514047)]
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
            new_cards = [0 for i in range(119315717514047)] 
            index = 0
            for i in range(119315717514047):
                new_cards[index%119315717514047] = cards[i]
                #print("new_cards:", new_cards)
                index += n 
            cards = new_cards.copy()
    print(cards.index(2020))

if __name__ == "__main__":
    data = [line.strip() for line in open("input.txt")]
    part1(data)
