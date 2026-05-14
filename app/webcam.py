import cv2
import requests

SERVER_URL = "http://127.0.0.1:5000/predict"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Currency Recognition", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):  # Press 's' to detect currency
        cv2.imwrite("currency.jpg", frame)
        files = {'file': open("currency.jpg", "rb")}
        response = requests.post(SERVER_URL, files=files)
        print("Detected Currency:", response.json())

    elif key == ord('q'):  # Quit
        break

cap.release()
cv2.destroyAllWindows()
