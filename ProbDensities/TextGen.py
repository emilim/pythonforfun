import random
import numpy as np

allChar = list("abcdefghijklmnopqrstuvwxyz '.,")

with open ("data1.txt", "r", encoding="utf8") as myfile:
    data = myfile.read()
data.lower()
datasetChar = list(''.join(c for c in data if c in allChar))

m = len(allChar)
freqMatrix = np.zeros((m, m, m, m, m, m))

N = freqMatrix.ndim

index = np.zeros((N), dtype=int)
for i in range(len(datasetChar)-N):
    for j in range(N):
        index[j] = allChar.index(datasetChar[i + j])
    freqMatrix[index[5]][index[4]][index[3]][index[2]][index[1]][index[0]] += 1#modify when change dimension


sparsity = 1.0 - np.count_nonzero(freqMatrix) / freqMatrix.size
print(sparsity)

def kickStartTotalProb():
    c = int(random.uniform(0, len(datasetChar)))
    cR = []
    for i in range(N):
        cR.append(datasetChar[c+i])
        print(cR[i], end='', flush=True)
    return cR
ch = kickStartTotalProb()

for nTimes in range(1000):
    totalProb = []
    for i in range(len(allChar)):
        index = [0]*(N-1)
        for j in range(N-1):
            index[j] = allChar.index(ch[j])
        totalProb.append(freqMatrix[i][index[4]][index[3]][index[2]][index[1]][index[0]])#modify when change dimension

    if sum(totalProb) > 0:
        r = int(random.uniform(0, sum(totalProb) + 1))
        sumC = 0
        for i in range(len(allChar)):
            sumC += totalProb[i]
            if r <= sumC:
                ch[N-1] = allChar[i]
                print(ch[N-1], end='', flush=True)
                for i in range(N-1):
                    ch[i] = ch[i+1]
                break
    else:
        print('', sep=' ')
        ch = kickStartTotalProb()
            

