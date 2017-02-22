from random import randint

goal = 300
nPop = 10000
nGene = 6
signs = []

# define signes
def setSign():
    # 1= +
    # 2= -
    # 3= *
    # 4= /
    for i in range(nGene-1):
        signs.append(randint(1,4))

# generate first generation
def firstGen():
    for i in range(nPop):
        # angle
        # width of bow
        # base
        # height
        # width of rope
        # width of arrow
        individu = []
        individu.append(randint(0,90))
        individu.append(randint(1,10))
        individu.append(randint(1,10))
        individu.append(randint(1,20))
        individu.append(randint(1,30))
        individu.append(randint(1,20))
        if rating(individu) == goal:
            return i

# compute score of individu
def rating(individu):
    res = individu[0]

    for i in range(nGene-1):
        if signs[i] == 0:
            return 0
        elif signs[i] == 1:
            res = res + individu[i+1]
        elif signs[i] == 2:
            res = res - individu[i+1]
        elif signs[i] == 3:
            res = res / individu[i+1]
        elif signs[i] == 4:
            res = res * individu[i+1]

    if res == goal:
        for i in range(nGene):
            print individu[i]
    return res

def fin(iteration):
    if iteration >= 0:
        print "GG, you did it in",iteration,"iterations!"
    else:
        print "No scoprio found"

# main function that run others
def main():
    setSign()
    fin(firstGen())

main()
