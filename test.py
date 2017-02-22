from random import randint

goal = 300
nPop = 100
nGene = 4
signs = [0,0,0]

def setSign():
    # 1= +
    # 2= -
    # 3= *
    # 4= /
    signs[0] = randint(1,4)
    signs[1] = randint(1,4)
    signs[2] = randint(1,4)

def firstGen():
    for i in range(nPop):
        individu = []
        for j in range(nGene):
            individu.append(randint(1,90))
        if rating(individu):
            print(i)
            break

def rating(individu):
    res = individu[0]
    for i in range(nGene-1):
        if signs[i] == 0:
            break
        elif signs[i] == 1:
            res = res + individu[i+1]
        elif signs[i] == 2:
            res = res - individu[i+1]
        elif signs[i] == 3:
            res = res / individu[i+1]
        elif signs[i] == 4:
            res = res * individu[i+1]
    print(res)

    if res == goal:
        print(individu[0], "+", individu[1], "+", individu[2], "+", individu[3])
        print("GG, you've did it! 300")
        return True
    return False

def main():
    setSign()
    firstGen()

main()
