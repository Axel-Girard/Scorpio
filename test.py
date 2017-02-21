from random import randint

goal = 300

def firstGen():
    for i in range(10):
        a = randint(0,100)
        b = randint(0,100)
        c = randint(0,100)
        d = randint(0,100)
        e = randint(0,100)
        f = randint(0,100)
        print("a+b+c+d+e+f: ", a+b+c+d+e+f)
        rating(a,b,c,d,e,f)

def rating(a,b,c,d,e,f):
    res = a+b+c+d+e+f
    if res == goal
        print("gg, you've did it!")


firstGen()
