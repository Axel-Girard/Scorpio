from random import randint
import random
import math

# La distance à atteindre
goal = 300
# Le nombre d'individu par population
nPop = 6
# Le nombre de gène
nGene = 6
# le nombre de génération souhaitée
nGeneration = 2
# Masse volumique
density = random.uniform(300,2000)
# Module de Young
E = random.uniform(10,1000)
# Coeficient de Poisson
poisson = random.uniform(0,0.5)
# Diamètre de la flèche
Df = random.uniform(0,10)
# Gravité, je choisit qu'on est sur la Terre et pas ailleurs
g = 9.81

offset = 50

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
    generation = ""
    for i in range(nPop):
        # 0.angle
        # 1.width of bow
        # 2.base
        # 3.height
        # 4.width of rope
        # 5.width of arrow
        individu = "0,"
        individu += "{0},".format(random.uniform(0,90))
        tmp = random.uniform(0,20)
        individu += "{0},".format(tmp)
        individu += "{0},".format(random.uniform(0,20))
        individu += "{0},".format(random.uniform(0,20))
        tmpp = random.uniform(0,20)
        while math.pow(tmp, 2)-(0.25*math.pow(tmpp,2)) <= 0:
            tmpp = random.uniform(0,20)
        individu += "{0},".format(tmpp)
        individu += "{0}".format(random.uniform(0,20))
        generation += individu + ";"
    return generation

# compute score of individu
def rating(individu):
    gene = []
    for itIndi in individu.split(',')[1:]:
        gene.append(itIndi)
        print(round(float(itIndi),3))
    if len(gene) is nGene:
        K = ressort(E, poisson)
        Lv = longeurAVide(float(gene[1]), float(gene[4]))
        Ld = longueurDeplacement(float(gene[5]),Lv)
        mp = masseProjectil(density,Df,float(gene[5]))
        V = velocite(K,Ld,mp)
        P = porte(V,g,float(gene[0]))
        Ec = impact(mp,V)
        I = momentQuadratique(float(gene[2]),float(gene[3]))
        F = forceTraction(K, Ld)
        f = maxFlechBras(F,float(gene[1]),E,I)

        # if abs(P - goal) <= 5:
        #     print("   -------   Less than 5 meters ", P, "   -------   ")
        #     for i in range(nGene):
        #         print(individu[i])
        #
        # print(" porté= ", round(P, 3))
        # print("impact= ", round(Ec,3))
        #
        # if Ld > f:
        #     print("Le bras casse! ",Ld, f)
        # if Lv > individu[5]:
        #     print("Pas de tir: Lv>Lf")
        # if individu[4] > individu[1]:
        #     print("Pas de tir: Lc>La")
        # print("Portee: {0} Energie cinitique {1}".format(round(P,3),round(Ec,3)))
        return abs(P - goal)
    return 0

# Generate next population
def nextGen(pop):
    population = pop
    rated = ""
    for individu in population.split(';'):
        rated += "{0}, ".format(round(rating(individu),3))
        for gene in individu.split(',')[1:]:
            rated += "{0}, ".format(round(float(gene), 3))
        rated = rated[:-1]
        rated += ";"
    rated = rated[:-1]
    rate = sorted(rated.split(';'))[1:]
    print(rate)
    return population

def fin(iteration):
    if iteration is not None:
        if iteration >= 0.0:
            print("GG, you did it in",iteration,"iterations!")
            return
    print("No scoprio found, sorry :'(")

# main function that run others
def main():
    print("Masse volumique: {0}".format(round(density,3)))
    print("Module de Young: {0}".format(round(E,3)))
    print("Coef de Poisson: {0}".format(round(poisson,3)))
    pop = firstGen()
    for i in range(nGeneration):
        print("{0} generation".format(i+1))
        pop = nextGen(pop)

main()
