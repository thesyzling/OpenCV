import cv2
import numpy as np
canvas = np.zeros((500, 500, 3), np.uint8) + 255
""""
cv2.line(canvas,(100,100),(300,300),(0,0,255),thickness=5)
cv2.line(canvas,(250,250),(330,400),(255,0,0),8)
"""
cv2.rectangle(canvas,(50,50),(80,80),(0,255,0),-1)

cv2.circle(canvas,(100,100),100,(255,0,0),4)

u1 = (300,300)
u2 = (300,200)
u3 = (500,250)

cv2.line(canvas,u1,u2,(0,0,0),4)
cv2.line(canvas,u2,u3,(0,0,0),4)
cv2.line(canvas,u1,u3,(0,0,0),4)


cv2.imshow("window", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()