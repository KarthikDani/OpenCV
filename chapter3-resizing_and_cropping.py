import cv2

img = cv2.imread("Resources/iandme.jpeg")
print(img.shape)

imgResize = cv2.resize(img, (250, 500))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Resized Image", imgResize)
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)