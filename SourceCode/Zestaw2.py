import random
import math

def losuj(n):
    a=0
    for i in range (1,n):
        x = random.random()
        y = random.random()
        length = math.sqrt(x * x + y * y)
        if (length < 1):
            a = a+1
    P = 4*(a/n)
    return P

print(losuj(10000000))


