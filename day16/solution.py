import time
import numpy as np
def part1(data):
    out = data
    for i in range(100):
        out = phase(out)
    return out

def part2(data):
    print(data)
    message_offset = int("".join([str(x) for x in data[:7]]))
    print(message_offset)
    print(len(data))
    out = data[message_offset:]
    for i in range(100):
        out = phase2(out)
        print(i)
        #print(out)
    return out[:9]

def get_pattern(iteration, out_index):
    pattern = [0,1,0,-1]
    pattern_index  = (iteration +1) // (out_index + 1) % 4
    return pattern[pattern_index]


def phase2(inn):
    print("new phase")
    s = sum(inn)
    out = []
    for i in range(len(inn)):
        out += [((s % 10)+ 10)%10]
        s -= inn[i]
    return out

def phase(inn):
    print("new phase")
    out = []
    basic_pattern = [0,1,0,-1] 
    for i in range(len(inn)):
        repeated = np.repeat(basic_pattern, i+1)
        full = np.tile(repeated, len(inn) // len(repeated)+1)
        full = np.roll(full, -1)
        full = full[:len(inn)]
        multi = inn * full
        total = int(np.sum(inn*full))

        last = int(str(total)[-1])
        out.append(last)
    return out
        

string = open("input.txt").read().strip()
list_data = [int(x) for x in string]
 
data1 = np.array(list_data)

print(part1(data1.copy()))
#data2 = np.array(list_data*10000)
#print(part2(data2.copy()))
