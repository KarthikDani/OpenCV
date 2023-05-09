import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 1278)
cap.set(4, 720)

while True:
    success, img = cap.read()
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGrey, scaleFactor=1.1, minNeighbors=5)
    

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Video", img)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

# img = cv2.imread("Resources/iandme.jpeg")
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(imgGrey, scaleFactor=1.1, minNeighbors=5)

# for(x,y,w,h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("Image", img)
# cv2.waitKey(0)