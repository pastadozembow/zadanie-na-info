import random 

def fourInputXOR(a, b, c, d):
    andOne = a & b & c & d
    andTwo = a & b & c
    andDrei = b & c & d
    andFour = a & c & d
    andFive = a & b & d
    bigOR = andTwo | andDrei | andFour | andFive
    return a ^ b ^ c ^ d ^ andOne ^ bigOR

def seedGen():
    while(True):
        uppByte = random.randint(1, 254)
        lowByte = random.randint(1, 254)
        specByte = random.randint(1, 254)
        numByte = random.randint(1, 254)
        if (fourInputXOR(uppByte, lowByte, specByte, numByte) == 255):
            return uppByte, lowByte, specByte, numByte

def charGen(startNum):
    if(startNum == 1):
        return chr(random.randint(ord("A"), ord("Z")))
    elif(startNum == 2):
        return chr(random.randint(ord("a"), ord("z")))
    elif(startNum == 3):
        return chr(random.randint(ord("!"), ord("+")))
    elif(startNum == 4):
        return chr(random.randint(ord("0"), ord("9")))

uppSeed, lowSeed, specSeed, numSeed = seedGen()
seeds = [uppSeed, lowSeed, specSeed, numSeed]
password = ["", "", "", "", "", "", "", ""]
i = 1
it = 0
sqr = 128

for ch in password:
    for sed in seeds:
        if sed >= sqr:
            break
        i += 1
    password[it] = charGen(i)
    seeds[i-1] = sed - sqr
    it = it + 1
    sqr = sqr / 2
    i = 1
    

print(*password)
#print(uppSeed, " ", lowSeed, " ", specSeed, " ", numSeed)

