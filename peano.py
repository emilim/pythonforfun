from matplotlib import pyplot as plt
import math

A = [0, 100]
B = [300, 100]
fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)
def drawKoch(a, b, n):
    l = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    h = (l * 3 ** (1/2)) / 6
    cx = (b[0]-a[0])/3 + a[0]
    cy = (b[1]-a[1])/3 + a[1]
    ex = (b[0]-a[0])/3 * 2 + a[0]
    ey = (b[1]-a[1])/3 * 2 + a[1]
    pMediox = (b[0] + a[0]) / 2
    pMedioy = (b[1] + a[1]) / 2
    #alpha = math.atan((b[1] - a[1]) / (b[0] - a[0]))
    #px = pMediox + (h * math.sin(alpha))
    #py = pMedioy + (h * math.cos(alpha))
    px = (h * (a[1] - b[1]) / l) + pMediox
    py = (h * (b[0] - a[0]) / l) + pMedioy
    x = [a[0], cx, px, ex,  b[0]]
    y = [a[1], cy, py, ey, b[1]]
    if n == 1:
        ax.plot(x, y, c='r')
    else:
        drawKoch(a, [cx, cy], n - 1)
        drawKoch([cx, cy], [px, py], n - 1)
        drawKoch([px, py], [ex, ey], n - 1)
        drawKoch([ex, ey], b, n - 1)
    

drawKoch(A, B, 5)
plt.show()
