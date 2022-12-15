import matplotlib.pyplot as plt
import numpy as np

'''
cnums = np.arange(5) + 1j * np.arange(6,11)
print(cnums)
X = [x.real for x in cnums]
Y = [x.imag for x in cnums]
plt.scatter(X,Y, color='red')
plt.show()
'''
n = (1j + 1)
iIns = [n ** i for i in np.arange(0.0, 10, 0.1)]
x = [x.real for x in iIns]
y = [y.imag for y in iIns]

#plt.scatter(x, y, color='red')
plt.plot(x, y, color='red')

plt.show()
