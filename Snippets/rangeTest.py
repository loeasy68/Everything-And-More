# This is a range test for the JSON
#Ranges = [0,64,128,0,128,256] # Weird
#[min0, min1, min2, Max0, Max1, Max2]
Ranges = [0, 128, 0, 0, 256, 0]
test = 160
if (test >= Ranges[2]) and (test <= Ranges[5]):
    print("Gaming")
def rangeTest(range1, range2, range3):
    if range1:
        value = [i for i in range(Ranges[0], Ranges[3] + 1) if True]
        print(value)
    if range2:
        value = [i for i in range(Ranges[1], Ranges[4] + 1) if True]
        print(value)
    if range3:
        value = [i for i in range(Ranges[2], Ranges[5] + 1) if True]
        print(value)
def rangeCheck(min0, min1, min2, Max0, Max1, Max2, test0, test1, test2):
    if not ((test0 >= min0) and (test0 <= Max0)):
        return False
    if not (test1 >= min1) and (test1 <= Max1):
        return False
    if not ((test2 >= min2) and (test2 <= Max2)):
        return False
    return True
rangeTest(True, True, True)
print(rangeCheck(10, 64, 10, 64, 128, 30, 15, 70, 16)) # Should be True