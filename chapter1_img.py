import cv2
print("Package imported")

img = cv2.imread("Resources/iandme.jpeg")

cv2.imshow("Output", img)
cv2.waitKey(0)

