import math 

def part1(filename):
    fd = open(filename, "r")
    inputs = [int(x) for x in fd]
    
    res = sum(i//3 - 2 for i in inputs) 
    return res

def part2(filename):
    fd = open(filename, "r")
    inputs = [int(x) for x in fd]
    res = 0
    for mass in inputs:
        module_fuel = mass // 3 - 2
        while module_fuel > 0:  
            res += module_fuel
            module_fuel = module_fuel //3 -2
    return res
        

print(part1("input.txt"))
print(part2("input.txt"))
