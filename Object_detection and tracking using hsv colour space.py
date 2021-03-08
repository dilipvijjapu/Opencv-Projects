import cv2
import numpy as np

def comeon(x):
    pass

cv2.namedWindow('Track')

cv2.createTrackbar('L_h','Track',0,255,comeon)
cv2.createTrackbar('L_s','Track',0,255,comeon)
cv2.createTrackbar('L_v','Track',0,255,comeon)
cv2.createTrackbar('U_h','Track',255,255,comeon)
cv2.createTrackbar('U_s','Track',255,255,comeon)
cv2.createTrackbar('U_v','Track',255,255,comeon)

while(1):

    img1 = cv2.imread('hsv_image.png')

    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)



    k = cv2.waitKey(1)

    if k == 27:
        break

    l_h = cv2.getTrackbarPos('L_h','Track')
    u_h = cv2.getTrackbarPos('U_h','Track')
    l_s = cv2.getTrackbarPos('L_s','Track')
    u_s = cv2.getTrackbarPos('U_s','Track')
    l_v = cv2.getTrackbarPos('L_v','Track')
    u_v = cv2.getTrackbarPos('U_v','Track')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(img1,img1,mask=mask)

    cv2.imshow('org_img',img1)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

cv2.destroyAllWindows()

#hello
#hai




























