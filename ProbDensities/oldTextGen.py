import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

allChar = list("abcdefghijklmnopqrstuvwxyz '.,")

def validDataset(tempDataset):
    datasetReturn = []
    for data in tempDataset:
        for char in allChar:
            if data == char:
                datasetReturn.append(data)
    return datasetReturn

with open ("data1.txt", "r", encoding="utf8") as myfile:
    data = myfile.read()
data.lower()
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
data = open(path_to_file, 'rb').read().decode(encoding='utf-8')
data.lower()
datasetChar = validDataset(list(data))
matrix = np.array([[0 for x in range(len(allChar))] for y in range(len(allChar))])
matrix2 = np.array([[[0 for x in range(len(allChar))] for y in range(len(allChar))] for z in range(len(allChar))])
matrix3 = np.array([[[[0 for x in range(len(allChar))] for y in range(len(allChar))] for z in range(len(allChar))] for w in range(len(allChar))])
for i in range(len(datasetChar)-3):
    index1 = allChar.index(datasetChar[i])
    index2 = allChar.index(datasetChar[i + 1])
    index3 = allChar.index(datasetChar[i + 2])
    index4 = allChar.index(datasetChar[i + 3])
    matrix[index2][index1] += 1
    matrix2[index3][index2][index1] += 1
    matrix3[index4][index3][index2][index1] += 1


for i in range(len(matrix)):
    for j in range(len(matrix)):
        for z in range(len(matrix2)):
            matrix[i][j] += matrix2[i][j][z]

ch1, ch2, ch3, ch4 = 'm', 'a', 'n', 'n'
print(ch1, end='', flush=True)
print(ch2, end='', flush=True)
print(ch3, end='', flush=True)

for nTimes in range(1000):
    totalProb = []
    for i in range(len(allChar)):
        index1 = allChar.index(ch1)
        index2 = allChar.index(ch2)
        index3 = allChar.index(ch3)
        totalProb.append(matrix3[i][index3][index2][index1])
        
    r = int(random.uniform(0, sum(totalProb)))
    sumC = 0
    for i in range(len(allChar)):
        sumC += totalProb[i]
        if r <= sumC and sum(totalProb) >= 1:
            ch4 = allChar[i]
            break
        else:
            ch4 = '.'
    print(ch4, end='', flush=True)
    ch1 = ch2
    ch2 = ch3
    ch3 = ch4

    

for i in range(len(matrix)):
    for j in range(len(matrix)):
        for z in range(len(matrix2)):
            matrix[i][j] += matrix2[i][j][z]

ch1, ch2, ch3 = 'm', 'a', 'n'
print(ch1, end='', flush=True)
print(ch2, end='', flush=True)

for nTimes in range(1000):
    mat = []
    totalProb = 0
    for i in range(len(allChar)):
        index1 = allChar.index(ch1)
        index2 = allChar.index(ch2)
        totalProb += matrix2[i][index2][index1]
        mat.append(matrix2[i][index2][index1])
        
    r = int(random.uniform(0, totalProb))
    sumC = 0
    for i in range(len(allChar)):
        sumC += mat[i]
        if r <= sumC:
            ch3 = allChar[i]
            break
    print(ch3, end='', flush=True)
    ch1 = ch2
    ch2 = ch3

tempCol = [0]*len(matrix)
for row in matrix:
    for i in range(len(matrix)):
        tempCol[i] += row[i]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] /= tempCol[j] if tempCol[j] != 0 else 1


t = random.randint(0, len(allChar)-1)
for nTimes in range(1000):
    colSum = 0
    r = random.uniform(0, 1)
    for i in range(len(matrix)):
        colSum += matrix[i][t]
        if r <= colSum:
            print(allChar[i], end='', flush=True)
            t = i
            break
