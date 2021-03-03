import cv2
import numpy as np

def picker(event,x,y,flags,param):#call_back_function
    if event == cv2.EVENT_LBUTTONDOWN:#on clicking left_button
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),2,(0,255,255),-1)

        colour_image=np.zeros((1024 , 1024, 3),np.uint8)
        colour_image[:] =[ blue,green,red]

        cv2.imshow("colour_image",colour_image)

img=cv2.imread('aurangzeb.jpg')

cv2.imshow("image",img)

cv2.setMouseCallback('image',picker)

cv2.waitKey(0)
cv2.destroyAllWindows()

