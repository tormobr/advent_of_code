# solution for part 1
def part1(data):
    return sum(calculate_fuel(mass) for mass in data) 

# solution for part 2
def part2(data):
    return sum(calculate_module(mass) for mass in data)

# calculates the fuel needs for a given mass
def calculate_fuel(mass):
    return mass // 3 - 2

# advanced calculation for fuel based on mass (used in part 2)
def calculate_module(mass):
    total = 0
    addon = calculate_fuel(mass)
    while addon > 0:
        total += addon
        addon = calculate_fuel(addon)
    return total


if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r")]
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
