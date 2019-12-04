

def task1():
    l = 307237
    h = 769058
    res = 0
    for i in range(l,h,1):
        if test_double(i) and test_decreasing(i):
            res += 1
    return res

def test_double(x):
    digit = str(x)
    for i in range(len(str(x))-1):
        if digit[i] == digit[i+1]:
            return True

    return False

def test_decreasing(x):
    digit = str(x)
    for i in range(len(str(x))-1):
        if digit[i] > digit[i+1]:
            return False

    return True


print(task1())
