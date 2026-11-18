"""Webcam hand tracking and five-finger state filtering.

Reconstructed from the original Python script shared by the project author.
This version displays/prints the tracking output but does not yet send serial
commands to the Arduino. The Arduino control portion is documented in README.
"""

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.4)

histories = [[], [], [], [], []]
HISTORY_SIZE = 10

# Connections between the 21 MediaPipe hand landmarks
connections = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17),
]

print("Hand tracking started")

try:
    while True:
        success, img = cap.read()
        if not success:
            continue

        hands, img = detector.findHands(img, draw=True)

        if hands:
            lmList = hands[0]["lmList"]

            # Detect thumb along the x-axis
            fingers = [1 if lmList[4][0] < lmList[3][0] else 0]

            # Detect remaining fingers along the y-axis
            for tipId in [8, 12, 16, 20]:
                fingers.append(
                    1 if lmList[tipId][1] < lmList[tipId - 2][1] else 0
                )

            print("Raw Data:", fingers)

            stability_check = []
            for i in range(5):
                histories[i].append(fingers[i])
                if len(histories[i]) > HISTORY_SIZE:
                    histories[i].pop(0)

                if len(histories[i]) == HISTORY_SIZE:
                    if sum(histories[i]) >= 7:
                        stability_check.append(1)
                    else:
                        stability_check.append(0)
                else:
                    stability_check.append(fingers[i])

            print("Stable Vals:", stability_check)

            # Each state maps to a binary servo endpoint (0 or 180 degrees)
            angles = [180 if f == 1 else 0 for f in stability_check]
            print("Angles:", angles)

            if all(f == 0 for f in stability_check):
                state = "CLOSED"
            elif all(f == 1 for f in stability_check):
                state = "OPEN"
            else:
                state = "PARTIAL"

            send_data = stability_check
            print("State:", state)
            print("Sending to Arduino:", send_data)
            # NOTE: The supplied script only prints send_data;
            # it does not contain a pyserial write operation.

            # Draw the hand skeleton and landmark dots
            for first, second in connections:
                pt1 = tuple(lmList[first][0:2])
                pt2 = tuple(lmList[second][0:2])
                cv2.line(img, pt1, pt2, (0, 255, 0), 2)

            for lm in lmList:
                cv2.circle(img, (lm[0], lm[1]), 5, (0, 0, 255), cv2.FILLED)

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
