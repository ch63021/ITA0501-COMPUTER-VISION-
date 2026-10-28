
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Normal Video", frame)

        key = cv2.waitKey(30) & 0xFF

        if key == ord('s'):
            cv2.imshow("Slow Motion", frame)
            cv2.waitKey(200)

        elif key == ord('f'):
            cv2.imshow("Fast Motion", frame)

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
