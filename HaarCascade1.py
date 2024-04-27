import cv2

img = cv2.imread("face.jpg")

face = cv2.CascadeClassifier("frontal.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray, 1.3, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()