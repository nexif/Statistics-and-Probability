import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import random

def transformacjaBoxMullera(): #generuje liczby o rozkładzie normalnym
    x1 = random.random()
    x2 = random.random()
    return np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)

def genX(n):
    out = np.empty(n)
    for i in range(n):
        out[i] = transformacjaBoxMullera()
    return out 


def randomPoints(n, size):
    tablica = np.empty(size)
    for i in range(size):
        t = genX(n)
        tablica[i] = np.dot(t,t)
    return tablica


tablica = randomPoints(3, 50000) #n = 3

space = np.linspace(0, 20, 100)
plt.figure(dpi=150, clear=True)
plt.hist(tablica, 150, density=True)
plt.plot(space, chi2.pdf(space, df=3))
plt.show()