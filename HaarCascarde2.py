import cv2
cap = cv2.VideoCapture(0)

yuz = cv2.CascadeClassifier("frontal.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = yuz.detectMultiScale(gray, 1.2, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("1", frame)

    if cv2.waitKey(50) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
