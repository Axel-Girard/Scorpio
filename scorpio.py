from random import randint
import random
import math

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
    return generation

# compute score of individu
def rating(porte, impact, individu):
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

    if abs(porte - goal) >= 5:
        for i in range(nGene):
            print(individu[i])
        print(" porté= ", round(porte, 3))
        print("impact= ", round(impact,3))

        if Ld > f:
            print("Le bras casse! ",Ld, f)
        if Lv > individu[5]:
            print("Pas de tir: Lv>Lf")
        if individu[4] > individu[1]:
            print("Pas de tir: Lc>La")

def fin(iteration):
    if iteration is not None:
        if iteration >= 0.0:
            print("GG, you did it in",iteration,"iterations!")
            return
    print("No scoprio found, sorry :'(")

def nextGen(pop):
    print(pop)
    return pop

# main function that run others
def main():
    pop = firstGen()
    for i in range(nGeneration):
        pop = nextGen(pop)

main()
