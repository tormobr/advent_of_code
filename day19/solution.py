import numpy as np
from intcoder import Intcoder

def part1(data):
    arr = np.zeros((1000,1000))

    start_x = 0
    for i in range(1000):
        print(i, np.count_nonzero(arr[i-1] == 1))
        found = False
        for j in range(start_x, 1000):
            computer = Intcoder(data.copy(), 0)
            out = computer.eval([j,i])    
            if out and not found:
                found = True
                start_x = j
            if found and not out:
                break


            arr[i][j] = out

    print(print_beam(arr))
    return np.count_nonzero(arr == 1)

def part2(data):
    arr = None
    for dim in range(34,37):
        print("new dim :" , dim)
        start_x = dim-1
        end_x = 0
        arr = np.zeros((dim+1,dim+1))

        for i in range(dim):
            for j in range(dim):
                computer = Intcoder(data.copy(), 0)
                out = computer.eval([j,i])    
                arr[i][j] = out
        print(test_array(arr))        
    return np.count_nonzero(arr == 1)

def test_array(a):
    for i in range(len(a)):
        if np.count_nonzero(a[i] == 1) == 10:
            hax = np.count_nonzero(a[i+10] == 1)
            if hax == 10:
                return True, i
    return False, 0

def print_beam(arr):
    arr = np.where(arr == 1, "#", "  ")
    res = " "
    for y in arr:
        for x in y:
            res+=x
        res += "\n"
    print(res)

if __name__ == "__main__":

    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    
    print(part1(data))
    #print(part2(data))
