from random import randint
import random
import math
import matplotlib.pyplot as plt
import numpy

goal = 300
nPop = 10
nGene = 6
nGeneration = 50
density = random.uniform(300,2000)
E = random.uniform(10,1000)
poisson = random.uniform(0,0.5)
Df = random.uniform(0,0.25)
g = 9.81

def ressort(E,v):
    res = 1/3
    tmp = 1-2*v
    tmp = E /tmp
    res = res * tmp
    return res

def longeurAVide(Lb, Lc):
    Lb = float(Lb)
    Lb = float(Lc)
    res = math.sqrt(math.pow(Lb, 2)-(0.25*math.pow(Lc,2)))
    return res

def longueurDeplacement(Lf,Lv):
    res = Lf-Lv
    return res

def masseProjectil(p,Df,Lf):
    res = p*Df*Lf
    return res

def velocite(K,Ld,mp):
    res = math.sqrt((K*math.pow(Ld,2))/mp)
    return res

def porte(V,g,a):
    res = math.pow(V,2)/g
    res = res*math.sin(2*math.radians(a))
    return res

def impact(mp,V):
    res = 1/2
    res = res * mp * math.pow(V,2)
    return res

def momentQuadratique(b,h):
    res = b * math.pow(h,3)
    res = res / 12
    return res

def forceTraction(K,Ld):
    res = K * Ld
    return res

def maxFlechBras(F,Lb,E,I):
    res = F * math.pow(Lb,3)
    res = res / (48*E*I)
    return res

# generate first generation
def firstGen():
    generation = []
    for i in range(nPop):
        # 0.angle
        # 1.width of bow
        # 2.base
        # 3.height
        # 4.width of rope
        # 5.width of arrow
        individu = []
        individu.append(random.uniform(0,90))
        individu.append(random.uniform(0,20))
        individu.append(random.uniform(0,20))
        individu.append(random.uniform(0,20))
        a = random.uniform(0,20)
        while math.pow(individu[1], 2)-(0.25*math.pow(a,2)) <= 0:
            a = random.uniform(0,20)
        individu.append(a)
        individu.append(random.uniform(0,20))
        generation.append(individu)
        rating(individu)
    return generation

# compute porte, energy and score of individu
def rating(individu):
    K = ressort(E, poisson)
    Lv = longeurAVide(individu[1], individu[4])
    Ld = longueurDeplacement(individu[5],Lv)
    mp = masseProjectil(density,Df,individu[5])
    V = velocite(K,Ld,mp)
    P = porte(V,g,individu[0])
    Ec = impact(mp,V)
    I = momentQuadratique(individu[2],individu[3])
    F = forceTraction(K, Ld)
    f = maxFlechBras(F,individu[1],E,I)

    individu.append(P)
    individu.append(Ec)

    #
    score = abs(goal-P) * 1000 + Ec/2
    individu.append(score)

    # if abs(P - goal) >= 5:
    #     for i in range(nGene):
    #         print(individu[i])
    #     print(" porté= ", round(P, 3))
    #     print("impact= ", round(Ec,3))
    #
    #     if Ld > f:
    #         print("Le bras casse! ",Ld, f)
    #     if Lv > individu[5]:
    #         print("Pas de tir: Lv>Lf")
    #     if individu[4] > individu[1]:
    #         print("Pas de tir: Lc>La")

def fin(iteration):
    if iteration is not None:
        if iteration >= 0.0:
            print("GG, you did it in",iteration,"iterations!")
            return
    print("No scoprio found, sorry :'(")

# affiche un gene de la population
def printGen(pop, gene):
    for indi in pop:
        print(indi[gene])
    return pop

def nextGen(pop):
    newPop = fitnesse(pop)
    for i in range(len(newPop)):
        rating(newPop[i])
    return newPop

# select parents then initiate croisement
def fitnesse(pop):
    total = 0
    for indi in pop:
        total += indi[6]
    offset = random.uniform(0,total/4)
    newPop = []
    while len(newPop) <= nPop:
        parent1 = getIndiFromOffset(pop, offset, total)
        offset = (offset + offset) % total
        parent2 = getIndiFromOffset(pop,offset, total)
        while parent1 == parent2:
            offset = (offset + offset) % total
            parent2 = getIndiFromOffset(pop,offset, total)
        offset += offset + offset
        newPop.append(croisement(parent1, parent2))

    return newPop

# croise les parents
def croisement(parent1, parent2):
    croise = randint(0,5)
    individu = []
    for i in range(croise):
        individu.append(parent1[i])
    for i in range(croise, nGene):
        individu.append(parent2[i])
    # launch mutation
    isMutation = randint(50,70)
    if randint(0,100) > isMutation:
        mutation(individu)
    return individu

def mutation(individu):
    gene = randint(0,nGene - 1)
    individu[gene] = random.uniform(0,20)

# return individu form offset beside porte
def getIndiFromOffset(pop,offset, maximum):
    porte = 0
    for indi in pop:
        porte = (porte + indi[6]) % maximum
        if porte >= offset:
            return indi
    return pop[0]

# main function that run others
def main():
    print('nGene', nGene)
    print('nPop', nPop)
    print('nGeneration', nGeneration)
    print('density', density)
    print('E', E)
    print('poisson', poisson)
    print('Df', Df)

    pop = []
    pop.append(firstGen())
    currentPopulation = pop[0]
    portes = []
    puissances = []
    notes = []
    moyPortes = []
    moyPuissances = []
    moyNotes = []
    varNotes = []

    for i in range(nGeneration):
        for j in range(nPop):
            portes.append(pop[i][j][6])
            puissances.append(pop[i][j][7])
            notes.append(pop[i][j][8])
        moyPortes.append(numpy.mean(portes))
        portes = []
        moyPuissances.append(numpy.mean(puissances))
        puissances = []
        moyNotes.append(numpy.mean(notes))
        varNotes.append(numpy.var(notes))
        notes = []
        pop.append(nextGen(currentPopulation))
        currentPopulation = pop[len(pop)-1]

    plt.subplot(2,2,1)
    plt.plot(moyPortes)
    plt.title('Porte')

    plt.subplot(2,2,2)
    plt.plot(moyPuissances)
    plt.title('Puissance')

    plt.subplot(2,2,3)
    plt.plot(varNotes)
    plt.title('Variance')

    plt.subplot(2,2,4)
    plt.plot(moyNotes)
    plt.title('Note')
    plt.show()

main()
