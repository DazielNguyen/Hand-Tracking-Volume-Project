import cv2 
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
detector = htm.HandDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False) # Chỗ điều khiển đường vẽ hiện thị hay không, nếu True thì sẽ hiện thị
    lmList = detector.findPosition(img, draw=False) # Chỗ điều khiển đường vẽ hiện thị hay không, nếu True thì sẽ hiện thị
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1/(cTime - pTime) 
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
