

def task1():
    l = 307237
    h = 769058
    res = 0
    digits = []
    for i in range(l,h,1):
        if test_double(i) and test_decreasing(i):
            res += 1
            digits.append(i)
    return res

def test_double(x):
    length = 6
    digit = "X" + str(x) + "X"  # add padding to borders are smooth
    for i in range(1, length):
        if digit[i] != digit[i-1] and digit[i] == digit[i+1] and digit[i] != digit[i+2]:
            return True
    return False 

def test_decreasing(x):
    digit = str(x)
    for i in range(len(str(x))-1):
        if digit[i] > digit[i+1]:
            return False

    return True

print(task1())
