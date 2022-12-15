import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from PIL import Image
from numpy import asarray
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()

    imgArray = asarray(img)
    data = imgArray / 255.0
    data = data.reshape(480 * 640, 3)
    
    kmeans = MiniBatchKMeans(128)
    kmeans.fit(data)
    new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

    img_recolored = new_colors.reshape(imgArray.shape)

    cv2.imshow('img', img_recolored)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
