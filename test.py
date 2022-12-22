import cv2
import numpy as np
cam=cv2.VideoCapture("C:/Users/xps/Downloads/ahmed shaban.mp4")
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sampleNum=0
while (True):
    ret,img=cam.read()
    faces=detector.detectMultiScale(img,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("fainal data set/ahmed shaban/User."+str(sampleNum)+".jpg",img[y:y+h,x:x+w])
        cv2.imshow('frame',img)
        #sendMsg(msg)

    if cv2.waitKey(10) & 0xff ==ord('q'):
        break
    elif sampleNum >1000:
        break
        
cam.release()
cv2.destroyAllWindows()
