import matplotlib.pyplot as plt
import numpy as np
import math
import random


x = [-1,0,1,2,3]
y = [0,1/3,1/3,1/3,0]
plt.plot(x,y)
plt.show()




def losuj(n):
    for i in range (1,n):
        x = random.random()

        if x < 1/6:
            x = math.sqrt(6*x) - 1
        elif x>=1/6 and x<5/6:
            x=3*x-1/2
        else:
            x=3-math.sqrt(6-6*x)
        tablica.append(x)


tablica = []
N = 100000
losuj(N)
plt.hist(tablica, density=True, bins=40)
plt.ylabel('Probability');
plt.show()

fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].hist(tablica, density=True, bins=40)
plt.show()