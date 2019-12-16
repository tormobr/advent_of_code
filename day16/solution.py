import numpy as np
def part1(data):
    out = data
    for i in range(100):
        out = phase(out)
    return out

def phase(inn):
    print("new phase")
    out = []
    for i in range(len(inn)):
        full = np.zeros((len(inn)+1))
        #print(np.shape(full))
        #print(np.shape(inn))
        pattern = [0,1,0,-1]
        index = 0
        for j in range(len(full)):
            for k in range(i+1):
                if index < len(full):

                    #print("adding here")
                    full[index] = pattern[j%4]
                    index += 1
            j += i+1
        #print("full:", full)
        full = full[1:]
        multi = inn * full
        #print("inn:", inn)
        #print("full:", full)
        #print("multi:", multi)
        total = int(np.sum(inn*full))

        #for x,y in zip(inn, full):
            #tmp = x*y
            #total += tmp
        last = int(str(total)[-1])
        out.append(last)
        #print(out)
    #out = "".join([str(x) for x in out])
    return out
        

string = open("input.txt").read().strip()
data = np.array([int(x) for x in string])

print(part1(data))
