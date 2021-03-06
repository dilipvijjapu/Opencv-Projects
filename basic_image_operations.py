import cv2

img1 = cv2.imread('aurangzeb.jpg')
img2 = cv2.imread('jahangir.jpg')

print(img1.shape)
print(img1.size)
print(img2.shape)
print(img2.size)

img1 = cv2.resize(img1 , (512 , 512))
img2 = cv2.resize(img2 , (512 , 512))

new_image = cv2.addWeighted(img1,0.3,img2,0.4,0.2)

cv2.imshow('image',new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()