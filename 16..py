import cv2
import numpy as np

img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corner = cv2.goodFeaturesToTrack(gray, 40, 0.01, 10)

corner = np.int0(corner)

for c in corner:
    x, y = c.ravel()

    cv2.circle(img,(x,y),3,(255,0,0), -1)

cv2.imshow("ferrari", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
