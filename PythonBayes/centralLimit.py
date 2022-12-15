import matplotlib.pyplot as plt
from numpy import random

N = 1000
M = 10 #aumenta questo valore e tenderà alla gaussiana
x = []
for i in range(N):
    xSum = 0
    for j in range(M):
        xSum += random.uniform(0, 1) #cambia la funzione e tenderà sempre alla gaussiana
    xSum /= M
    x.append(xSum)
    
plt.hist(x, bins=50)
plt.show()


