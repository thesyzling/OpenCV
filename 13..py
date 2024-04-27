import cv2
import numpy as np

img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))

blr = cv2.blur(img, (5, 5))
gb = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)
mb = cv2.medianBlur(img, 5)
b = cv2.bilateralFilter(img, 9, 75, 75)


cv2.imshow("b", b)
cv2.imshow("gb", gb)
cv2.imshow("img", img)
cv2.imshow("blr", blr)
cv2.imshow("mb", mb)

cv2.waitKey(0)
cv2.destroyAllWindows()