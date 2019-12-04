import math 

def solve(filename):
    fd = open(filename, "r")
    inputs = [int(x) for x in fd]
    
    res = sum(math.floor(i/3) - 2 for i in inputs) 
    print(res)

solve("input.txt")
