import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))

print(img)

print(img.shape)

print(img.ndim)

cv2.imshow("Galaxy",img)

cv2.waitKey(0)
