import numpy as np
from intcoder import Intcoder 

def part1(data):
    computer = Intcoder(data, 0)
    ret = 0 
    tile_id = 0
    arr = np.zeros((45,23))
    while tile_id != -1:
        x = computer.eval([None])
        y = computer.eval([None])
        tile_id = computer.eval([None])
        if tile_id == 2:
            ret += 1
        arr[x,y] = tile_id
    return ret
def draw_frame(arr):
    pass
    

def part2(data):
    data[0] = 2
    computer = Intcoder(data, 0)
    ret = 0 
    tile_id = 0
    current_score = 0
    while tile_id != -1:
        x = computer.eval([0])
        y = computer.eval([0])
        ret3 = computer.eval([0])
        if x == -1 and y == 0:
            current_score = ret3
        else:
            tile_id = ret3
        print(current_score)
    return current_score
if __name__ == "__main__":
    data = {i:int(x) for (i,x) in  enumerate(open("input.txt", "r").read().split(","))}
    print("part 1 res :" ,part1(data))
