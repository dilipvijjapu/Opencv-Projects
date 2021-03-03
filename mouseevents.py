import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        fonta = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ',' + str(y)
        cv2.putText(img,strxy,(x,y),fonta,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('image',img)
img = np.zeros((1024,1024,3), np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

