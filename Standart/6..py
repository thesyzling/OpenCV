import cv2
import numpy as np
img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))

img[200, 300, 0] = 0
print(img[200,300])

blue = img.item(150, 150, 0)
print(blue)
img.itemset((150, 150 ,0),200)


cv2.imshow("photo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()