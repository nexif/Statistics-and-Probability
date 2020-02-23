import matplotlib.pyplot as plt
import numpy as np
import math
import random

#zakładamy lambda = 4

# def losuj(n):
#     for i in range (1,n):
#         x = random.random()
#
#         if x < 1/6:
#             x = math.sqrt(6*x) - 1
#         elif x>=1/6 and x<5/6:
#             x=3*x-1/2
#         else:
#             x=3-math.sqrt(6-6*x)
#         tablica.append(x)




tablica = []
k = 16
lamb = 4

def rozklad_oczekiwany(k):
    for i in range (0,k):
        tablica.append(poisson_wzor(i))

def poisson_wzor(i):
    result = (math.pow(lamb,i)*math.exp(-lamb))/math.factorial(i)
    return result



rozklad_oczekiwany(k) #wyliczany ze wzoru
plt.plot(tablica, 'ro')
plt.grid()
plt.axis([0,14,0,0.2])
plt.ylabel('Wykres wyliczony bezposrednio ze wzoru');
#plt.show()



def generator_liczb():
    q = math.exp(-lamb)
    s = q
    p = q
    u = random.random()
    k = 0
    if u > s:
        while u>s:
            k = k + 1
            p = (p * lamb) / k
            s = s + p
        return k
    else:
        return k

tablica2 = []
N = 3000000
for i in range (0,N):
    tablica2.append(generator_liczb())
plt.hist(tablica2,density = True, bins=15)
plt.axis([0,14,0,0.2])
#plt.show()

fig, axs = plt.subplots(2)
axs[0].plot(tablica, 'ro')
axs[1].hist(tablica2,density = True, bins=15)
plt.show()
