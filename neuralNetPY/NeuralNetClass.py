'''
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def makePrediction(inputVec, weights, bias):
    layer1 = np.dot(inputVec, weights) + bias
    layer2 = sigmoid(layer1)
    return layer1

inputVector = np.array([2, 4])
weights = np.array([2, 1])
bias = np.array([0.0])

for i in range(10):
    prediction = makePrediction(inputVector, weights, bias)
    inputVector = np.append(inputVector, prediction)
    weights = np.append(weights, 1)
    print(prediction)
'''

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def makePrediction(inputVec, weights, bias):
    layer1 = np.dot(inputVec, weights) + bias
    layer2 = sigmoid(layer1)
    return layer2

inputVector = np.array([2, 4])
weights = np.array([2, 1])
bias = np.array([0.0])
prediction = makePrediction(inputVector, weights, bias)

target = 0
mse = (prediction - target) ** 2
derivative = 2 * (prediction - target)
print("Prediction:", prediction, "Error:", mse, "Derivative:", derivative)


#Error fixing
weights = weights - derivative
prediction = makePrediction(inputVector, weights, bias)
mse = (prediction - target) ** 2
print("Prediction:", prediction, "Error:", mse, "Derivative:", derivative)

