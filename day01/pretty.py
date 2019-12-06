# solution for part 1
def part1(data):
    return sum(calculate_fuel(mass) for mass in data) 

# solution for part 2 using recursion
def part2(data):
    return sum([calculate_module(mass) for mass in data])

#  calculate the fuel for a module using recursion
def calculate_module(mass):
    addon = calculate_fuel(mass)
    if addon <= 0: return 0
    return addon + calculate_module(addon)

# calculates the fuel needs for a given mass
def calculate_fuel(mass):
    return mass // 3 - 2

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r")]
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
