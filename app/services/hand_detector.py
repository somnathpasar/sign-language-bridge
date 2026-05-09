import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1
)


def extract_landmarks(image_bytes):

    image = cv2.imdecode(
        np.frombuffer(
            image_bytes,
            np.uint8
        ),
        cv2.IMREAD_COLOR
    )


    rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )


    results = hands.process(rgb)


    if not results.multi_hand_landmarks:
        return None


    landmarks = []


    for hand in results.multi_hand_landmarks:

        for point in hand.landmark:

            landmarks.append(point.x)
            landmarks.append(point.y)


    return landmarks