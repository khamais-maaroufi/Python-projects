#you have to install opencv2 packages before going further
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#put your photo name with its extension here
img = cv2.imread('example.jfif')
#-------------------------------------------
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gimg,
scaleFactor = 1.05,
minNeighbors = 5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
