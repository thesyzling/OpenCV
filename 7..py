import cv2
img = cv2.imread("ferrari.jpg")
img = cv2.resize(img, (1100, 600))
roi = img[500:700, 150:500]
cv2.imshow("roi",roi)


cv2.imshow("windows", img)
cv2.waitKey(0)
cv2.destroyAllWindows()