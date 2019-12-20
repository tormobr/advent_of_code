import time
import numpy as np
from intcoder import Intcoder
from plotter import Animater
from copy import deepcopy

def part1(data, val):
    dim = val*12
    arr = np.zeros((dim,dim))
    arrays = []
    start_x = 0
    last_xs = np.zeros((dim), dtype=int)
    print(last_xs)
    i = 0
    ship_loc = False
    while i < dim:
        arrays.append(deepcopy(arr))
        found = False
        for j in range(start_x, dim):
            computer = Intcoder(data.copy(), 0)
            out = computer.eval([j,i])    
            arr[i,j] = out
            if out and not found:
                found = True
                start_x = j
            if found and not out:
                last_xs[i] = j-1
                break
        done = False
        if not ship_loc and i > val:
            done, res_i,res_j  = test_array(arr,arrays, i,last_xs[i-val], val=val)
        #if done:
            #ship_loc = True
            #print(done, res_i, res_j)
            #print(arr)
            #return (10000*res_j)+res_i
        print("haxor" , i, np.sum(arr[i]))
        i += 1
    for _ in range(200):
        arrays.append(deepcopy(arr))
    a = Animater(arrays)
    return np.count_nonzero(arr == 1)

def test_array(a, arrays, current_index, last_x, val=99):
    i = current_index-val
    if a[i][last_x-val] == 1 and a[i+val][last_x-val] == 1:
        for i in range(i+val, i-1, -1):
            for j in range(last_x, last_x-val-1, -1):
                a[i,j] = 2
                arrays.append(deepcopy(a))

        return True, i, last_x-val
    return False, 0, 0

def print_beam(arr):
    res = ""
    for y in arr:
        for x in y:
            if x == 1:
                res += "X"
            else:
                res += " "
        res += "\n"
    print(res)

if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    
    print(part1(data,99))
    #print(part2(data))

    


