import cv2
import numpy as np

canvas = np.zeros((600,600,3), np.uint8) +255

f1 = cv2.FONT_ITALIC
f2 = cv2.FONT_HERSHEY_PLAIN
f3 = cv2.CAP_AVFOUNDATION

cv2.putText(canvas,"merhaba dunya",(30,200),f2,4,(255,0,0), cv2.LINE_AA)


cv2.imshow("window", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()