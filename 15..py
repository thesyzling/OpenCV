import cv2
import numpy as np

img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))

sat, sut, _ = img.shape

m = cv2.getRotationMatrix2D((sut/2,sat/2),180,1)

d = cv2.warpAffine(img, m,(sut,sat))

cv2.imshow("car", d)

cv2.waitKey(0)
cv2.destroyAllWindows()