import cv2

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("frontal.xml")
eye = cv2.CascadeClassifier("eye.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        img2 = frame[y: y+h, x: x+h]
        gray2 = gray[y:y + h, x: x + h]

        eyes = eye.detectMultiScale(gray2)

        for x1, y1, w1, h1 in eyes:
            cv2.rectangle(img2, (x1, y1), (x1+w1, y1+h1), (0, 255, 255), 2)

    cv2.imshow("1",frame)

    if ret == 0:
        break
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
