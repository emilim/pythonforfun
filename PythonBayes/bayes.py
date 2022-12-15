import matplotlib.pyplot as plt
import numpy as np

rows, cols = (5, 5)
gridArr = [[0 for i in range(cols)] for j in range(rows)]
probArr = [[0 for i in range(cols)] for j in range(rows)]
fig, ax = plt.subplots(2, 2)
ax[0][0].set_xlim([0, 10]); ax[0][0].set_ylim([0, 10])
totalPoint = 0
def onclick(event):
    global totalPoint
    totalPoint += 1
    sumCol = [0] * cols
    sumRow = [0] * rows
    probCol = [0] * cols
    probRow = [0] * rows

    xDataRound = int(round(event.xdata / 2, 2))
    yDataRound = int(round(event.ydata / 2, 2))

    gridArr[yDataRound][xDataRound] += 1
    for i in range(rows):
        for j in range(cols):
            sumRow[j] += gridArr[j][i]
            sumCol[j] +=  gridArr[i][j]
            probArr[i][j] = gridArr[i][j] / totalPoint
    
    for i in range(len(sumRow)):
        probCol[i] = sumCol[i] / totalPoint
        probRow[i] = sumRow[i] / totalPoint
        

    ax[1][0].clear(); ax[0][1].clear(); ax[0][1].set_xlim([0, 1]); ax[1][0].set_ylim([0, 1]); ax[1][1].set_xlim([0, rows]); ax[1][1].set_ylim([0, cols])

    ax[0][0].scatter(event.xdata, event.ydata, c='g')
    ax[1][0].bar([0, 1, 2, 3, 4], probCol, color='b')
    ax[0][1].barh([0, 1, 2, 3, 4], probRow, color='r')
    ax[1][1].pcolormesh(probArr, vmin=0, vmax=1, cmap='RdBu_r')
    fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
ax[0][0].grid(color='b', linestyle='-', linewidth=2)
plt.show()