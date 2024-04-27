import cv2
import numpy as np

img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("car2",img2)

cv2.imshow("car1",img1)

cv2.imshow("car", img)
cv2.waitKey(0)
cv2.destroyAllWindows()