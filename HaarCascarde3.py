import cv2

img = cv2.imread("face.jpg")

face = cv2.CascadeClassifier("frontal.xml")
eye = cv2.CascadeClassifier("eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("gray",gray)

faces = face.detectMultiScale(gray, 1.3, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img2 = img[y: y+h, x: x+h]
    gray2 = gray[y:y + h, x: x + h]

    eyes = eye.detectMultiScale(gray2)

    for x1, y1, w1, h1 in eyes:
        cv2.rectangle(img2, (x1, y1), (x1+w1, y1+h1), (0, 255, 255), 2)

cv2.imshow("1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
