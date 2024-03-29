import cv2, time
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

#time.sleep(3)
while True:
    check, frame = video.read()
    print(check)
    print(frame)
    #time.sleep(3)
    #cv2.imshow('Capture',frame)
    gimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gimg,
    scaleFactor = 1.05,
    minNeighbors = 5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Gray",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows
