import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 350
pts1 = np.float32([[428, 252], [874, 47], [1015, 366], [571, 564]])
pts2 = np.float32([[0,0], [0, width], [width, height], [width, 0]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Original Image", img)
cv2.imshow("OUTPUT Image", imgOutput)
cv2.waitKey(0)