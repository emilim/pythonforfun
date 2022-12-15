import numpy as np
from numpy import random

class Node:
    def __init__(self):
        self.x = np.random()
        self.y = np.random()
        self.color = [np.random.next(255), np.random.next(255), np.random.next(255)]
        self.value = np.random()


class Network:
    def __init__(self):
        self.nodes = np.zeros(20)
        self.links = np.zeros((20, 20))

    def test(self):
        print(self.links)


net = Network()
net.test()
