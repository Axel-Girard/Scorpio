from random import randint

goal = 300

def firstGen():
    for i in range(100):
        a = randint(0,100)
        b = randint(0,100)
        c = randint(0,100)
        d = randint(0,100)
        e = randint(0,100)
        f = randint(0,100)
        if rating(a,b,c,d,e,f):
            break

def rating(a,b,c,d,e,f):
    res = a+b+c+d+e+f
    if res == goal:
        print(a, "+", b, "+", c, "+", d, "+", e, "+", f)
        print("GG, you've did it! 300")
        return True
    return False


firstGen()
