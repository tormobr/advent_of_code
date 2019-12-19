import time
import numpy as np
from intcoder import Intcoder

def part1(data, val):
    dim = val*100
    arr = np.zeros((dim,dim))
    start_x = 0
    last_xs = [0]*val
    i = val
    while True:
        found = False
        print("start_x : ", start_x)
        for j in range(start_x, dim):
            computer = Intcoder(data.copy(), 0)
            out = computer.eval([j,i])    
            arr[i][j] = out
            if out and not found:
                found = True
                start_x = j
            if found and not out:
                print("strudel")
                last_xs.append(j-1)
                print("breaking at: ", j)
                break

            done, res_i,res_j  = test_array(arr, i,last_xs[i-val], val=val)
            if done:
                print(done, res_i, res_j)
                return (10000*res_j)+res_i
        print("haxor" , i, np.sum(arr[i]))
        i += 1

    return np.count_nonzero(arr == 1)

def test_array(a, current_index, last_x, val=99):
    i = current_index-val
    if a[i][last_x-val] == 1 and a[i+val][last_x-val] == 1:
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

    


