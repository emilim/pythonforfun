import random
import numpy as np
import tensorflow as tf
from scipy.sparse import csr_matrix

allChar = list("abcdefghijklmnopqrstuvwxyz '.,")

path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
data = open(path_to_file, 'rb').read().decode(encoding='utf-8')
data = data.lower()

# define the n-gram size
N = 7

# initialize a sparse matrix with the appropriate shape
m = len(allChar)
# csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])

freqMatrix = csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
# create a mapping from characters to indices
charToIndex = dict(zip(allChar, range(m)))

# extract all n-grams from the data and update the frequency matrix
for i in range(len(data)-N):
    ngram = tuple(data[i:i+N])
    if all(c in allChar for c in ngram):
        indices = [charToIndex[c] for c in ngram]
        freqMatrix[indices] += 1

sparsity = 1.0 - np.count_nonzero(freqMatrix) / np.prod(freqMatrix.shape)
print("Sparsity: {:.4f}".format(sparsity))

def kickStartTotalProb():
    c = int(random.uniform(0, len(data)-N))
    cR = list(data[c:c+N])
    print(''.join(cR), end='', flush=True)
    return cR

ch = kickStartTotalProb()

for nTimes in range(1000):
    totalProb = []
    for i in range(len(allChar)):
        ngram = tuple(ch[1:]) + (allChar[i],)
        if all(c in allChar for c in ngram):
            indices = [charToIndex[c] for c in ngram]
            totalProb.append(freqMatrix[indices])
        else:
            totalProb.append(0)

    if sum(totalProb) > 0:
        r = int(random.uniform(0, sum(totalProb) + 1))
        sumC = 0
        for i in range(len(allChar)):
            sumC += totalProb[i]
            if r <= sumC:
                ch[N-1] = allChar[i]
                print(ch[N-1], end='', flush=True)
                for j in range(N-2):
                    ch[N-2-j] = ch[N-3-j]
                ch[0] = allChar[i]
                break
    else:
        print('', sep=' ')
        ch = kickStartTotalProb()
