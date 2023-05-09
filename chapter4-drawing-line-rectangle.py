import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img)

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 1)
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2) # or cv2.FILLED can also be used
cv2.circle(img, (450, 100), 30, (255, 255, 0), 2)
cv2.putText(img, "Hello Karthik!", (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 150, 0), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)