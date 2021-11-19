import numpy as np
import cv2
def nothing(x):
    print("value changed")
#capturing our video from the camera
cap=cv2.VideoCapture(0)
cv2.namedWindow('test')

#creating 3 trackbars for altering values of RGB
cv2.createTrackbar('R','test',0,255,nothing)
cv2.createTrackbar('G','test',0,255,nothing)
cv2.createTrackbar('B','test',0,255,nothing)


while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    k=cv2.waitKey(1)
    if k==27:
        break

    #getting the values of trackbars
    r=cv2.getTrackbarPos('R','test')
    g=cv2.getTrackbarPos('G','test')
    b=cv2.getTrackbarPos('B','test')
    
    #assignming the values to the lower and upper range of HSV
    lower=np.array([b,g,r])
    higher=np.array([255,255,255])

    #creating a mask
    mask=cv2.inRange(hsv,lower,higher)

    #applying mask on the frame
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #displaying the frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

cap.release()
cv2.destroyAllWindows()

