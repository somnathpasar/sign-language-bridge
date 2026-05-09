import cv2
import mediapipe as mp
import numpy as np
import csv
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

label = input("Enter sign label: ")

filename = f"dataset/{label}.csv"

camera = cv2.VideoCapture(0)

with open(filename, "a", newline="") as file:

    writer = csv.writer(file)

    while True:

        ret, frame = camera.read()

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = hands.process(rgb)

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                landmarks = []

                for point in hand.landmark:

                    landmarks.append(point.x)
                    landmarks.append(point.y)

                writer.writerow(landmarks)

        cv2.imshow(
            "Collect Data",
            frame
        )

        key = cv2.waitKey(1)

        if key == ord("q"):
            break


camera.release()
cv2.destroyAllWindows()