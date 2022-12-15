import cv2
import numpy as np

img = cv2.imread("lena.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #bianco e nero
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #sfocato
imgCanny = cv2.Canny(img, 150, 200) #edge detection
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #edge detection with more thickness
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # contrario di dialation

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2.imshow("Erosion", imgEroded)


cv2.waitKey(0)
