import random
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin
import numpy as np

n = 100
point = np.array([[None] * 2] * n)
for i in range(n):
    point[i, 0] = random.randrange(0, 100)
    point[i, 1] = random.randrange(0, 100)
plt.scatter(point[:, 0], point[:, 1])
plt.show()

def find_clusters(x, n_clusters, rseed=2):
    rng = np.random.RandomState(rseed)
    i = rng.permutation(x.shape[0])[:n_clusters]
    centers = x[i]

    while True:
        labels = pairwise_distances_argmin(x, centers)
        
        #Find new centers from means of points
        new_centers = np.array([x[labels == i].mean(0) for i in range(n_clusters)])
        
        #Check for convergence
        if np.all(centers == new_centers):
            break
        centers = new_centers
    
    return centers, labels

center, labels = find_clusters(point, 2)

plt.scatter(center[:, 0], center[:, 1])
plt.show()