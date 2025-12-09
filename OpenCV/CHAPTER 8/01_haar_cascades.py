# https://github.com/opencv/OpenCV/tree/master/data/haarcascades

import cv2

face_cascade = cv2.CascadeClassifier('CHAPTER 8\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) # 1.1 is scalefactor(how much to zoom in), 5 is minNieghbor's(when it passes 3 times as a face)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        """
        x,y - top left corner 
        (x+w, y+h) 
        
        face = [
            (100,150,80,80) face1
            (250,120,90,90) face2
        ]
        
        x - how far from left
        y - how far from top
        w - width of face
        h - height of face
        """
    cv2.imshow('Webcam Face Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        