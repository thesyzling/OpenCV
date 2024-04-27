import cv2
import numpy as np
circle = np.zeros((512, 512, 3),np.uint8) +255
cv2.circle(circle,(256,256),50,(255,0,0),-1)

square = np.zeros((512, 512, 3),np.uint8) +255
cv2.rectangle(square,(150,150),(350,350),(120,255,0),-1)

add = cv2.addWeighted(circle, 0.5, square, 0.5, 0)
cv2.imshow("add",add)


cv2.waitKey(0)
cv2.destroyAllWindows()