import joblib

from app.services.hand_detector import extract_landmarks


model = joblib.load(
    "trained_model/sign_model.pkl"
)


def predict_sign(image_bytes):

    landmarks = extract_landmarks(
        image_bytes
    )


    if landmarks is None:

        return "No hand detected"


    prediction = model.predict(
        [landmarks]
    )


    return prediction[0]