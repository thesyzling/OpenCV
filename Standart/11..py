import cv2
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("cap", frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()