import numpy as np
import matplotlib.pyplot as plt

def avg_loss(x, y, w, b):
    N = len(x)
    loss = 0.0
    for i in range(N):
        loss +=  (y[i] -(w*x[i] + b))**2
    return loss / float(N)
    
def updateWandB(x, y, w, b, alpha):
    dl_dw = 0.0
    dl_db = 0.0
    N = len(x)

    for i in range(N):
        dl_dw += -2*x[i]*(y[i] - (w*x[i] + b))
        dl_db += -2*(y[i] - (w*x[i] + b))

    w = w - (1/float(N))*dl_dw*alpha
    b = b - (1/float(N))*dl_db*alpha

    return w, b

def train(x, y, w, b, alpha, epochs):
    for e in range(epochs):
        w, b = updateWandB(x, y, w, b, alpha)

        if e % 400 == 0:
            print("epoch:", e, "loss:", avg_loss(x, y, w, b))
    return w, b
def predict(x, w, b):
    pred = []
    for i in range(len(x)):
        pred.append(w*x[i] + b)
    return pred
x = np.arange(10)
y = np.array([1, 10, 17, 27, 32, 45, 47, 80, 90, 100])

w, b = train(x, y, 0.0, 0.0, 0.001, 15000)

xNew = np.arange(0, 20)
yNew = predict(xNew, w, b)
plt.xlim(0, 200)
plt.ylim(0, 200)
plt.scatter(x, y, c='r')
#plt.scatter(xNew, yNew, c='b')
plt.plot([xNew[0], xNew[len(xNew)-1]], [yNew[0], yNew[len(yNew)-1]], c='b')

plt.show()
