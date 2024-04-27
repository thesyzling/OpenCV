import cv2
import numpy as np

img = cv2.imread("park.jpg")
img = cv2.resize(img, (1000, 700))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 100, 250)
line = cv2.HoughLinesP(edge, 1, np.pi/180, 100)
print(edge)

for i in line:
    x1, x2, y1, y2 =i[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv2.imshow("park", img)

cv2.waitKey(0)
cv2.destroyAllWindows()