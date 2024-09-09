binary = []
def decToBin(x):
    if(x == 0):
        return 0
    else:
        while(x != 0):
            if(x % 2 == 0):
                binary.append(0)
            else:
                binary.append(1)
            x = x >> 1
        binary.reverse()
        return binary

print(decToBin(120))